import psutil
import time


def show_processes(limit=5):
    processes = []

    # Initialize CPU measurement
    for p in psutil.process_iter():
        try:
            p.cpu_percent(interval=None)
        except:
            pass

    time.sleep(1)

    for p in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        try:
            processes.append(p.info)
        except:
            pass

    sorted_procs = sorted(processes, key=lambda x: x['cpu_percent'], reverse=True)

    return sorted_procs[:limit] if sorted_procs else "No processes found"


def filter_high_cpu_process(threshold=50):
    high_cpu = []

    print(f"🔍 Filtering processes > {threshold}% CPU")

    # Initialize CPU measurement
    for p in psutil.process_iter():
        try:
            p.cpu_percent(interval=None)
        except:
            pass

    time.sleep(1)

    for p in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        try:
            if p.info['cpu_percent'] > threshold:
                high_cpu.append(p.info)
        except:
            pass

    return high_cpu if high_cpu else "No high CPU processes found"
# def kill_high_cpu_process(threshold=50):
#     killed = []

#     for p in psutil.process_iter(['pid', 'cpu_percent', 'name']):
#         try:
#             if p.info['cpu_percent'] > threshold:
#                 pid = p.info['pid']

#                 if platform.system() == "Windows":
#                     os.kill(pid, signal.SIGTERM)
#                 else:
#                     os.kill(pid, signal.SIGKILL)

#                 killed.append(p.info)

#         except:
#             pass

#     return killed



def cleanup_temp_files():
    # SAFE VERSION
    return "Cleanup simulated (no files deleted yet)"


def log_alert(message):
    with open("alerts.log", "a") as f:
        f.write(message + "\n")

    return "Alert logged"