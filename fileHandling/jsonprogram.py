import json

myJfile=open(r'C:\Users\Nrupsh mhatre\Desktop\nrupesh.py\fileHandling\emp.json')
jData=myJfile.read()

object=json.loads(jData)
print(str(object['firstName']))
print(str(object['lastName']))
