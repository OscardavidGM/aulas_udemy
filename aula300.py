import os

from dotenv import load_dotenv

load_dotenv()

# print(os.environ)

print(os.getenv('BD_PASSWORD'))
