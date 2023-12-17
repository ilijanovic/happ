
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)




from flask import Flask

app = Flask(__name__)

@app.route("/on")
def hello_world():
    GPIO.setup(26, GPIO.OUT);
    GPIO.setup(19, GPIO.OUT);
    GPIO.output(26, True);
    GPIO.output(19, True); 
    return "work";

@app.route("/off")
def hell():
    GPIO.setup(26, GPIO.OUT);
    GPIO.setup(19, GPIO.OUT);
    GPIO.output(26, False);
    GPIO.output(19, False); 
    return "work";