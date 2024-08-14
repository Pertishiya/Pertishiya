#### Restart Netprobe #####
import subprocess
import time
import os

def stop_process_by_name(process_name):
    try:
        result = subprocess.run(['taskkill','/f','/im',process_name],capture_output = True, text = True)
        if result.returncode == 0:
            print("Process stopped")
        else:
            print("Failed")
    except Exception as e:
        print("Error")

def start_process(exe_path):
    try:
        subprocess.Popen(exe_path)
        print("Process started")
    except Exception as e:
        print("Error")
        exit(1)