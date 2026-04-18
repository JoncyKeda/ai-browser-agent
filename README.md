# 🌐 AI Browser Automation Agent

---

## 📌 Overview

AI Browser Automation Agent is an intelligent system that automates web tasks using natural language instructions. It uses a Large Language Model (LLM) to plan tasks and a browser automation tool (Playwright) to execute them in real time.

Users can give tasks like searching products, extracting information, or navigating websites, and the AI agent performs the actions automatically.

---

## ✨ Features

- Natural language task input
- AI-powered task planning
- Automated browser execution
- Web data extraction
- Simple UI using Streamlit

---

## 🧠 Tech Stack

- Python
- Streamlit
- OpenAI API (LLM)
- Playwright (browser automation)

---

## 🏗️ Architecture

User Task  
   ↓  
LLM Planning  
   ↓  
Browser Automation (Playwright)  
   ↓  
Data Extraction  
   ↓  
Results Display  

---

## 📂 Project Structure

ai-browser-agent/
│
├── app.py
├── requirements.txt
├── README.md
│
├── utils/
│   ├── planner.py
│   ├── browser.py
│   └── extractor.py

---

## ▶️ How to Run

### 1. Install dependencies

pip install -r requirements.txt  

---

### 2. Install Playwright

playwright install  

---

### 3. Set API Key

Mac/Linux:
export OPENAI_API_KEY=your_api_key  

Windows:
set OPENAI_API_KEY=your_api_key  

---

### 4. Run App

streamlit run app.py  

---

## 💡 Example Usage

Input:
Search iPhone on Amazon and list top products  

Output:
- Product 1  
- Product 2  
- Product 3  

---

## 📬 Author

Joncy Keda - AI Developer  
