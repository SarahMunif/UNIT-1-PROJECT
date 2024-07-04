from datetime import date 
class Task :
    def __init__(self,titel:str,responsable:str,start_date,end_date,id:str,comment:str=None) -> None:
        self.__id=id
        self.__start_date=start_date
        self.__end_date=end_date
        self.__responsable=responsable
        self.__status='to do'
        self.comment=comment
        self.titel=titel
        self.today=date.today()

            
    def set_id(self,id):
       self.__id=id
    def get_id(self):
        return self.__id
    def set_start_date(self, start_date):
        self.__start_date=start_date
    def get_start_date(self):
       return self.__start_date
    
    def set_end_date(self, end_date):

        self.__end_date=end_date


    def get_end_date(self):
        
       return self.__end_date
    


    
    def set_responsable(self, responsable):
            self.__responsable = responsable
    def get_responsable(self):
       return self.__responsable
    def set_titel(self, titel):
            self.titel = titel
    def get_titel(self):
       return self.titel
    
    def set_status(self,status):
        if status in ['to do', 'in progress', 'done']:
            self.__status = status
        else:
            raise ValueError("Invalid status. Choose 'to do', 'in progress', or 'done'.")
    def get_status(self):
       return self.__status
    
    def set_comment(self,comment):
       self.comment=comment

    def get_comment(self):
       return self.comment
            




    



          
    
    
    def __str__(self):
        return (f"Task ID: {self.get_id()}, Title: {self.get_titel()}, Start Date: {self.get_start_date()}, "
                f"End Date: {self.get_end_date()}, Status : {self.get_status()}")