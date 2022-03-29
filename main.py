from flask import Flask, send_from_directory
from flask_cors import CORS
import json
import os
from datetime import datetime

app = Flask('app')
CORS(app)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def hello_world():
  return 'Hello, World!'

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/lasit')
def lasit():
  with open('dati/chats.json', 'r', encoding="utf-8") as f:
    chats = f.read()
  
  return chats


@app.route('/stats')
def stats():
  with open('dati/chats.json', 'r', encoding="utf-8") as r:
    vecie = r.read()
    rindas = json.loads(vecie)
    chata_garums = len(rindas)
  return "Čatā ir " + str(chata_garums) + " ieraksti."


@app.route('/sutit/<vards>/<zina>')
def sutit(vards, zina):
  tagad = datetime.now()
  laiks = tagad.strftime("%Y/%m/%d, %H:%M:%S")

  # "/sutit/Anna/Labrīt visiem!"
  rinda = {
      "zina": zina,
      "vards": vards,
      "laiks": laiks
  }
  with open('dati/chats.json', 'r', encoding="utf-8") as r:
    vecie = r.read()
    rindas = json.loads(vecie)

  #if vards == "Serveris":
   # rinda["vards"] = "Blēdis"
  
  if zina == "!stats":
    chata_garums = len(rindas)
    rinda["zina"] = "Čatā ir " + str(chata_garums) #+ " ieraksti."
    rinda["vards"] = "Serveris"
  #elif zina =="!joks":
    #joks = "Briesmīgi smieklīgs joks ..."
    #rinda ["vards"]= "Serveris"
    #rinda["zina"] = joks

  rindas.append(rinda)
  
  with open('dati/chats.json', 'w', encoding="utf-8") as f:
    f.write(json.dumps(rindas, indent=2, ensure_ascii=False))
    
  return "OK"


app.run(host='0.0.0.0', port=8080)
