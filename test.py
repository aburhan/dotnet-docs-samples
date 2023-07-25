import os
import json


print(os.environ['GOOGLE_APPLICATION_CREDENTIALS'])
f = open(os.environ['GOOGLE_APPLICATION_CREDENTIALS'])
# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Iterating through the json
# list
for i in data['emp_details']:
    print(i)

