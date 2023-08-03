#!/usr/bin/env python3

import json
import subprocess
from multiprocessing import Pool
from colorama import Fore, Style

# Load the services dictionary
with open('services_dictionary.json') as json_file:
    services_dictionary = json.load(json_file)

# Define the banner
def display_banner():
    banner = Fore.GREEN + r'''
     _________
    / ======= \
   / __________\
  | ___________ |
  | | -       | |
  | |         | |
  | |_________| |________________________
  \=____________/   ENUM BUDDY           )
  / """"""""""" \                       /
 / ::::::::::::: \                 br0-'
(_________________)

''' + Style.RESET_ALL
    print(banner)

# DEFINE NMAP TIPS 
def display_nmap_tips():
    nmap_tips = {
        '-sS': 'SYN scan - This is a stealthy scan method as it does not complete TCP connections.',
        '-sV': 'Version detection - This uses probes to determine the exact version of the service running on the port.',
        '-sC': 'Script scan - This runs a script to gather more information about the service.',
        '-sn': 'Ping scan - This scan simply checks if the hosts are online. No port scanning is performed.',
        '-O': 'OS detection - This attempts to detect the operating system on the host.',
        '-A': 'Aggressive scan - This enables OS detection, version detection, script scanning, and traceroute.'
    }
    print(f"\n{Fore.YELLOW}Nmap Command Tips:{Style.RESET_ALL}")
    for flag, description in nmap_tips.items():
        print(f"{flag}: {description}")

# Get user input for Nmap flag and target IP
def get_user_input():
    command = input("\nPlease enter your desired Nmap flag (FLAG ONLY) (or 'quit' to exit): ")
    if command.lower() == 'quit':
        return None, None
    target = input("\nPlease enter an IP or IP range to scan: ")
    return command, target

# Run the Nmap scan
def run_scan(args):
    target, command = args
    print(f"\n{Fore.YELLOW}Running command '{command}' on {target}.{Style.RESET_ALL}")

    # Split the command into a list of arguments
    args = ['nmap'] + command.split() + [target]

    # Run the scan as a subprocess
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = ''

    # Print the output in real-time
    for line in iter(process.stdout.readline, b''):
        line = line.decode('utf-8').strip()
        print(line)
        output += line + '\n'

    # Wait for the process to finish and get the exit code
    exit_code = process.wait()

    if exit_code != 0:
        print(f"{Fore.RED}Nmap scan failed with exit code {exit_code}.{Style.RESET_ALL}")
        return None

    return output

# Save scan results
def save_scan_results(results):
    if results:
        with open('scan_results.txt', 'w') as f:
            f.write(results)
        print(f"\n{Fore.GREEN}Scan results saved to scan_results.txt.{Style.RESET_ALL}")
    return

# Parse scan results and provide suggestions
def parse_scan_results(results):
    unrecognized_ports = {}
    if results:
        print(f"\n{Fore.YELLOW}Our Suggestions:{Style.RESET_ALL}")
        for line in results.splitlines():
            if "/tcp" in line or "/udp" in line:
                port = line.split('/')[0].strip()
                if port in services_dictionary:
                    for suggestion in services_dictionary[port]['suggestions']:
                        print(f"{port} - {suggestion}")
                else:
                    print(f"{Fore.RED}{port} not yet in our dictionary.{Style.RESET_ALL}")
                    unrecognized_ports[port] = get_user_suggestions(port)

        # Save unrecognized ports to new_services.json
        if unrecognized_ports:
            with open('new_services.json', 'w') as f:
                json.dump(unrecognized_ports, f, indent=4)
            print(f"\n{Fore.GREEN}Unrecognized ports saved to new_services.json.{Style.RESET_ALL}")

# Get user suggestions for unrecognized ports
def get_user_suggestions(port):
    print(f"\n{Fore.YELLOW}For the unrecognized port {port}, please provide a description and suggestions for enumeration.{Style.RESET_ALL}")
    description = input("\nPlease enter a description for this service: ")
    suggestions = input("\nPlease enter suggestions for this service (separated by ','): ").split(',')
    return {"description": description, "suggestions": [suggestion.strip() for suggestion in suggestions]}

# Main program
def main():
    display_banner()
    print(f"{Fore.CYAN}\nWelcome to Enum Buddy, your enumeration companion! This tool is designed to provide helpful suggestions for further investigation based on open ports. You can exit the tool at any time by typing 'quit'. Happy scanning!{Style.RESET_ALL}")

    while True:
        display_nmap_tips()
        command, target = get_user_input()
        if command is None:
            break
        results = run_scan((target, command))
        save_scan_results(results)
        parse_scan_results(results)

if __name__ == "__main__":
    main()
