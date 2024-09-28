#!/usr/bin/env python3
import os
import time
import shutil
import socket
from colorama import Fore, Style, init

# Initialize colorama
init()

def clear_console(except_art=False):
    if not except_art:
        os.system('clear')  # Clear the console

def center_text(text):
    # Get terminal width
    terminal_width = shutil.get_terminal_size().columns
    # Split text into lines and center each line
    centered_lines = [line.center(terminal_width) for line in text.strip().split('\n')]
    # Join centered lines with new line characters
    return "\n".join(centered_lines)

def print_centered(text):
    print(center_text(text))

def dummy_ddos_function():
    clear_console()
    ddos_art = """
┳┓┳┓  ┏┓  ┏┓┏┳┓┏┳┓┏┓┏┓┓┏┓
┃┃┃┃┏┓┗┓  ┣┫ ┃  ┃ ┣┫┃ ┃┫ 
┻┛┻┛┗┛┗┛  ┛┗ ┻  ┻ ┛┗┗┛┛┗┛
                         

created by iamgeo1
    """
    print(Fore.GREEN + ddos_art + Style.RESET_ALL)
    print(Fore.RED + "This is a DDoS simulation. hping3 is not supported in iSH." + Style.RESET_ALL)
    target_ip = input(Fore.RED + "Target IP: ")
    duration = int(input(Fore.YELLOW + "Duration in seconds: "))

    print("Simulating DDoS attack...")
    time.sleep(duration)
    print("DDoS simulation finished.")
    wait_for_user()

def port_scanner():
    clear_console()
    port_scanner_art = """
┏┓┏┓┳┓┏┳┓  ┏┓┏┓┏┓┳┓┳┓┏┓┳┓
┃┃┃┃┣┫ ┃   ┗┓┃ ┣┫┃┃┃┃┣ ┣┫
┣┛┗┛┛┗ ┻   ┗┛┗┛┛┗┛┗┛┗┗┛┛┗
created by iamgeo1
    """
    print(Fore.GREEN + port_scanner_art + Style.RESET_ALL)
    print(Fore.LIGHTGREEN_EX + "Port Scanner" + Style.RESET_ALL)
    
    target_ip = input(Fore.RED + "Target IP: ")
    start_port = int(input(Fore.YELLOW + "Start Port: "))
    end_port = int(input(Fore.YELLOW + "End Port: "))

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target_ip, port))
        
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
        
        sock.close()

    wait_for_user()

def wait_for_user():
    """Waits for the user to input 'exit' or press Enter to return to the menu."""
    while True:
        user_input = input(Fore.YELLOW + "Type 'exit' to close the application or press Enter to return to the menu: ")
        if user_input.lower() == 'exit':
            print("Exiting the application.")
            exit(0)
        elif user_input == "":
            return  # Just return to the main menu

def dummy_run_maskphish():
    clear_console()
    print(Fore.GREEN + "MaskPhish isn't available in iSH. This is a simulation." + Style.RESET_ALL)
    wait_for_user()

def dummy_run_phishing_links():
    clear_console()
    print(Fore.GREEN + "Zphisher isn't available in iSH. This is a simulation." + Style.RESET_ALL)
    wait_for_user()

def dummy_run_cam_links():
    clear_console()
    print(Fore.GREEN + "CamPhish isn't available in iSH. This is a simulation." + Style.RESET_ALL)
    wait_for_user()

def main_menu():
    while True:
        clear_console()  # Clear the console at the start of the menu

        # Hardcoded ASCII art and menu options
        menu_text = Fore.GREEN + """
┳┳┓┏┓┏┓┏┓┏┓  ┏┓┓ ┳┏┓┳┓┏┳┓
┃┃┃┏┛┏┛┏┛┃┃  ┃ ┃ ┃┣ ┃┃ ┃ 
┛ ┗┗┛┗┛┗┛┗┻  ┗┛┗┛┻┗┛┛┗ ┻ 
created by mdalam-4986

Main Menu
1. DDoS (Simulation)
2. Link Masker (Simulation)
3. Phishing Links (Simulation)
4. Cam Links (Simulation)
5. Port Scanner
6. Exit
Select an option (1-6):
""" + Style.RESET_ALL
        
        print(center_text(menu_text))  # Print the centered menu
        choice = input().strip()
        
        if choice == '1':
            dummy_ddos_function()
        elif choice == '2':
            dummy_run_maskphish()
        elif choice == '3':
            dummy_run_phishing_links()
        elif choice == '4':
            dummy_run_cam_links()
        elif choice == '5':
            port_scanner()
        elif choice == '6':
            print("Exiting the application.")
            break  # Exit the application
        else:
            print("Invalid choice, please select a valid option.")

if __name__ == "__main__":
    main_menu()
