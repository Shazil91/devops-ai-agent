import os
import json
import psutil
from google import genai
import tools
import re


client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def get_metrics():
    return {
        "cpu": psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage('/').percent
    }


def ask_ai(metrics):
    prompt = f"""
You are an autonomous DevOps multi-action agent.

SYSTEM METRICS:
CPU: {metrics['cpu']}%
Memory: {metrics['memory']}%
Disk: {metrics['disk']}%

AVAILABLE ACTIONS:
- show_processes
- filter_high_cpu_process
- cleanup_temp_files
- log_alert

RULES:
- You can return MULTIPLE actions
- Always inspect processes before cleanup when system is unhealthy
- Prefer safety-first decisions

RETURN ONLY VALID JSON:

{{
  "status": "healthy/unhealthy",
  "reason": "...",
  "actions": [
    {{
      "action": "show_processes",
      "params": {{}}
    }},
    {{
      "action": "filter_high_cpu_process",
      "params": {{
        "threshold": 50
      }}
    }}
  ]
}}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


def clean_json_response(text):
    # Remove markdown wrappers if present
    text = re.sub(r"```json", "", text)
    text = re.sub(r"```", "", text)
    return text.strip()


def execute_actions(action_json):
    try:
        cleaned = clean_json_response(action_json)
        print("\n🧹 CLEANED JSON:\n", cleaned)

        data = json.loads(cleaned)

        actions = data.get("actions", [])

        results = []

        if not actions:
            return "No actions returned by AI"

        for step in actions:
            action = step.get("action")
            params = step.get("params", {})

            print(f"\n⚙️ EXECUTING: {action} | PARAMS: {params}")

            if action == "show_processes":
                result = tools.show_processes()

            elif action == "filter_high_cpu_process":
                threshold = params.get("threshold", 50)
                result = tools.filter_high_cpu_process(threshold)

            elif action == "cleanup_temp_files":
                result = tools.cleanup_temp_files()

            elif action == "log_alert":
                message = params.get("message", data.get("reason", "No reason"))
                result = tools.log_alert(message)

            else:
                result = f"Unknown action: {action}"

            results.append({
                "action": action,
                "result": result
            })

        return results

    except Exception as e:
        return f"Execution error: {str(e)}"

if __name__ == "__main__":
    metrics = get_metrics()

    print("\n📊 SYSTEM METRICS:\n", metrics)

    ai_response = ask_ai(metrics)
    print("\n🧠 AI RAW RESPONSE:\n", ai_response)

    result = execute_actions(ai_response)

    print("\n⚙️ EXECUTION RESULT:\n", result)