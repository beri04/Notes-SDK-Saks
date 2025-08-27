import json 
import os

class Notes:
    def __init__(self,file_name = "notes.json"):
        self.file_name = file_name
        self.notes = self.load_notes()

    def load_notes(self):
        if os.path.exists(self.file_name):
            with open(self.file_name,"r") as f:
                return json.load(f) # this load json into the py dict
        else:
            return{}
        
    def save_notes(self):
        with open(self.file_name,"w") as f:
            json.dump(self.notes,f,indent= 4)

    # This is the functon to create the a dictionary 
    def create(self,dict_name,content):
        self.notes[dict_name] = content
       
        self.save_notes() 
        return f"Note {dict_name} created"
    


    # This is the functon to read the a dictionary name 
    def read(self,dict_name):
        return self.notes.get(dict_name,"Note doesn't exists")
    
    # This is the functon to update the a dictionary 
    def update(self,dict_name,new_content):
        if dict_name in self.notes:
            self.notes[dict_name] = new_content
            self.save_notes()
            return f"Note '{dict_name}' is updated"
        else:
            return "Note is not founded"

    # This is the functon to delete the a dictionary     
    def delete(self,dict_name):
        if dict_name in self.notes:
            del self.notes[dict_name]
            self.save_notes()
            return f"Note {dict_name} is deleted"
        else:
            return "Nothing to delete"
        
    # This is the functon to read all content in the dictionary 
    def get_all(self):
        return self.notes
