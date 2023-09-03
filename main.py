import json
from core.database import Database
from uuid import uuid4

db = Database(f"room_{str(uuid4())}")
db.find_room("23")



# db.add({"message": "Hai!", "sender": "12345678"})
# db.add({"message": "Hai!", "sender": "123456789"})

# data = db.read()
# for item in data:
#     item = json.loads(item)
#     print(item['message'])