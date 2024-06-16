from flask import Flask, request, render_template, redirect, url_for, jsonify
import threading
from time import sleep

app = Flask(__name__)

loop_running = False
i = 0

@app.route("/", methods=["POST", "GET"])
def index():
    return render_template('index.html', loop_status=get_loop_status_str())

def get_loop_status_str():
    if loop_running:
        return "Running"
    return "Stopped"

@app.route("/startloop", methods=["POST"])
def start_loop():
    global loop_running
    loop_running = True   
    return redirect(url_for("index"))

@app.route("/stoploop", methods=["POST"])
def stop_loop():
    global loop_running
    loop_running = False   
    return redirect(url_for("index"))

@app.route("/getnumber", methods=["GET"])
def get_current_number():
    global i
    return jsonify(i)

def infinite_loop():
    global i
    while True:
        if loop_running:
            print(i)
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
