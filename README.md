🚦 Smart Traffic Signal Controller
A cloud-based, IoT-driven traffic management system that dynamically controls traffic signal timings based on real-time traffic data. This project uses AWS services to simulate, process, and respond to changing traffic conditions in a smart and automated way.

📌 Features
Real-time traffic data simulation
Intelligent signal timing based on traffic density
Serverless processing using AWS Lambda
Data storage with AWS DynamoDB
Alerts and monitoring with AWS SNS
Scalable and fully event-driven architecture
🧰 Tech Stack
Python, AWS IoT Core, AWS Lambda, DynamoDB, SNS, GitHub, IoT Simulation

🛠️ How It Works
Traffic Simulation:
Simulated IoT traffic devices send data (vehicle count, congestion level) to AWS IoT Core.

Data Processing:
AWS Lambda functions are triggered on data arrival to analyze traffic density and decide signal durations.

Storage:
All traffic data, signal statuses, and history are stored in DynamoDB.

Notifications:
AWS SNS sends alerts (e.g., heavy congestion, system failure) via email or SMS.

Optional Automation:
AWS EventBridge can trigger periodic checks for traffic conditions.

📂 Project Structure
