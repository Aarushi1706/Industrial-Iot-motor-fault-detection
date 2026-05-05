# Industrial IoT Motor Fault Detection System

---

**Overview**

Industrial IoT-based motor fault detection system using sensor fusion and hybrid machine learning classification for real-time monitoring and automated protection.

This project implements a real-time IIoT system to monitor electric motor health using multi-sensor data. It detects abnormal behavior and triggers automatic shutdown via a relay to prevent damage.

**Monitored Parameters:**
- Motor Current  
- Temperature  
- Vibration  

---

**System Architecture**

Sensors → Feature Extraction → Machine Learning Model → Decision Logic → Relay Control → Dashboard

---

**Hardware Components**

- Raspberry Pi  
- ACS712 Current Sensor  
- DS18B20 Temperature Sensor  
- MPU6050 (Vibration Sensor)  
- PCF8591 ADC  
- Relay Module  

---

**Software Architecture**

- `realtime.py` → Main execution loop  
- `main.py` → Feature extraction and windowing  
- `relay.py` → Motor control logic  
- `dashboard.py` → Real-time visualization  

---

**Feature Engineering**

**Current Features**
- Mean current  
- RMS current  
- Standard deviation of current  

**Temperature Features**
- Mean temperature  
- Rate of temperature change  

**Vibration Features**
- RMS vibration  
- Standard deviation of vibration  
- Peak vibration  
- Crest factor  
- Kurtosis  

---

**Machine Learning Model**

- Model Used: Random Forest Classifier  
- Comparison Model: Gradient Boosting  

**Input:**  
Extracted statistical features from sensor signals  

**Output Classes:**
- highCurrent  
- jam  
- noload  
- normal  
- overload  

**Approach:**  
A hybrid strategy is used:
- Machine learning for classification  
- Rule-based thresholds for safety-critical decisions  

---

**Model Evaluation**

**Confusion Matrix**
![Confusion Matrix](images/confusion_matrix.png)

**Metrics (Test Data)**

**Random Forest**
- Accuracy: 95%  
- Precision (weighted): 96%  
- Recall (weighted): 95%  
- F1 Score (weighted): 95%  

**Gradient Boosting**
- Accuracy: 95%  
- Precision (weighted): 96%  
- Recall (weighted): 95%  
- F1 Score (weighted): 96%  

**Key Observations**
- High recall indicates effective detection of fault conditions  
- Slight drop in precision for certain classes (e.g., overload) suggests occasional false positives  
- Model performs consistently across most operating conditions  

---

**System Setup**
![System Setup](images/setup.jpg)

---

**Dashboard**

**Normal Operation**
![Normal](images/normal.jpg)

**Fault Detected**
![Fault](images/faulty.jpg)

---

**Limitations**

- Limited dataset used for training and testing  
- Low-resolution ADC (PCF8591) affects measurement accuracy  
- Model performance may vary across different motor types and environments  
- Dataset imbalance may affect class-wise prediction performance  

---

**Future Improvements**

- Time-series modeling using LSTM or GRU networks  
- Integration with cloud platforms (AWS IoT, MQTT)  
- Use of higher resolution ADC for improved sensing accuracy  
- Deployment for multi-machine monitoring systems  
- Online learning for adaptive fault detection  

---

**Applications**

- Industrial motor monitoring systems  
- Predictive maintenance in manufacturing  
- Fault detection in rotating machinery  
- Smart factory automation  
## 📄 Project Report

Detailed documentation of the system design, circuit diagrams, and implementation is available here:

👉 [View Full Report](docs/Project_Report.pdf)


