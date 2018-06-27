import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

enable_pin = 18
coil_A_1_pin = 4 # pink
coil_A_2_pin = 17 # orange
coil_B_1_pin = 23 # blue
coil_B_2_pin = 24 # yellow
 
# adjust if different
StepCount = 8
Seq = range(0, StepCount)
Seq[0] = [0,0,0,1]
Seq[1] = [0,0,1,1]
Seq[2] = [0,0,1,0]
Seq[3] = [0,1,1,0]
Seq[4] = [0,1,0,0]
Seq[5] = [1,1,0,0]
Seq[6] = [1,0,0,0]
Seq[7] = [1,0,0,1]

stepOther = 4
other = range(0, stepOther)
other[0] = [0,0,1,1]
other[1] = [0,1,1,0]
other[2] = [1,1,0,0]
other[3] = [1,0,0,1]
 
GPIO.setup(enable_pin, GPIO.OUT)
GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)
 
GPIO.output(enable_pin, 1)
 
def setStep(w1, w2, w3, w4):
    GPIO.output(coil_A_1_pin, w1)
    GPIO.output(coil_A_2_pin, w2)
    GPIO.output(coil_B_1_pin, w3)
    GPIO.output(coil_B_2_pin, w4)
 
def forward(delay, steps):
    for i in range(steps):
        for j in range(stepOther):
            setStep(other[j][0], other[j][1], other[j][2], other[j][3])
            time.sleep(delay)
 
def backwards(delay, steps):
    for i in range(steps):
        for j in reversed(range(stepOther)):
            setStep(other[j][0], other[j][1], other[j][2], other[j][3])
            time.sleep(delay)

def getSteps(deg):
    steps = deg * 512 / 360
    return steps
 
if __name__ == '__main__':
    while True:
      delay = raw_input("Delay between steps (milliseconds)?")
      degInput = raw_input("How many degrees forward? ")
      forward(int(delay) / 1000.0, getSteps(int(degInput)))

      setStep(0, 0, 0, 0)
      
      degInput = raw_input("How many degrees backwards? ")
      backwards(int(delay) / 1000.0, getSteps(int(degInput)))

      setStep(0, 0, 0, 0)
