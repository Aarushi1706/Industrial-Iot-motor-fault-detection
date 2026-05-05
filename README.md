# Industrial-Iot-motor-fault-detection
1.Overview
Industrial IoT-based motor fault detection system using sensor fusion and hybrid ML classification for real-time monitoring and automated protection.This project implements a real-time Industrial IoT (IIoT) system for monitoring and fault detection in electric motors using multi-sensor data and machine learning.
The system continuously monitors motor operating conditions using current, temperature, and vibration sensors. Based on this data, it detects abnormal behavior and triggers automatic shutdown using a relay to prevent equipment damage.

2.System Architecture
Sensors → Feature Extraction → Machine Learning Model → Decision Logic → Relay Control → Dashboard

3.Hardware Components
Raspberry Pi
ACS712 Current Sensor
DS18B20 Temperature Sensor
MPU6050 (Vibration Sensor)
PCF8591 ADC
Relay Module

4.Software Architecture
realtime.py → Main execution loop
main.py → Feature extraction and windowing
relay.py → Motor control logic
dashboard.py → Real-time visualization

5.Feature Engineering

The following features are extracted from sensor signals:
Current Features
Mean current
RMS current
Standard deviation of current
Temperature Features
Mean temperature
Rate of temperature change
Vibration Features
RMS vibration
Standard deviation of vibration
Peak vibration
Crest factor
Kurtosis

6.Machine Learning Model
Model Used: Random Forest Classifier
Comparison Model: Gradient Boosting
Input: Extracted features
Output Classes:
highCurrent
jam
noload
normal
overload

7.Model Evaluation
Confusion Matrix
Metrics (from test data)
Random Forest:
Accuracy: 95%
Precision (weighted): 96%
Recall (weighted): 95%
F1 Score (weighted): 95%

Gradient Boosting:
Accuracy: 95%
Precision (weighted): 96%
Recall (weighted): 95%
F1 Score (weighted): 96%
Key Observations
High recall indicates the system effectively detects fault conditions
Slight drop in precision for certain classes (e.g., overload) suggests occasional false positives
Model performs consistently across most operating conditions

The system uses a hybrid approach:
Machine learning prediction for classification
Threshold-based logic for safety-critical decisions

## 🧠 System Setup
![System Setup](images/setup.jpg)

## 📊 Dashboard

### ✅ Normal Operation
![Normal](images/normal.jpg)

### ⚠️ Fault Detected
![Fault](images/faulty.jpg)
## 📊 Model Evaluation

### Confusion Matrix
![Confusion Matrix](images/confusion_matrix.png)

8.Limitations
Limited dataset used for training and testing
Low-resolution ADC (PCF8591) affects measurement accuracy
Model performance may vary across different motor types and environments
Dataset imbalance may affect class-wise prediction performance

9.Future Improvements
Time-series modeling using LSTM or GRU networks
Integration with cloud platforms (AWS IoT, MQTT)
Use of higher resolution ADC for improved sensing accuracy
Deployment for multi-machine monitoring systems
Online learning for adaptive fault detection

10.Applications
Industrial motor monitoring systems
Predictive maintenance in manufacturing
Fault detection in rotating machinery
Smart factory automation

## 📄 Project Report

Detailed documentation of the system design, circuit diagrams, and implementation is available here:

👉 [View Full Report](docs/Project_Report.pdf)


