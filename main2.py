from flask import Flask
from flask_cors import CORS
import json

app = Flask('app')
CORS(app)

@app.route('/')
def hello_world():
  return 'Hello, World!'


@app.route('/lasit')
def lasit():
  with open('dati/chats.json', 'r') as f:
    chats = f.read()
  
  return chats


@app.route('/sutit/<vards>/<zina>')
def sutit(vards, zina):
  # "/sutit/Anna/Labrīt visiem!"
  rinda = {
      "zina": zina,
      "vards": vards
  }
  with open('dati/chats.json', 'r') as r:
    vecie = r.read()
    vecieJson = json.loads(vecie)

  print(vecieJson)
  print(rinda)
  # with open('dati/chats.json', 'w') as f:
    
    
  return "OK"


@app.route('/sutit')
def sutit2():
  # "/sutit?vards=Anna&zina=Labrīt"
  return True



app.run(host='0.0.0.0', port=8080)
