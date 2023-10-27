import webbrowser
import time
import pandas as pd
import random
import pyautogui as pg
import numpy as np
import logging
import tempfile
import pywhatkit as pwt
import os

tmp = tempfile.gettempdir()
logging.basicConfig(level=logging.INFO,filename=f"{tmp}\\registro.log", format="%(asctime)s - %(message)s ")

print("Escolha uma das opções: \n1 - Iniciar Aquecimento \n3 - Iniciar Disparo \n2 - Configurar Caminho dos Navegadores")
#print("Escolha uma das opções: \n1 - Iniciar Aquecimento \n2 - Configurar Caminho dos Navegadores")
op = int(input("Selecione a Opção: "))


data = pd.read_csv("dados.CSV", sep=";", converters={0:str})
df = pd.DataFrame(data)
data_dict = data.to_dict('list')
leads = data_dict['WhatsApp']
df_leads = df[~df['WhatsApp'].isin(['', np.nan])]['WhatsApp'].dropna(ignore_index=True).astype(str)
msg = data_dict['msg']
cont_num = len(df_leads)
cont = 0


def search(file,path):
    for (root, dirs, files) in os.walk(path, topdown=True):
        #print(root)
        #print(dirs)
        #print(files)
        if file in files:
            return True
        else:
            return False

try:

    ##Config
    if op == 2:
        arquivo = open('path_navegadores.txt', 'r')
        chrome_path = arquivo.readline()
        brave_path = arquivo.readline()
        edge_path = arquivo.readline()
        opera_path = arquivo.readline()

        op = int(input("Iniciar o codigo?\n1 - Sim / 2 - Nao :  "))

        if op == 2:
            exit()

    else:
        ## PATH DOS NAVEGADORES
        chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
        brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s"
        edge_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s"
        opera_path = "C:/Users/Poupacred/AppData/Local/Programs/Opera/opera.exe %s"

    ##Aquecimento
    if op == 1:
        choice_is_equal = 10
        WIDTH, HEIGHT = pg.size()
        for m in msg:
            logging.info("INICIADO O PROGRAMA !!")

            navegadores = [chrome_path, brave_path, edge_path, opera_path]
            choice = random.randint(0,3)
            if choice_is_equal == choice:
                if choice == 0:
                    choice = choice + 1
                if choice == 3:
                    choice = choice - 1

            tp_envio = random.randint(1, 10)  # 30seg a 3min
            print(f"Tempo para envio de mensagem: {tp_envio} Segundos.")
            time.sleep(tp_envio)
            for c in range(cont_num):
                webbrowser.get(navegadores[choice]).open("https://web.whatsapp.com/send?phone=" + df_leads[c])
                print("ENVIANDO MENSAGEM...")
                time.sleep(10)
                pg.click(WIDTH / 2, HEIGHT / 2)
                pg.typewrite(df['msg'].sample(ignore_index=True)[0])
                pg.press('enter')
                time.sleep(4)
                pg.hotkey('ctrl','w')

            choice_is_equal = choice
            print("TODAS AS MENSAGENS FORAM ENVIADAS ENVIADAS!")
            print("-----------------")


    logging.info("FINALIZADO TODOS OS ENVIOS!")

    #Disparo
    if op == 3:
        image = input("Insira o nome da Imagem que será enviada ( Nome com a extensão do arquivo ): ")
        path = r"Imagens"
        file = image
        busca = search(file, path)
        print(busca)
        if image == False:
            print("vazio")
        else:
            for n in df_leads:
                print(n)
                pwt.sendwhats_image(f'+{n}',  f'{image}')
except Exception as e:
    print(e)
    logging.warning(f" Error: {e} ")
exit()
