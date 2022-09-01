'''Creates a unique 'FileStorage' instance for our application
'''
from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
