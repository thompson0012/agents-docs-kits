import json
import time
import os
import subprocess

TIMEOUT_SECONDS = 900 # 15 minutes

def check_for_stale_sprints():
    current_time = int(time.time())
    
    # Check all local sprint folders
    harness_dir = ".harness/"
    if not os.path.exists(harness_dir):
        return
        
    for sprint in os.listdir(harness_dir):
        status_path = os.path.join(harness_dir, sprint, "status.json")
        if not os.path.exists(status_path):
            continue
            
        with open(status_path, "r") as f:
            status = json.load(f)
            
        # If the state claims to be active but the heartbeat is old
        if status["phase"] in ["in_progress", "in_review"]:
            last_heartbeat = status.get("last_updated_at", 0)
            
            if (current_time - last_heartbeat) > TIMEOUT_SECONDS:
                print(f"⚠️ Stale sprint detected: {sprint}. Initiating recovery...")
                recover_sprint(sprint, status)

def recover_sprint(sprint, status):
    # 1. Kill zombie processes
    kill_zombie_servers(sprint)
    
    # 2. Update the status file to trigger a clean resume
    status["phase"] = "paused_by_timeout"
    status["resume_from"] = determine_last_checkpoint(sprint)
    
    with open(f".harness/{sprint}/status.json", "w") as f:
        json.dump(status, f, indent=2)
        
    print(f"✅ {sprint} reset and ready for next agent to resume from {status['resume_from']}.")
