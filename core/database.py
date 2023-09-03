import json


class Database:
    def __init__(self, db_name: str = None) -> None:
        self.db_name = db_name
        self.db_path = f"data/{db_name}.txt"

    def add(self, data: dict):
        with open(self.db_path, 'a') as f:
            f.write(f"{json.dumps(data)}\n")
    
    def read(self):
        data = []
        
        with open(self.db_path, 'r') as f:
            for line in f:
                data.append(line)
                
        return data
    
    def find_room(self, room_id: str):
        import os
        directory = 'data'
        
        room = None
        for filename in os.listdir(directory):
            f = os.path.join(directory, filename)
            if os.path.isfile(f):
                room_name = str(f)
                if room_id in room_name:
                    # data\room_42e36725-081f-4b32-ab7e-6e904ca66ec9.txt
                    
                    splitted_text = room_name.split("_")
                    # ["data\room", "42e36725-081f-4b32-ab7e-6e904ca66ec9.txt"]
                    
                    filename = splitted_text[1]
                    # "42e36725-081f-4b32-ab7e-6e904ca66ec9.txt"
                    
                    filename = filename.split(".")
                    # ["42e36725-081f-4b32-ab7e-6e904ca66ec9", "txt"]
                    
                    room_name = filename[0]
                    # 42e36725-081f-4b32-ab7e-6e904ca66ec9
                    
                    if room_name == room_id:
                        room = room_name
                
        return room