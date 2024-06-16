from flask import Flask, request, render_template, redirect, url_for, jsonify
from flask_socketio import SocketIO, emit
import threading
from time import sleep

app = Flask(__name__)
app.config['SECRET_KEY'] = "super_secret_key"
socketio = SocketIO(app)

loop_running = False
i = 0

@app.route("/", methods=["POST", "GET"])
def index():
    return render_template('index.html')

def get_loop_status_str():
    if loop_running:
        return "Running"
    return "Stopped"

@socketio.on("startloop")
def start_loop():
    global loop_running
    loop_running = True   
    socketio.emit("update_loop_status", loop_running)

@socketio.on("stoploop")
def stop_loop():
    global loop_running
    loop_running = False
    socketio.emit("update_loop_status", loop_running)

@socketio.on("connect")
def socket_connect():
    print("Socket connected")

@socketio.on("disconnect")
def socket_disconnect():
    print("Socket disconnected")

def infinite_loop():
    global i
    while True:
        if loop_running:
            print(i)
            socketio.emit("update_num", i)
            i += 1
            sleep(1)
        else:
            # when loop is paused, the main 'while' loop actually continues running
            # but it now instead is waiting for loop_running to be true
            sleep(0.1)

if __name__ == '__main__':
    loop_thread = threading.Thread(target=infinite_loop)
    loop_thread.daemon = True
    loop_thread.start()
    app.run(debug=True, use_reloader=False)
