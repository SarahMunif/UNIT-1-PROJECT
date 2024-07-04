import pickle
from datetime import date
from task import Task
from Admin import Admin
import pandas as pd
from tabulate import tabulate

class Member (Admin,Task):
    """
    The Member class represents a member of the team and inherits from the Admin and Task classes.

    Attributes:
        file_name (str): The filename to save and load member data.
        tasks_by_member (dict): A dictionary to store tasks assigned to each member.
        admin (Admin): An instance of the Admin class.

    Methods:
        edit_status(self, responsible, id, status): Edit the status for the member Tasks .
        edit_comment(self, responsible, id, comment): Edit or add a comment for  a task .
        display_member_tasks(self, responsible): Display the tasks assigned to the  member.
        save_to_file(self, filename): Save the member's task data to a file.
        load_from_file(self, filename): Load the member's task data from a file.
    """     
    file_name = "member.pickle"
    def __init__(self) -> None:
     self. tasks_by_member = {}
     self.admin=Admin()
     self.load_from_file(Member.file_name)



    def edit_status(self, responsible, id, status):
        """
        Edit the status of a task and assure it done by the responsible member .

        Args:
            responsible (str): The member responsible for the task.
            id (str): The ID of the task to edit.
            status (str): The new status for the task.
        """
        if id in self.admin.task:
            task=self.admin.task[id]

            if task.get_responsable().lower() == responsible.lower():
                task.set_status(status)

                self.admin.save_to_file(self.admin.file_name)
                self.save_to_file(Member.file_name)
            else:
                print(f"Error: {responsible} is not the responsible member for task {id}")
        else:
            print(f"Error: No task found with ID {id}")     
    def edit_comment(self, responsible, id, comment):
        """
        Edit or add  comment of a task and assure it done by the responsible member .
        """
        if id in self.admin.task:
            task=self.admin.task[id]
            if task.get_responsable().lower() == responsible.lower():
                task.set_comment(comment)
                self.admin.save_to_file(self.admin.file_name)
                self.save_to_file(Member.file_name)
            else:
                print(f"Error: {responsible} is not the responsible member for task {id}")
        else:
            print(f"Error: No task found with ID {id}")     

    def display_member_tasks(self, responsable):
        """
        Display the tasks assigned to a the member itself.
        """
        
        member_tasks = []
        for task_id, task in self.admin.task.items():
            if task.get_responsable().lower() == responsable.lower():
                member_tasks.append({
                    'id': task_id,
                    'titel': task.get_titel(),
                    'start_date': task.get_start_date(),
                    'end_date': task.get_end_date(),
                    'status': task.get_status(),
                    'comment': task.get_comment()
                })
        if member_tasks:
            print(f"Tasks for responsable: {responsable}")
            print(tabulate(member_tasks, headers='keys', tablefmt='grid'))
            print()
        else:
            print(f"No tasks found for responsable: {responsable}")
            
    def save_to_file(self, filename: str):
        """
        Save the member's task data to a file.
        """
        with open(filename, "wb") as file:
              pickle.dump(self.admin.task, file)
              pickle.dump(self.tasks_by_member, file)
  
    def load_from_file(self, filename: str):
        """
        Load the member's task data from a file.
        """
        try:
            with open(filename, "rb") as file:
                self.tasks_by_member = pickle.load(file)
        except:
              pass  
  


  
    

