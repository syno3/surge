# we stream the output to the browser
from flask import Flask, render_template, Response
import cv2
from main import *


run = videoOutput() # we instantiate the class

#Initialize the Flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', visibility="test")

@app.route('/video_feed')
def video_feed():
    return Response(run.stream_buffer(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)