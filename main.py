from fastapi import FastAPI, Request, Form
from fastapi.middleware.cors import CORSMiddleware
import hashlib
import json
from os import environ
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import random
import string


def generate_id(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return "id" + result_str


cred = credentials.Certificate(environ['GOOGLE_APPLICATION_CREDENTIALS'])

firebase_admin.initialize_app(cred,{
    'databaseURL': environ['DB_URL']
})

db_ref = db.reference("tables")

app = FastAPI()

origins = [
    "http://armelline.com",
    "https://www.armelline.com",
    "https://armelline.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/all")
async def receive_table(request: Request, sig: str = Form(...), params: str = Form(...)):

  # SHA1 hash check of param data
  '''
  content_sig = hashlib.sha1(params.encode('utf-8')).hexdigest()
  if content_sig != sig:
    # Failed security check
    return { "Status": "Failure" }
  '''
  
  print(params)
  
  #print("Received Params:", params)
  
  data = json.loads(params)
  
  #print("Parsed Data:", data)

  for id in data:
    db_ref.child(id).set(data[id])
   
  # Return success
  return {
    "Status": "Success"
  }


@app.post("/change")
async def change_tables(request: Request, sig: str = Form(...), params: str = Form(...)):

  # SHA1 hash check of param data
  '''
  content_sig = hashlib.sha1(params.encode('utf-8')).hexdigest()
  if content_sig != sig:
    # Failed security check
    return { "Status": "Failure" }
  '''
  
  print(params)
  
  params = json.loads(params)
  added = params["added"]
  deleted = params["deleted"]
  
  for id in deleted:
    db_ref.child(id).delete()
    
  if added:
    
    newtable = '''{"Children":[{"Name":"","Properties":[{"Name":"rowCount","Value":16},{"Name":"columnCount","Value":40},{"Name":"0-1-name","Value":"Math Juice"},{"Name":"0-1-type","Value":1},{"Name":"0-2-name","Value":"Grind 2"},{"Name":"0-2-type","Value":2},{"Name":"0-3-name","Value":"Grind 3"},{"Name":"0-3-type","Value":2},{"Name":"0-4-name","Value":"Grind 4"},{"Name":"0-4-type","Value":1},{"Name":"0-5-name","Value":"GameOver 1"},{"Name":"0-5-type","Value":2},{"Name":"0-6-name","Value":"GameOver 2"},{"Name":"0-6-type","Value":1},{"Name":"0-7-name","Value":"Gameover 3"},{"Name":"0-7-type","Value":2},{"Name":"0-8-name","Value":"Gameover 4"},{"Name":"0-8-type","Value":2},{"Name":"0-9-name","Value":"Gameover 5"},{"Name":"0-9-type","Value":3},{"Name":"0-10-name","Value":"Gameover 6"},{"Name":"0-10-type","Value":3},{"Name":"0-11-name","Value":"Gameover 7"},{"Name":"0-11-type","Value":1},{"Name":"0-12-name","Value":"Gameover 8"},{"Name":"0-12-type","Value":1},{"Name":"0-13-name","Value":"Gameover 9"},{"Name":"0-13-type","Value":1},{"Name":"0-14-name","Value":"Gameover 10"},{"Name":"0-14-type","Value":1},{"Name":"0-15-name","Value":"Gameover 11"},{"Name":"0-15-type","Value":1},{"Name":"0-16-name","Value":"Gameover 12"},{"Name":"0-16-type","Value":1},{"Name":"0-17-name","Value":"Stats 1"},{"Name":"0-17-type","Value":3},{"Name":"0-18-name","Value":"Stats 2"},{"Name":"0-18-type","Value":3},{"Name":"0-19-name","Value":"Stats 3"},{"Name":"0-19-type","Value":3},{"Name":"0-20-name","Value":"Stats Infinity 1"},{"Name":"0-20-type","Value":3},{"Name":"0-21-name","Value":"Stats Infinity 2"},{"Name":"0-21-type","Value":3},{"Name":"0-22-name","Value":"Stats Infinity 3"},{"Name":"0-22-type","Value":3},{"Name":"0-23-name","Value":"Stats Infinity 4"},{"Name":"0-23-type","Value":3},{"Name":"0-24-name","Value":"Highscores 1"},{"Name":"0-24-type","Value":2},{"Name":"0-25-name","Value":"Highscores 2"},{"Name":"0-25-type","Value":2},{"Name":"0-26-name","Value":"Coins 1"},{"Name":"0-26-type","Value":2},{"Name":"0-27-name","Value":"Coins 2"},{"Name":"0-27-type","Value":2},{"Name":"0-28-name","Value":"Coins 3 "},{"Name":"0-28-type","Value":2},{"Name":"0-29-name","Value":"Coins 4"},{"Name":"0-29-type","Value":2},{"Name":"0-30-name","Value":"Coins 5"},{"Name":"0-30-type","Value":2},{"Name":"0-31-name","Value":"Coins 6"},{"Name":"0-31-type","Value":2},{"Name":"0-32-name","Value":"Coins 7"},{"Name":"0-32-type","Value":2},{"Name":"0-33-name","Value":"Coins 8"},{"Name":"0-33-type","Value":2},{"Name":"0-34-name","Value":"Coins 9"},{"Name":"0-34-type","Value":2},{"Name":"0-35-name","Value":"Coins 10"},{"Name":"0-35-type","Value":1},{"Name":"0-36-name","Value":"Consecutive 1"},{"Name":"0-36-type","Value":2},{"Name":"0-37-name","Value":"Consecutive 2"},{"Name":"0-37-type","Value":2},{"Name":"0-38-name","Value":"Consec 3"},{"Name":"0-38-type","Value":2},{"Name":"0-39-name","Value":"Consec 4"},{"Name":"0-39-type","Value":2},{"Name":"0-40-name","Value":""},{"Name":"0-40-type","Value":1}]},{"Name":"","Properties":[{"Name":"1","Value":"|8888888|0|0||0|0|0|0|0.000000|0.000000|||||||0.000000|0.000000|0.000000|0.000000|0.000000|0.000000|0.000000|0|0|300|800|2|0|0|0|712|20|5|1,2,5,6,7,10,|0|966|0|0||"},{"Name":"2","Value":"|8888888|0|0||0|0|0|0|0.000000|0.000000|||||||0.000000|0.000000|0.000000|0.000000|0.000000|0.000000|0.000000|0|0|200|500|2|0|0|0|73|7|10|1,2,3,4,5,6,7,8,9,10,11,12,|0|966|0|0||"},{"Name":"3","Value":"||0|0||0|0|0|0|0.000000|0.000000|||||||0.000000|0.000000|0.000000|0.000000|0.000000|0.000000|0.000000|0|0|99999|400|2|1|0|1|355|20|5|1,2,3,4,5,6,7,8,9,10,11,12,|0|966|0|0||"},{"Name":"4","Value":"||0|0||0|0|0|0|0.000000|0.000000|||||||0.000000|0.000000|0.000000|0.000000|0.000000|0.000000|0.000000|0|0|100|99999|99999|0|0|0|99999|100|5|1,2,5,6,7,10|0|966|0|0||"},{"Name":"5","Value":"||1|1||0|0|0|0|0.000000|0.000000|||||||0.000000|1.000000|0.000000|0.000000|0.000000|0.000000|0.000000|0|0|99999|10|5|0|0|0|6|20|5|1,2,3,4,5,6,7,8,9,10,11,12,|1|966|1|1||"},{"Name":"6","Value":"||0|0||0|0|0|0|0.000000|0.000000|||||||0.000000|0.000000|0.000000|0.000000|0.000000|0.000000|0.000000|0|0|9999|9999|99999|0|0|0|0|0|0||0|966|0|0||"},{"Name":"7","Value":"||0|0||0|0|0|0|0.000000|0.000000|||||||0.000000|0.000000|0.000000|0.000000|0.000000|0.000000|0.000000|0|0|0|0|0|0|0|0|0|0|0||0|966|0|0||"},{"Name":"8","Value":"||0|0||0|0|0|0|0.000000|0.000000|||||||0.000000|0.000000|0.000000|0.000000|0.000000|0.000000|0.000000|0|0|0|0|0|0|0|0|0|0|0||0|966|0|0||"},{"Name":"9","Value":"||0|0||0|0|0|0|0.000000|0.000000|||||||0.000000|0.000000|0.000000|0.000000|0.000000|0.000000|0.000000|0|0|0|0|0|0|0|0|0|0|0||0|966|0|0||"},{"Name":"10","Value":"||0|0||0|0|0|0|0.000000|0.000000|||||||0.000000|0.000000|0.000000|0.000000|0.000000|0.000000|0.000000|0|0|0|0|0|0|0|0|0|0|0||0|966|0|0||"},{"Name":"11","Value":"||0|0||0|0|0|0|0.000000|0.000000|||||||0.000000|0.000000|0.000000|0.000000|0.000000|0.000000|0.000000|0|0|0|0|0|0|0|0|0|0|0||0|966|0|0||"},{"Name":"12","Value":"||0|0||0|0|0|0|0.000000|0.000000|||||||0.000000|0.000000|0.000000|0.000000|0.000000|0.000000|0.000000|0|0|0|0|0|0|0|0|0|0|0||0|966|0|0||"},{"Name":"13","Value":"||0|0||0|0|0|0|0.000000|0.000000|||||||0.000000|0.000000|0.000000|0.000000|0.000000|0.000000|0.000000|0|0|0|0|0|0|0|0|0|0|0||966|0|0|0||"},{"Name":"14","Value":"||0|0||0|0|0|0|0.000000|0.000000|||||||0.000000|0.000000|0.000000|0.000000|0.000000|0.000000|0.000000|0|0|0|0|0|0|0|0|0|0|0||1|0|0|0||"},{"Name":"15","Value":"||0|0||0|0|0|0|0.000000|0.000000|||||||0.000000|0.000000|0.000000|0.000000|0.000000|0.000000|0.000000|0|0|0|0|0|0|0|0|0|0|0||1|0|0|0||"},{"Name":"16","Value":"||0|0||0|0|0|0|0.000000|0.000000|||||||0.000000|0.000000|0.000000|0.000000|0.000000|0.000000|0.000000|0|0|0|0|0|0|0|0|0|0|0||1|0|0|0||"}]}],"Name":""}'''
    newtable = json.loads(newtable)
    
    for id in added:
      table_id = generate_id(6)
      newtable["Children"][0]["Name"] = table_id + "_headers"
      newtable["Children"][1]["Name"] = table_id
      db_ref.child(id).set(newtable)
  
  
  #print("Parsed Data:", data)

  # Return success
  return {
    "Status": "Success"
  }


# Called when you use "Network Send Table To URL"
@app.post("/")
async def receive_table(request: Request, userId: str, sig: str = Form(...), params: str = Form(...)):

  # SHA1 hash check of param data
  '''
  content_sig = hashlib.sha1(params.encode('utf-8')).hexdigest()
  if content_sig != sig:
    # Failed security check
    return { "Status": "Failure" }
  '''
  
  print(params)
  
  db_ref.child(userId).set(json.loads(params))
   
  # Return success
  return {
    "Status": "Success"
  }


# Called when you use "Network Get Table From URL"
@app.get("/all")
async def send_tables(request: Request, games: str = ""):
  
  tables = db_ref.get()
  filtered = {}
  
  if games:
    games = games.split(",")
    for table_name in tables:
      prefix = table_name.split("-")[0]
      if prefix in games:
        filtered[table_name] = tables[table_name]
  else:
    filtered = tables
  
  print(filtered)
  
  return filtered


# Called when you use "Network Get Table From URL"
@app.get("/")
async def send_table(userId: str):
  
  table = db_ref.child(userId).get()
  
  print(table)
  
  return table

