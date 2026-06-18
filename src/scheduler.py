import schedule
import time
import subprocess
import os

def run_tasks():
    print("Running automated tasks...")
    # Get the directory of the current script to find other scripts
    src_dir = os.path.dirname(os.path.abspath(__file__))
    
    scripts = ["update_readme.py", "generate_stats.py", "changelog_generator.py"]
    
    for script in scripts:
        script_path = os.path.join(src_dir, script)
        print(f"Executing {script}...")
        subprocess.run(["python3", script_path], cwd=os.path.dirname(src_dir))
    
    # Optionally, you can add Git commands here to commit locally if you want.
    print("Tasks completed!")

def start_scheduler():
    print("Starting local scheduler. Tasks will run daily at 06:00...")
    # Schedule to run every day at 06:00
    schedule.every().day.at("06:00").do(run_tasks)
    
    # If you want to test it immediately, uncomment the line below:
    # run_tasks()

    while True:
        schedule.run_pending()
        time.sleep(60) # Wait a minute before checking the schedule again

if __name__ == "__main__":
    start_scheduler()
