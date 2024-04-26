import subprocess
import time

def ping_host(host):
    # Use the ping command with subprocess
    result = subprocess.run(['ping', '-c', '1', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Check if ping was successful
    if result.returncode == 0:
        # Extracting relevant information from the output
        output_lines = result.stdout.splitlines()
        reply_line = output_lines[-2]  # Assuming the reply is always second from the last line
        return reply_line.strip()
    else:
        return "Ping request failed."

# Example usage:

host_to_ping =input("Enter The host :")

try:
    while True:
        ping_result = ping_host(host_to_ping)
        print(ping_result)
        time.sleep(1)  # Wait for 1 second before the next ping
except KeyboardInterrupt:
    print("\nPing stopped by user.")
