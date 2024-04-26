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

# Function to print colored text
def print_colored_text(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")  # \033[0m resets the color

# Function to print large banner
def print_banner(text, color_code):
    print_colored_text('''
 m    m                 m             m""                  mmm m     m  mmmm 
 ##  ## m   m   mmm   mm#mm   mmm   mm#mm   mmm          m"   " "m m"  #"   "
 # ## # #   #  #   "    #    "   #    #    "   #         #       "#"   "#mmm 
 # "" # #   #   """m    #    m"""#    #    m"""#   """   #        #        "#
 #    # "mm"#  "mmm"    "mm  "mm"#    #    "mm"#          "mmm"   #    "mmm#"

'''.format(text), color_code)

# Color codes for banners
color_codes = {
    "HEADER": "95",
    "OKBLUE": "94",
    "OKGREEN": "92",
    "WARNING": "93",
    "FAIL": "91"
}

# Displaying the banner
print_banner("BlackArch-MFBK", color_codes["HEADER"])
host_to_ping = input("Enter The host: ")
try:
    while True:
        ping_result = ping_host(host_to_ping)
        if "received" in ping_result:
            print_colored_text("Ping is successful!", color_codes["OKGREEN"])
        else:
            print_colored_text("Ping request failed.", color_codes["FAIL"])
        time.sleep(1)  # Wait for 1 second before the next ping
except KeyboardInterrupt:
    print("\nPing stopped by user.")
