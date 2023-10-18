import webbrowser
import subprocess
import time
import pandas as pd
import random
import pyautogui as pg

data = pd.read_csv("dados.CSV", sep=";")
data_dict = data.to_dict('list')
leads = data_dict['WhatsApp']
msg = data_dict['msg']
combo = list(zip(leads, msg))
first = True

chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s"

for leads, msg in combo:
    tp_envio = random.randint(30, 180)  # 30seg a 3min
    print(f"Tempo para envio de mensagem: {tp_envio} Segundos.")
    time.sleep(tp_envio)

    if first:
        webbrowser.get(chrome_path).open("https://web.whatsapp.com/send?phone=" + leads + "&text=" + msg)
        print("ENVIANDO MENSAGEM PELO NAVEGADOR 1...")
        time.sleep(30)
        pg.press('enter')
        time.sleep(5)
        pg.hotkey('ctrl','w')
        #subprocess.call("TASKKILL /F /IM chrome.exe")  # Fechando o Chrome
        first = False
    else:
        webbrowser.get(brave_path).open("https://web.whatsapp.com/send?phone=" + leads + "&text=" + msg)
        print("ENVIANDO MENSAGEM PELO NAVEGADOR 2...")
        time.sleep(30)
        pg.press('enter')
        time.sleep(5)
        pg.hotkey('ctrl','w')
        #subprocess.call("TASKKILL /F /IM brave.exe")  # Fechando o brave
        first = True

    print("MENSAGEM ENVIADA!")
    print("-----------------")
