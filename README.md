# 🌐 Strategic Supply Chain Orchestrator: LLM-Agentic Decision System

![LLM](https://img.shields.io/badge/LLM-Gemini--1.5--Flash-blue) 
![RL](https://img.shields.io/badge/RL-Reward--Modeling-green) 
![Python](https://img.shields.io/badge/Python-3.10+-yellow)

## 📌 Project Overview
This project implements an **Agentic AI System** designed for high-level supply chain decision-making. Unlike standard chatbots, this system utilizes a **Reasoning-Action loop** where a Large Language Model (LLM) acts as a Strategic Manager, analyzing global crises and executing optimized logistics movements across an Indian supply chain network.

## 💼 Business Alignment (Supply Chain Focus)
The system is designed to overcome critical supply chain disruptions (e.g., port strikes, warehouse floods, demand spikes) by optimizing three key **KPIs**:
- **Operational Resilience:** Rapidly responding to unforeseen crises to minimize downtime.
- **Cost Minimization:** Calculating the most efficient transit routes in Indian Rupees (₹) to protect margins.
- **Risk Mitigation:** Preventing "stock-outs" and ensuring balanced inventory across regional hubs.

## 🛠️ Technical Architecture

### 1. The Agentic Workflow
The system employs a **Chain-of-Thought (CoT)** reasoning process. The agent observes the current state of the supply chain, reasons through the constraints, and outputs a structured **JSON command** for execution. This allows the AI to be integrated into a programmatic pipeline rather than just providing text.

### 2. Reward Modeling & Iteration (The RL Core)
To ensure the agent doesn't just provide "plausible" answers but "optimal" ones, I implemented a **Reward Modeling framework**. This allows the system to:
- **Quantitative Evaluation:** Grade decisions based on Cost, Effectiveness, and Risk.
- **Identify Reward Hacking:** I specifically simulated "flawed" reward functions to identify **shortcut behavior** (e.g., the agent choosing inaction to minimize cost).
- **Iterative Hardening:** Developed a "Hardened Reward Model" that penalizes inactivity and prioritizes crisis resolution over simple cost-saving.

### 3. Tech Stack
- **LLM:** Google Gemini (via Generative AI API)
- **State Management:** Custom Python Simulation Engine
- **Reasoning:** Structured JSON Output & Chain-of-Thought prompting
- **Evaluation:** Custom Reward Model for performance auditing
- **Frontend:** Streamlit for real-time interactive dashboarding

## 📈 Results & Audit
- **Convergence:** The agent successfully learned to navigate complex crises, moving from random suggestions to strategic pathfinding.
- **Efficiency:** Optimized routing reduced transit costs compared to baseline random moves.
- **Zero-Cheating:** Successfully eliminated "Reward Hacking" behavior through refined penalty signals.

## 🚀 How to Run
1. Clone the repo:
   ```bash
   git clone https://github.com/srushti41131/Strategic-Supply-Chain-Agent.git
2.Install dependencies:
pip install -r requirements.txt

3.Run the dashboard:
streamlit run app.py
