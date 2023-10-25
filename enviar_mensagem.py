import webbrowser
import time
import pandas as pd
import random
import pyautogui as pg
import numpy as np
import logging

logging.basicConfig(level=logging.INFO,filename="registro.log", format="%(asctime)s - %(message)s ")

try:
    data = pd.read_csv("dados.CSV", sep=";")
    df = pd.DataFrame(data)
    data_dict = data.to_dict('list')
    leads = data_dict['WhatsApp']
    df_leads = df[~df['WhatsApp'].isin(['', np.nan])]['WhatsApp'].dropna(ignore_index=True)
    msg = data_dict['msg']
    cont_num = len(df_leads)
    sessao = 1
    cont = 0


    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s"
    edge_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s"
    opera_path = "C:/Users/Administrador/AppData/Local/Programs/Opera GX/opera.exe %s"
    #opera_path = "C:/Users/Poupacred/AppData/Local/Programs/Opera/opera.exe %s"

    for m in msg:
        logging.info("INICIADO O PROGRAMA !!")
        if sessao == 1:
            tp_envio = random.randint(1, 10)  # 30seg a 3min
            print(f"Tempo para envio de mensagem: {tp_envio} Segundos.")
            time.sleep(tp_envio)
            for c in range(cont_num):
                webbrowser.get(chrome_path).open("https://web.whatsapp.com/send?phone=" + df_leads[c] + "&text=" + df['msg'].sample(ignore_index=True)[0], 2 )
                print("ENVIANDO MENSAGEM PELO NAVEGADOR 1...")
                if c == 0:
                    time.sleep(15)
                    pg.doubleClick(1000,500)
                    pg.press('enter')
                    time.sleep(8)
                    pg.hotkey('ctrl','w')
                else:
                    time.sleep(10)
                    pg.doubleClick(1000,500)
                    pg.press('enter')
                    time.sleep(4)
                    pg.hotkey('ctrl','w')

            if cont_num > sessao:
                sessao = 2
            print("1º NUMERO -> MENSAGENS ENVIADAS!")
            print("-----------------")

        if sessao == 2:
            tp_envio = random.randint(1, 10)  # 30seg a 3min
            for b in range(cont_num):
                print(f"Tempo para envio de mensagem: {tp_envio} Segundos.")
                time.sleep(tp_envio)
                webbrowser.get(brave_path).open("https://web.whatsapp.com/send?phone=" + df_leads[b] + "&text=" + df['msg'].sample(ignore_index=True)[0])
                print("ENVIANDO MENSAGEM PELO NAVEGADOR 2...")
                pg.doubleClick(1000, 500)
                if b == 0:
                    time.sleep(15)
                    pg.doubleClick(1000, 500)
                    pg.press('enter')
                    time.sleep(6)
                    pg.hotkey('ctrl', 'w')
                else:
                    time.sleep(10)
                    pg.doubleClick(1000, 500)
                    pg.press('enter')
                    time.sleep(4)
                    pg.hotkey('ctrl', 'w')

            if cont_num > sessao:
                sessao = 3
            else :
                sessao = 1

            print("2º NUMERO -> MENSAGENS ENVIADAS!")
            print("-----------------")

        if sessao == 3:
            tp_envio = random.randint(1, 10)  # 30seg a 3min
            print(f"Tempo para envio de mensagem: {tp_envio} Segundos.")
            time.sleep(tp_envio)
            for e in range(cont_num):
                webbrowser.get(edge_path).open("https://web.whatsapp.com/send?phone=" + df_leads[e] + "&text=" + df['msg'].sample(ignore_index=True)[0])
                print("ENVIANDO MENSAGEM PELO NAVEGADOR 3...")
                pg.doubleClick(1000, 500)
                if e == 0:
                    time.sleep(15)
                    pg.doubleClick(1000, 500)
                    pg.press('enter')
                    time.sleep(6)
                    pg.hotkey('ctrl', 'w')
                else:
                    time.sleep(10)
                    pg.doubleClick(1000, 500)
                    pg.press('enter')
                    time.sleep(4)
                    pg.hotkey('ctrl', 'w')

            if cont_num > sessao:
                sessao = 4
            else:
                sessao = 1
            print("3º NUMERO -> MENSAGENS ENVIADAS!")
            print("-----------------")

        if sessao == 4:
            tp_envio = random.randint(1, 10)  # 30seg a 3min
            print(f"Tempo para envio de mensagem: {tp_envio} Segundos.")
            time.sleep(tp_envio)
            for o in range(cont_num):
                webbrowser.get(opera_path).open("https://web.whatsapp.com/send?phone=" + df_leads[o] + "&text=" + df['msg'].sample(ignore_index=True)[0])
                print("ENVIANDO MENSAGEM PELO NAVEGADOR 4...")
                pg.doubleClick(1000, 500)
                if o == 0:
                    time.sleep(15)
                    pg.doubleClick(1000, 500)
                    pg.press('enter')
                    time.sleep(6)
                    pg.hotkey('ctrl', 'w')
                else:
                    time.sleep(10)
                    pg.click(1000, 500)
                    pg.press('enter')
                    time.sleep(4)
                    pg.hotkey('ctrl', 'w')
            sessao = 1

            print("4º NUMERO -> MENSAGENS ENVIADAS!")
            print("-----------------")
    logging.info("FINALIZADO TODOS OS ENVIOS! ")
except Exception as e:
    print(e)
    logging.warning(f" Error: {e} ")
input("terminou !")
