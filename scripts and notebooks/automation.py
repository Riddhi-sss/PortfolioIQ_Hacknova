import subprocess
import time
import os
import sys

def run_supervisor():
    # 1. Dynamically find the path to main_inference.py
    # Since automation.py is in 'scripts and notebooks', we stay in the current dir
    script_path = os.path.join(os.getcwd(), "main_inference.py")
    
    # 2. Use the same Python that is running this script (your hacknova_env)
    python_executable = sys.executable

    print(f"🚀 [Supervisor] Starting Quant Engine at: {time.ctime()}")
    
    while True:
        try:
            # Run main_inference.py as a subprocess
            process = subprocess.Popen([python_executable, script_path])
            
            # Wait for it to finish (or crash)
            process.wait()
            
            print(f"⚠️ [Supervisor] Engine stopped at {time.ctime()}. Restarting in 10s...")
            time.sleep(10)
            
        except KeyboardInterrupt:
            print("\n🛑 [Supervisor] Manual shutdown initiated. Exiting...")
            process.terminate()
            break
        except Exception as e:
            print(f"❌ [Supervisor] Fatal Error: {e}")
            time.sleep(30)

if __name__ == "__main__":
    run_supervisor()