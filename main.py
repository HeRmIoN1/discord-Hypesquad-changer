import time
import requests
import getpass
from colorama import Fore

token = getpass.getpass(prompt = f"Token: {Fore.RESET}")
choice = input(f"\n[1] Bravery\n[2] Briliance\n[3] Balance\nChoice: {Fore.RESET}")
headerpost = {
    'Authorization': token
}
payloadsosat = {
    'house_id': choice
}
time.sleep(1)
requests.session().post("https://discord.com/api/v8/hypesquad/online", json=payloadsosat, headers=headerpost)
print("Done")
#by hermione
