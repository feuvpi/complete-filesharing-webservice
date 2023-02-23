import os
from dotenv import load_dotenv

load_dotenv()

MYSQL_HOST = os.environ.get('MYSQL_HOST')
MYSQL_USER = os.environ.get('MYSQL_USER')
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
MYSQL_DB = os.environ.get('MYSQL_DB')



# MONGODB_SETTINGS = {
#     'host': 'mongodb://mongo:27017/your_db_name'
# }