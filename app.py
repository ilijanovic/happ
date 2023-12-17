
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(26, GPIO.OUT);
GPIO.setup(19, GPIO.OUT);



from flask import Flask

app = Flask(__name__)

@app.route("/on")
def hello_world():
    GPIO.output(26, GPIO.HIGH);
    GPIO.output(19, GPIO.HIGH); 
    return "work"

@app.route("/off")
def hell():
    GPIO.output(26, GPIO.LOW);
    GPIO.output(19, GPIO.LOW); 
    return "work"