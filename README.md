# 🚦 Smart Traffic Signal Controller

A cloud-based, IoT-powered intelligent traffic management system that dynamically adjusts traffic signal timings based on real-time traffic density. Built using serverless AWS architecture, this project is designed to improve urban traffic flow efficiency by responding to real-time data from simulated IoT devices.

---

## 📖 Project Overview

Traditional traffic systems operate on fixed timers, often causing unnecessary delays and congestion. This smart controller introduces real-time responsiveness by:

- Collecting traffic data from simulated sensors
- Analyzing traffic density
- Dynamically adjusting green/red signal durations
- Sending alerts or logs for abnormal conditions

This setup is ideal for learning and demonstrating how IoT and cloud computing can be used to solve real-world urban challenges.

---

## 🚀 Key Features

- 🧠 **Intelligent Decision Making:** Adjusts signal timing based on traffic load.
- ☁️ **Serverless Architecture:** Powered by AWS Lambda, no need to manage servers.
- 📶 **IoT Integration:** Simulated traffic data sent via AWS IoT Core.
- 🛢️ **Real-time Storage:** Uses AWS DynamoDB to store traffic and signal state.
- 🔔 **Notifications:** Sends alerts via AWS SNS in critical situations.
- 📈 **Scalable Design:** Easily extendable to multiple junctions or cities.

---

## 🧰 Tech Stack

**Languages & Tools:** Python, Git, GitHub  
**Cloud Services:** AWS IoT Core, AWS Lambda, DynamoDB, SNS  
**Architecture:** Serverless, Event-driven  
**Extras:** IoT Simulation (Python script).

---

## 🔧 How It Works

1. **Traffic Simulation:**  
   Python scripts simulate traffic data (e.g., number of vehicles at a junction) and send it to AWS IoT Core.

2. **Data Ingestion:**  
   AWS IoT Core acts as the entry point for all incoming traffic data from connected devices.

3. **Data Processing:**  
   AWS Lambda is triggered on data arrival. It analyzes vehicle count and determines optimal green light durations.

4. **Storage:**  
   DynamoDB stores current and historical traffic stats, junction status, and signal timings.

5. **Notification:**  
   If congestion crosses a threshold or errors occur, AWS SNS sends an SMS/email notification to the admin.

6. **Optional:**  
   AWS EventBridge can be configured to run periodic health checks or rule-based alerts.

---

## 📂 Folder Structure
