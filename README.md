# AgriHUB: Smart Pest & Crop Health Monitoring System  

## Overview  
AgriHUB is an advanced agricultural monitoring system that leverages deep learning and IoT technology to assist farmers in detecting crop diseases, monitoring soil and water conditions, and receiving real-time weather insights. The system is optimized for offline operation on a Raspberry Pi and provides user-friendly access to critical agricultural data.  

## Features  
✅ **Pest & Disease Detection**: Uses YOLOv8 deep learning models to detect pests and diseases in Rice, Wheat, and Sugarcane.  
✅ **IoT-Based Monitoring**: Water level, flow rate, and soil moisture sensors provide real-time environmental data.  
✅ **Weather Forecasting**: Integrates Weather API for real-time weather updates and short-term forecasts.  
✅ **Offline Support**: Runs natively on Raspberry Pi sequentially for real-time processing in remote areas.  

## System Architecture  
1. **YOLOv8 Model**: Trained to recognize common crop diseases and pests.  
2. **IoT Sensors**:  
   - **Water Level Sensor**: Monitors irrigation levels.    
   - **Soil Moisture Sensor**: Prevents over/under-watering.  
3. **Weather Data Integration**: Fetches real-time weather information using Weather API.  
4. **User Dashboard**: Provides intuitive visualization of sensor data and AI-based insights.  

## Hardware Components  
- **Raspberry Pi 5** (for offline processing)  
- **Arduino UNO** (to interface with sensors)  
- **IoT Sensors**: Water level and soil moisture sensors  

## Model Optimization  
To ensure efficient execution on Raspberry Pi, the YOLOv8 model may be optimized using:  
- **ONNX** and **TFLite** conversion for reduced size and faster inference.  
- **Quantization techniques** for running deep learning models on low-power hardware.  

## Benefits  
✅ **Improved Crop Yields**: Early disease detection helps in timely intervention.  
✅ **Resource Optimization**: Smart irrigation reduces water and fertilizer waste.  
✅ **Cost-Effective**: Low-power hardware ensures sustainability for small-scale farmers.  
✅ **Farmer Empowerment**: Easy-to-use interface delivers actionable insights.  

## How to Run  
1. **Clone the Repository**  
   git clone https://github.com/thunderbolt27/AgriHUB_Numericals.git
   cd AgriHUB
2. **Install Dependencies**
	pip install -r requirements.txt
3. **Run the files**
	python seq_model_runner.py
	python dashboard.py
4. **Access the dashboard**
	Access the dashboard via http://localhost:8050
