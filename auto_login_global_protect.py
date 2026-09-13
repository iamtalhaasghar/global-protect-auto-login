#!/home/programmer/.local/share/virtualenvs/global-protect-auto-login_iamfaizanrashid-hVSt9Kwu/bin/python
import pyautogui
import time, os
import subprocess

from dotenv import load_dotenv

data_dir = f'/mnt/data/projects/clones/global-protect-auto-login_iamfaizanrashid'
print(data_dir)
load_dotenv(f'{data_dir}/.env')

def open_globalprotect_vpn():
    '''open program'''
    try:
        server = os.getenv('SERVER')
        print('connecting to', server)

        subprocess.Popen(['/usr/bin/gpclient'])#, '--ignore-tls-errors', '--fix-openssl', 'connect', server])
        print("GlobalProtect VPN is now open.")
    except FileNotFoundError:
        print("GlobalProtect command not found. Please ensure GlobalProtect is installed.")


def find_element(img_path, do_click = False):
    pos = None
    while pos is None:
        try:
            print("waiting ", img_path, pos)
            pos = pyautogui.locateOnScreen(f'{data_dir}/{img_path}')
        except pyautogui.ImageNotFoundException:
            time.sleep(3) 

    if do_click:
        pyautogui.click(pos)
    return pos


open_globalprotect_vpn()
find_element("connect.png", True)
#find_element("next.png") <--- newer version
#pyautogui.write(os.getenv("USERNAME"))
#pyautogui.press("enter")
for i in range(1):
    find_element("login.png")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.write(os.getenv("PASSWORD"))
    pyautogui.press("enter")
#find_element("push.png", True)

