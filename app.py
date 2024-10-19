from flask import Flask
import os
import time
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get system username
    system_username = os.getenv('USER')
    
    # Get server time in IST
    server_time_ist = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(time.time() + 5.5 * 3600))
    
    # Get 'top' command output
    top_output = subprocess.getoutput('top -b -n1')
    
    # Create HTML response
    return f"""
    <h1>System Info</h1>
    <p><strong>Name:</strong> Your Full Name</p>
    <p><strong>Username:</strong> {system_username}</p>
    <p><strong>Server Time (IST):</strong> {server_time_ist}</p>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
