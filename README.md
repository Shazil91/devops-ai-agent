🚀 DevOps AI Agent (Multi-Action Autonomous System)

An AI-powered autonomous DevOps monitoring agent built using Python, psutil, and Google Gemini.
The system continuously analyzes system metrics and executes multi-step automated actions like process inspection, alerts, and cleanup simulation.

🧠 Features

✔ Real-time system monitoring (CPU, Memory, Disk)
✔ AI-driven decision making (Gemini 2.5 Flash)
✔ Multi-action execution pipeline
✔ Process inspection with CPU filtering
✔ Safe logging system
✔ Extensible tool-based architecture
✔ No destructive operations (safe by design)

⚙️ Architecture
System Metrics → AI Agent (Gemini) → Action Planner → Executor → Tools Layer
Flow:
Collect system metrics using psutil
Send metrics to AI (Gemini)
AI returns multiple actions
Executor runs actions sequentially
Tools module handles system operations safely
📦 Project Structure
devops-ai-agent/
│
├── agent.py          # Main AI agent logic (planner + executor)
├── tools.py          # System tools (process monitoring, logging)
├── alerts.log        # Generated alerts (auto-created)
└── README.md         # Project documentation
🧰 Available Tools
1. Show Processes

Displays top CPU-consuming processes.

show_processes(limit=5)
2. Filter High CPU Processes

Returns processes above a CPU threshold.

filter_high_cpu_process(threshold=50)
3. Cleanup Temp Files (Simulated)

Safe placeholder for cleanup logic.

cleanup_temp_files()
4. Log Alerts

Stores system alerts in a log file.

log_alert(message)
🤖 AI Behavior

The AI receives system metrics like:

CPU: 10%
Memory: 75%
Disk: 92%

It returns multi-step JSON actions:

{
  "status": "unhealthy",
  "reason": "High disk usage",
  "actions": [
    {
      "action": "show_processes",
      "params": {}
    },
    {
      "action": "filter_high_cpu_process",
      "params": {
        "threshold": 50
      }
    },
    {
      "action": "log_alert",
      "params": {
        "message": "System overloaded"
      }
    }
  ]
}
🔁 Execution Engine

The agent executes actions sequentially:

show_processes → list CPU-heavy processes
filter_high_cpu_process → filter by threshold
log_alert → save system warnings
cleanup_temp_files → simulated cleanup
🛡️ Safety Design

This system is intentionally safe:

✔ No process killing
✔ No file deletion
✔ Cleanup is simulated only
✔ Logging instead of destructive actions

🧪 Example Run
python agent.py
Output:
📊 SYSTEM METRICS:
CPU: 5.2
Memory: 70.1
Disk: 91.3

🧠 AI RESPONSE:
{ ... multi-action JSON ... }

⚙️ EXECUTING: show_processes
⚙️ EXECUTING: filter_high_cpu_process
⚙️ EXECUTING: log_alert

📦 FINAL RESULT:
[...]
🔧 Setup Instructions
1. Install dependencies
pip install psutil google-genai
2. Set API Key
Windows (PowerShell)
setx GEMINI_API_KEY "your_api_key_here"
Linux / Mac
export GEMINI_API_KEY="your_api_key_here"
3. Run the agent
python agent.py
🚀 Future Improvements
🔁 Continuous monitoring loop (daemon mode)
📊 FastAPI dashboard for live metrics
🧠 Memory system (history of alerts)
📦 Dockerized deployment
⚡ Real-time anomaly detection
🔔 Slack / email alert integration
🤖 Multi-agent collaboration system
💡 Use Cases
DevOps system monitoring
Server health automation
AI-based incident detection
Learning autonomous agents
Infrastructure observability experiments
👨‍💻 Author

Built by Shazil Ali
Exploring AI Agents, DevOps automation, and multi-agent systems.