
class InputError(Exception):
    """Custom exception for invalid input."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

import json
import colorama
from colorama import Fore, Style
from datetime import date,datetime
from openai import OpenAI
from Admin import Admin
from task import Task
from member import Member
admin=Admin()
member=Member()


client = OpenAI(api_key=key)
colorama.init(autoreset=True)
def save_json(output, file_name='output.json'):
    try:
        # Try to parse the string to JSON
        json_object = json.loads(output)
        with open(file_name, 'w') as file:
            json.dump(json_object, file, indent=4)
        print("JSON file has been saved.")
    except json.JSONDecodeError:
        print("Failed to parse JSON. Please check the model output for errors.")
def clean_json_string(json_string):
    # Check if the string starts and ends with triple backticks
    json_string=json_string.replace("```json","").replace("```","")
    return json_string       
def get_non_empty_input(prompt):
    """Function to get non-empty input from the user."""
    while True:
        user_input = input(prompt)
        if user_input.strip():  # Checks if input is not just whitespace
            return user_input
        else:
            print("This field cannot be empty. Please enter a valid input.")



def validate_date(date_str):

    try:
        return datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        print(Fore.RED + "Invalid date format. Please use the format YYYY-MM-DD.")
        return None


def handle_new_user():


    with open('suggested_format.txt', 'r') as f:
        suggested_format=f.read()

    
    # Get user input
    project_details = input("Please enter the project idea, the members working on it, and their roles, start and end date for the project : ")
    print("......this may take a while don't worry......")

    prompt =  f""" You are an project manager expert and you are required to do the following for the project idea:\n
    Analyze the project idea {project_details}\n
    and Subdivide it into specific tasks that covers all the project goals.\n
    Analyze and estimate each task to have a start and end date in the format YYYY-MM-DD.\n
    Assign a unique ID for each task.\n
    Assign a task for a responsible member.\n
    Return the output as a JSON file and strictly follow this format:\n\n
    {suggested_format}\n\n
    please dont add any words out of the json format
    """
    response = client.chat.completions.create(
        model="gpt-4-turbo-preview",
        temperature=0.4,
        messages=[
            {"role": "system", "content": "You are a helpful and team lead assistant."},
            {"role": "user", "content": prompt}
        ]
    ) 


 
    def parse_ai_output(ai_output_string):
        tasks = []
        ai_data = json.loads(ai_output_string)  # Load string as JSON
        
        # Dynamically determine the number of tasks
        task_indices = set()
        for key in ai_data.keys():
            # Extract task number from keys like "Task 1", "Task_1_srtdt", etc.
            if key.startswith("Task_"):
                task_number = key.split('_')[1]
                if task_number.isdigit():
                    task_indices.add(int(task_number))
        
        # Iterate over each task index found
        for i in sorted(task_indices):
            title_key = f"Task {i}"
            if title_key in ai_data:
                title = ai_data[title_key]
                start_date = ai_data[f"Task_{i}_srtdt"]
                end_date = ai_data[f"Task_{i}_etc"]
                responsible = ai_data[f"Task_{i}_responsible"]
                task_id = ai_data[f"Task_{i}_id"]
                
                task = Task(title, responsible, start_date, end_date, task_id)
                tasks.append(task)
    
        return tasks

    ai_output = response.choices[0].message.content
    ai_output=clean_json_string(ai_output)
    print(f"ai_output\n {ai_output}")
    save_json(ai_output)
    # Parse AI output and create Task instances
    tasks = parse_ai_output(ai_output)
    admin=Admin()

  
    for task in tasks:
         admin.add_task(task)
    print("Admin view ")
    admin.display_task()



print(Fore.CYAN + Style.BRIGHT + "Welcome to the TaskTrack  System!")
while True:
  log_in_choice = input(" Enter \n'Project Manager' if you are a Project Manager of existing project\n'new' if you are a New Project Manager\n'member' if you are an Existing Member\n: ").lower()
  
  if log_in_choice == "new":
        handle_new_user()
        input("")

    
  elif log_in_choice == "project manager":
        while True:  
          try:
    
            print(Fore.GREEN + "Project Manager Menu:")
            print("  [add] Add a Task")
            print("  [delete] Delete a Task")
            print("  [edit] Edit a Task")
            print("  [info] View All Tasks")
            print("  [member tasks] View Member's Tasks")
            print("  [exit] Exit")
            
            choice = input("What would you like to do? ").lower()
    
            if choice=="exit":
                print(Fore.YELLOW + "Exiting... Thank you for using the system!")
                input("")

                break
            if choice.lower()=="add":
             try:
                title=get_non_empty_input("Task Title :  ")
                responsable=get_non_empty_input("Responsible Person :  ")
                start_date_str=get_non_empty_input("Start Date (YYYY-MM-DD): ")
                end_date_str=get_non_empty_input("End Date (YYYY-MM-DD): ")
                start_date = validate_date(start_date_str)
                end_date = validate_date(end_date_str)
                if not start_date or not end_date:
                    continue
                id = get_non_empty_input("Task ID: ")

                      
    
                # Simulating task addition logic
                task=Task(title,responsable,start_date,end_date,id)
    
                admin.add_task(task)
                print(Fore.GREEN + f"Task ({id})successfully added.")
                input(" ")
             except InputError as e:
                 print(e)    
            input(" ")        
            if choice.lower()=="delete":
                id=input("Eneter the id of the task you wants to delete : ")
                admin.delete_task(id)
                input("")
    
            if  choice.lower()=="edit":
                id = input("Task ID for the task you want to edit : ")
                title=input("Task Title :  ")
                responsable=input("Responsible Person :  ")
                start_date=input("Start Date (YYYY-MM-DD): ")
                end_date=input("End Date (YYYY-MM-DD): ")
    
                status = input("Initial Status: ")

                admin.edit_task(id,title,responsable,start_date,end_date,status)
                input("")
    
            if choice.lower()=="info":
                admin.display_task()
                input("")
            if choice.lower()=="member tasks":
                responsable=input("Enter the task responsable to view their tasks : ")
                admin.display_member_tasks(responsable)
                input("")
    


          except Exception as e:
              print(f"An error occurred: {e}")
    
  elif log_in_choice == "member":
    
        member_name = input("Please enter your name: ").lower()
        print(Fore.CYAN + f"Welcome, {member_name}!")  
        while True:  
          try:            
            print(Fore.GREEN + "Member Menu:")
            print("  [edit status] Edit Task Status")
            print("  [comment] Add/Edit Comment")
            print("  [info] View Your Tasks")
            print("  [exit] Exit")
    
            choice = input("What would you like to do? ").lower()
            if choice.lower()=="exit":
                print(Fore.YELLOW + f"Goodbye, {member_name}👋! Thank you for your visit.")
                input("")
                break

    
            if choice.lower()=="edit status":
                id=input("Enter the id of the task you want to edit : ")
                status=input("Enter the new status : ")
                member.edit_status(member_name,id,status)
                input("")
    
            if choice.lower()=="comment":
                id=input("Enter the id of the task you want to edit or add comment to : ")
                comment=input("Enter the new comment : ")           
                member.edit_comment(member_name,id,comment)
                input("")
             
            if choice.lower()=="info":
                member.display_member_tasks(member_name)
                input("")
            elif choice.lower()!=" ":
             raise ValueError (Fore.RED + "Invalid entry. Please try again.")
            

          except Exception as e:
              print(f"An error occurred: {e}")
  else:
        print(Fore.RED + "Invalid entry. Please try again.")
  
  