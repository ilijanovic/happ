
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)




from flask import Flask

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