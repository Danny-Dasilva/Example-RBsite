from flask import Flask, render_template, flash, redirect, render_template, \
     request, url_for
from flask_socketio import SocketIO
from flask_socketio import send, emit 
import csv
import urllib.request
import codecs
import time
import random
# data preprocessing
#HS CSV
data = urllib.request.urlopen('https://raw.githubusercontent.com/DannylDasilva/F/master/HS.csv')
reader = csv.reader(codecs.iterdecode(data, 'utf-8', errors='replace'))
build = list(reader)
columns = build[0]
build = build[1:]
HS2 = {}
for row in build:
  dict = {columns[1]: row[1], columns[2]: row[2], columns[3]: row[3]}
  HS2[row[0]] = dict

#MS CSV
with open('MS.csv', 'r') as infile:
  reader = csv.reader(infile)
  build = list(reader)
columns = build[0]
build = build[1:]
MS2 = {}
for row in build:
  dict = {columns[1]: row[1], columns[2]: row[2], columns[3]: row[3]}
  MS2[row[0]] = dict



app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/admin')
def s3_admin():
  return render_template('index.html')

@app.route('/admin/reset', methods=['POST'])
def s3_reset():
  socketio.emit('msg', {'msg': 'reset'}, broadcast=True)

@app.route('/admin/start', methods=['Post'])
def test4():
  #hs = render_template('HS.html', row= HS)
  time.sleep(3)
  redform = request.form.get('Red')
  blueform = request.form.get('blue')
  print(str(redform))
  #select1 = request.form.get('Blue')
  socketio.emit('msg', {'q': 'q', 'Red': str(redform), 'total': int(request.form['total'])}, broadcast=True)
  return '<html>working</html>'

redlevel = redform
bluelevel = blueform

@app.route('/screen')
def s3_screen():
  return render_template('screen.html')


@app.route('/team/<color>')
def s3_team_screen(color):
  level = redlevel if color == red else bluelevel
  if level == "HS": 
    dictionary = MS2[random.choice(list(MS2.keys()))]
  elif level == "MS": 
    dictionary = HS2[random.choice(list(HS2.keys()))]
  
  else dictionary = {"":""}:
  return render_template('team.html', color=color, row=dictionary)


if __name__=='__main__':
    app.run(debug=True)