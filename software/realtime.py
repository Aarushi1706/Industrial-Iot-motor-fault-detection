import time
import numpy as np
import pandas as pd
import joblib
import smbus
from w1thermsensor import W1ThermSensor
from mpu6050 import mpu6050
import RPi.GPIO as GPIO

# -----------------------
# LOAD MODEL FILES
# -----------------------
model = joblib.load("rf_model.pkl")
scaler = joblib.load("scaler.pkl")
feature_columns = joblib.load("features.pkl")
WINDOW_SIZE = joblib.load("window.pkl")

# -----------------------
# SETUP I2C (PCF8591)
# -----------------------
bus = smbus.SMBus(1)
PCF8591_ADDR = 0x48

def read_adc(channel):
    bus.write_byte(PCF8591_ADDR, channel)
    bus.read_byte(PCF8591_ADDR)
    return bus.read_byte(PCF8591_ADDR)

# -----------------------
# CURRENT SENSOR (ACS712)
# -----------------------
def read_current():
    value = read_adc(0)
    voltage = value * (3.3 / 255)
    current = (voltage - 2.5) / 0.185
    return current

# -----------------------
# TEMPERATURE (DS18B20)
# -----------------------
temp_sensor = W1ThermSensor()

def read_temp():
    return temp_sensor.get_temperature()

# -----------------------
# VIBRATION (MPU6050)
# -----------------------
mpu = mpu6050(0x68)

def read_vibration():
    data = mpu.get_accel_data()
    vib = abs(data['x']) + abs(data['y']) + abs(data['z'])
    return vib

# -----------------------
# RELAY SETUP
# -----------------------
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)

def motor_on():
    GPIO.output(22, 0)

def motor_off():
    GPIO.output(22, 1)

# -----------------------
# BUFFERS
# -----------------------
curr_buffer = []
temp_buffer = []
vib_buffer = []

# -----------------------
# FEATURE EXTRACTION
# -----------------------
def extract_features(curr, temp, vib):

    curr = np.array(curr)
    temp = np.array(temp)
    vib = np.array(vib)

    mean_curr = curr.mean()
    rms_curr = np.sqrt(np.mean(curr**2))
    std_curr = curr.std()

    mean_temp = temp.mean()
    temp_rate = (temp[-1] - temp[0]) / len(temp)

    rms_vib = np.sqrt(np.mean(vib**2))
    std_vib = vib.std()
    peak_vib = vib.max()
    crest = peak_vib / rms_vib if rms_vib != 0 else 0
    kurt = np.mean((vib - vib.mean())**4) / (vib.std()**4 + 1e-6)

    return {
        "mean_curr": mean_curr,
        "rms_curr": rms_curr,
        "std_curr": std_curr,
        "mean_temp": mean_temp,
        "temp_rate": temp_rate,
        "rms_vib": rms_vib,
        "std_vib": std_vib,
        "peak_vib": peak_vib,
        "crest": crest,
        "kurt": kurt
    }

# -----------------------
# MAIN LOOP
# -----------------------
print("System started...")

while True:

    curr = read_current()
    temp = read_temp()
    vib = read_vibration()

    print(f"Curr:{curr:.2f} Temp:{temp:.2f} Vib:{vib:.2f}")

    curr_buffer.append(curr)
    temp_buffer.append(temp)
    vib_buffer.append(vib)

    if len(curr_buffer) >= WINDOW_SIZE:

        features_dict = extract_features(curr_buffer, temp_buffer, vib_buffer)

        features_df = pd.DataFrame([features_dict])
        features_df = features_df[feature_columns]

        features_scaled = scaler.transform(features_df)

        prediction = model.predict(features_scaled)[0]

        print("Predicted Fault:", prediction)

        # OPTIONAL: auto stop motor
        if prediction != "normal":
            print("⚠️ Fault detected! Turning motor OFF")
            motor_off()

        # reset buffers
        curr_buffer.clear()
        temp_buffer.clear()
        vib_buffer.clear()

    time.sleep(0.2)