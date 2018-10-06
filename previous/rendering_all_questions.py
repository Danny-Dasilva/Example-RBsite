from flask import Flask, render_template, request, jsonify, json, url_for
from pusher import Pusher
import uuid
import json
from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_socketio import send, emit 
import jinja2
import csv


with open('Questions.csv', 'r') as infile:
  reader = csv.reader(infile)
  build = list(reader)

columns = build[0]
build = build[1:]

build2 = {}

for row in build:
  dict = {columns[1]: row[1], columns[2]: row[2]}
  build2[row[0]] = dict

# create flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


# index route, shows index.html view
@app.route('/')
def index():
  return render_template('index.html')



@app.route('/screen')
def screen():
  return render_template('screen.html')

# feed route, shows feed.html view
@app.route('/red')
def red():
  return render_template('red.html')
  
@app.route('/blue')
def blue():
  return render_template('blue.html')

@app.route('/HS')
def HS():
  return render_template('faq.html', build=build2)


@app.route('/MS')
def MS():
  return render_template('MS.html')


@app.route('/ES')
def ES():
  return render_template('ES.html')

@app.route('/end')
def end():
  return render_template('end.html')


@app.route('/files')
def files():
  return render_template('files.html')

def json():
    json_data = open(url_for('static', filename="static/json/test.json"))
    data = json.load(json_data)
    return render_template('taiwan.jade', data=data)

#red High School Middle School and Elementary teams
@app.route('/admin/HS', methods=['POST'])
def redHS(): 
  socketio.emit('msg', {'msg': 'HS'}, broadcast=True)
  return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

@app.route('/admin/MS', methods=['POST'])
def redMS():
  socketio.emit('msg', {'msg': 'MS'}, broadcast=True)
  return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

@app.route('/admin/ES', methods=['POST'])
def redES():
  socketio.emit('msg', {'msg': 'ES'}, broadcast=True)
  return json.dumps({'success':True}), 200, {'ContentType':'application/json'}


#reset Function
@app.route('/admin/reset', methods=['POST'])
def reset():
  socketio.emit('msg', {'msg': 'reset'}, broadcast=True)
  return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

'''
@app.route('/admin/button2', methods=['POST'])
def button():
  socketio.emit('msg', {'msg': 'start'}, broadcast=True)
  return json.dumps({'success':True}), 200, {'ContentType':'application/json'}
'''
# websockets


# run Flask app in debug mode
if __name__ == '__main__':
    socketio.run(app)