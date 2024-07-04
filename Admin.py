from datetime import date
from task import Task
import pickle
import pandas as pd

from tabulate import tabulate

class Admin(Task):
    """
    Manages a collection of tasks.

    Attributes:
        tasks (dict): A dictionary that stores the tasks, with the task ID as the key.
        file_name (str): The name of the file used to save and load the task data.
    """
    file_name = "Tasks.pickle"
    def __init__(self) -> None:
     self.task={}
    
     self.load_from_file(Admin.file_name)




    def add_task(self,task:Task):
       """
       Adds a new task to the collection.
       """
       self.task[task.get_id()]=task
       
       self.save_to_file(Admin.file_name)
    
    def delete_task(self,id ):
        """
        delete a task from the collection.
        
        Args:
            task_id (str): The ID of the task to be deleted  
        """
        if id in self.task:
            del self.task[id]
            self.save_to_file(Admin.file_name)
            print(f"task with id ({id}) have been deleted")
        else:
            print(f" there is no task with id ({id}) ")
           
    
    def edit_task(self,id,titel,responsable,start_date,end_date,status):
        '''
        Edits an existing task in the collection .
        '''

        if id in self.task:
          if titel: 
              self.task[id].set_titel(titel)
          if responsable:
              self.task[id].set_responsable(responsable)
          if start_date:
              self.task[id].set_start_date(start_date)
          if end_date:
             self.task[id].set_end_date(end_date)

          if status:
              self.task[id].set_status(status)
          self.save_to_file(Admin.file_name)
        else:
            raise Exception("Task not found ...")
        
    def task_exists(self, id):
        """
        Checks if a task with the given ID exists in the collection.
        Returns:
            bool: True if the task exists, False otherwise
        """
        return id in self.task
    
    def display_task(self):
     """
     Displays all the tasks in the collection in a formatted table.
    """
     self.task_panda = {}
    
     for id, task in self.task.items():

        self.task_panda[id] = {
            '     id   ': task.get_id(),
            '     titel   ': task.get_titel(),
            'responsable':task.get_responsable(),
            '     start_date   ': task.get_start_date(),
            '     end_date   ': task.get_end_date(),
            '     status   ': task.get_status(),
            '     comment   ': task.get_comment()
        }
    
    # Create the Pandas DataFrame from the self.task_panda dictionary
     self.task_panda = pd.DataFrame.from_dict(self.task_panda, orient='index')
    
    # Print the task details in a formatted table
     print(tabulate(self.task_panda, headers='keys', tablefmt='grid'))
         
    def display_member_tasks(self, responsable):
        """
        Displays all the tasks for a specific responsible person in a formatted table.
        """
        self. tasks_by_member = {}

        for id ,task in self.task.items():
            if task.get_responsable().lower() == responsable.lower():
                self.tasks_by_member [id]= {
                    'id': task.get_id(),
                    'titel': task.get_titel(),
                    'start_date': task.get_start_date(),
                    'end_date': task.get_end_date(),
                    'status': task.get_status(),
                    'comment': task.get_comment()
                }

        if self.tasks_by_member:
            print(f"Tasks for responsable: {responsable}")
            print()

            self.tasks_by_member_panda = pd.DataFrame.from_dict(self.tasks_by_member, orient='index')
            print(tabulate(self.tasks_by_member_panda, headers='keys', tablefmt='grid'))

        else:
          print(f"No tasks found for responsable: {responsable}")

    def save_to_file(self, filename: str):
        """
        Saves the task data to a file.
        """
        with open(filename, "wb") as file:
              pickle.dump(self.task, file)
  
    def load_from_file(self, filename: str):
        """
        Loads the task data from a file.
        """
        try:
              with open(filename, "rb") as file:
                  self.task = pickle.load(file)
        except:
              pass  
  



    

    


 
         



  

  
