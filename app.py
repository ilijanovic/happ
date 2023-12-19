
import RPi.GPIO as GPIO
from flask import Flask
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(26, GPIO.OUT);
GPIO.setup(19, GPIO.OUT);



app = Flask(__name__)

@app.route("/on")
def hello_world():

    GPIO.output(26, 1)
    GPIO.output(19, 1)
    return "work"

@app.route("/off")
def hell():
   
    GPIO.output(26, 0)
    GPIO.output(19, 0)
    return "work"