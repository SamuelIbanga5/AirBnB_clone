from base_model import BaseModel
from engine.file_storage import FileStorage


fs = FileStorage()
bm = BaseModel()
print(bm.to_dict())
fs.new(bm.to_dict())
# fs.save()