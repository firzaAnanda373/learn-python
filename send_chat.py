from core.database import Database
from uuid import uuid4

class SendChat:
    def execute(self):
        room = input("please input your room id (leave blank to create new): ") 
        if room == '':
          username = input("Input your new username : ")
          db = Database(f"room_{str(uuid4())}")
          self.loop(db, username)
        else:
            # Sample ID: 42e36725-081f-4b32-ab7e-6e904ca66ec9
          db = Database()
          result = db.find_room(room)
          if result == None:
            print("Not Found")
            return
          else:
            db = Database(f"room_{str(result)}")
            
            inp_user = input("Input username : ")
            self.loop(db, inp_user)
    
    def loop(self, db: Database, username: str):
        while True:
          inp_msg = input("Input your message : ")
          data = {
            "username" : username,
            "message" : inp_msg
          }
          db.add(data)
          inp_option = input("Want to send message again ? Y / N")
          inp_option = inp_option.lower()
          if inp_option == 'n':
            break
 
s = SendChat()

while True:
  s.execute()