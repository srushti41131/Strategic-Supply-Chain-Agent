import google.generativeai as genai
import json
import random

class SupplyChainWorld:
    """
    The Global Simulation Engine - India Edition.
    Generates supply chain states and crises for the LLM Agent to solve.
    """
    def __init__(self):
        self.warehouses = {
            "Mumbai": {"inventory": 100, "capacity": 200, "status": "Operational"},
            "Delhi": {"inventory": 150, "capacity": 200, "status": "Operational"},
            "Bangalore": {"inventory": 80, "capacity": 200, "status": "Operational"},
            "Chennai": {"inventory": 120, "capacity": 200, "status": "Operational"}
        }
        self.transit_costs = {
            "Bangalore_to_Delhi": 12000,
            "Delhi_to_Mumbai": 8000,
            "Chennai_to_Mumbai": 10000,
            "Bangalore_to_Chennai": 5000
        }

    def generate_crisis(self):
        crises = [
            {"event": "Monsoon Flooding", "location": "Mumbai", "impact": "Major flooding. 40% inventory damaged.", "urgency": "High"},
            {"event": "Festival Demand Spike", "location": "Delhi", "impact": "Orders increased by 400%. Stockout imminent.", "urgency": "Critical"},
            {"event": "Transport Strike", "location": "Bangalore", "impact": "Trucking strike. Outbound shipments halted.", "urgency": "Medium"}
        ]
        return random.choice(crises)

    def get_current_state(self):
        full_state = {
            "warehouses": self.warehouses,
            "transit_costs": self.transit_costs,
            "currency": "INR (₹)"
        }
        return json.dumps(full_state, indent=2)

class SupplyChainAgent:
    """
    The LLM-powered Strategic Manager.
    """
    def __init__(self, api_key, world):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-3.8-flash')
        self.world = world

    def solve_crisis(self, crisis):
        state = self.world.get_//current_state()
        prompt = f"""
        You are the Strategic Logistics Manager of a major Indian supply chain.
        GOAL: Resolve the crisis while minimizing cost (INR ₹) and maximizing speed.
        CURRENT STATE: {state}
        CURRENT CRISIS: {crisis}
        Respond ONLY in JSON: {{"reasoning": "...", "action": "...", "estimated_cost": "...", "expected_impact": "..."}}
        """
        try:
            response = self.model.generate_content(prompt)
            text = response.text.replace('```json', '').replace('```', '').strip()
            return json.loads(text)
        except Exception as e:
            return {"error": str(e)}

class RewardModel:
    """
    The Critic.
    Evaluates the LLM's decisions and provides a numerical reward.
    """
    def __init__(self, world):
        self.world = world

    def evaluate_action(self, crisis, decision):
        if "error" in decision: return -100, "Invalid Action"
        reward = 0
        feedback = []
        if crisis['location'] in decision['action']:
            reward += 100
            feedback.append("✅ Crisis location addressed.")
        else:
            reward -= 100
            feedback.append("❌ Failed to address location.")
        
        try:
            cost_str = decision['estimated_cost'].replace('₹', '').replace(',', '').strip()
            cost = float(''.join(filter(str.isdigit, cost_str)))
            if cost <= 15000: reward += 50; feedback.append("✅ Cost-effective.")
            else: reward -= 50; feedback.append("❌ Too expensive.")
        except:
            reward -= 20; feedback.append("⚠️ Cost verification failed.")
        return reward, " | ".join(feedback)
