import subprocess
import webbrowser
import threading

def run_msft_script():
    subprocess.run(['python', 'MSFT_UpToDate.py'])

def open_website():
    webbrowser.open('http://localhost:8000/FinalProject.html')

def start_server():
    subprocess.run(['python', '-m', 'http.server'])

# Start the MSFT script in a separate thread
msft_thread = threading.Thread(target=run_msft_script)
msft_thread.start()

# Start the server
start_server()

# Open the website
open_website()

