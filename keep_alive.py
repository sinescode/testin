from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Bot is running and alive!"

def run():
    # Run Flask server on port 10000
    app.run(host="0.0.0.0", port=10000)

def keep_alive():
    # Start Flask server in background thread
    t = Thread(target=run)
  # Daemon thread exits when program ends
    t.start()
  
