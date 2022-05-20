import os
from pprint import pprint
import json

file = os.path.join(os.getcwd(), 'school.json')


with open(file, mode='r', encoding='utf-8') as file_json:
   read = json.load(file_json)
   pprint(read)
