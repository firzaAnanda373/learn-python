from core.database import Database
import json

class ListenChat:
    def execute(self):
        db = Database()
        room = input("please input your room id: ")
        find_room = db.find_room(room)
        if find_room == None:
          print("Not found")
        else:
          username = input("Masukkan username : ")
          db = Database(f"room_{str(room)}")
          result = db.read()
          for item in result:
              item = json.loads(item)
              _tmp = item['username']
              if username == item['username']:
                _tmp = 'You'
              # "Firza: test 1"
              # print(item)
              # print(item['username'])
              # print(item['message'])
              print(f"{_tmp} sent : {item['message']}")
              
              # You sent: {message}
              # Ahmed sent: {message}
              
          # print(result)
        

lc = ListenChat()
lc.execute()
        # Bikin loop yang harus membaca setiap chat