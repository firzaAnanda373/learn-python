from core.database import Database
from uuid import uuid4

class SendChat:
    def execute(self):
        room = input("please input your room id (leave blank to create new): ") 
        if room == '':
          username = input("Input your new username : ")
          db = Database(f"room_{str(uuid4())}")
          message = input("Input your message : ")
          data = {
            "username" : username,
            "message" : message
          }
          db.add(data)
        else:
            # Sample ID: 42e36725-081f-4b32-ab7e-6e904ca66ec9
          db = Database()
          result = db.find_room(room)
          if result == None:
            print("Not Found")
            return
          else:
            inp_user = input("Input username : ")
            inp_msg = input("Input your msg : ")
            db = Database(f"room_{str(result)}")
            data = {
              "username" : inp_user, 
              "message" : inp_msg,
            }
            db.add(data)
            print(data)
          # print(result)
          
        
      
        # Bikin loop yang bisa mengirim setiap chat
        
        
s = SendChat()
s.execute()