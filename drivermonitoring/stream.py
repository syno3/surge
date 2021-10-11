# we stream the output to the browser
from flask import Flask, render_template, Response, url_for
from main import videoOutput
import cv2

run = videoOutput() # we instantiate the class

#Initialize the Flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(run.debug(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)