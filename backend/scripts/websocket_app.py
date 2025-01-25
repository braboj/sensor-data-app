import time
from threading import Lock
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='threading')

thread = None
thread_lock = Lock()

def emit_data():
    """Example of how to send server generated events to clients."""
    count = 0
    while True:
        time.sleep(1)
        count += 1
        socketio.emit('message',
                      {'data': 'Server generated event', 'count': count})
@app.route('/')
def index():
    return render_template('index.html')

@socketio.event
def connect():

    # Access the server's global thread variable
    global thread

    # Start the background thread only if the thread has not been started before.
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(emit_data)

    # Send a message to the client
    emit('my_response', {'data': 'Connected', 'count': 0})



if __name__ == '__main__':
    socketio.run(app, allow_unsafe_werkzeug=True)
