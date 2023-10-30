import random
import time

import pandas as pd
import pyautogui as pg
import numpy as np
import logging
import tempfile
import pywhatkit as pwt
import funcoes as fn
import PySimpleGUI as sg
import windows as win

tmp = tempfile.gettempdir()
logging.basicConfig(level=logging.INFO, filename=f"{tmp}\\registro.log", format="%(asctime)s - %(message)s ")
data = pd.read_csv("dados.CSV", sep=";", converters={0: str})
df = pd.DataFrame(data)
data_dict = data.to_dict('list')
leads = data_dict['WhatsApp']
df_leads = df[~df['WhatsApp'].isin(['', np.nan])]['WhatsApp'].dropna(ignore_index=True).astype(str)
msg = data_dict['msg']
cont_num = len(df_leads)
cont = 0

chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s"
edge_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s"
opera_path = "C:/Users/Poupacred/AppData/Local/Programs/Opera/opera.exe %s"

janela1, janela2 = win.janela_menu(), None
janela3, janela4 = None, None

while True:
    window, event, values = sg.read_all_windows()

    if window == janela1 and event == sg.WINDOW_CLOSED:
        break
    if window == janela1 and event == 'Iniciar Aquecimento':
        janela2 = win.janela_aquecer()
        janela1.hide()
        terminou = False
        choice_is_equal = 10
        WIDTH, HEIGHT = pg.size()
        if not terminou:
            for m in msg:
                print(m)
                choice = random.randint(0, 3)
                logging.info("INICIADO O PROGRAMA !!")
                retorno_choice = fn.aquecer(df, df_leads, cont_num, choice_is_equal, choice, chrome_path, brave_path,
                                            edge_path, opera_path, WIDTH, HEIGHT)
                choice_is_equal = retorno_choice
                print("TODAS AS MENSAGENS FORAM ENVIADAS ENVIADAS!")
                print("-----------------")
                terminou = True
        if terminou:
            janela2.hide()
            janela1.un_hide()
        logging.info("FINALIZADO TODOS OS ENVIOS!")

    if window == janela2 and event == 'SAIR':
        janela2.hide()
        janela1.un_hide()
    if window == janela1 and event == 'Iniciar Disparo':
        janela3 = win.janela_aquecer()
        janela1.hide()
        image = input("Insira o nome da Imagem que será enviada ( Nome com a extensão do arquivo ): ")
        path = r"Imagens"
        file = image
        busca = fn.search(file, path)
        print(busca)
        if not image:
            print("vazio")
        else:
            for n in df_leads:
                print(n)
                pwt.sendwhats_image(f'+{n}', f'{image}')

    if window == janela3 and event == 'SAIR':
        janela3.hide()
        janela1.un_hide()

    if window == janela1 and event == 'Configurações':
        janela4 = win.janela_config()
        janela1.hide()
        arquivo = open('path_navegadores.txt', 'r')
        chrome_path = arquivo.readline()
        brave_path = arquivo.readline()
        edge_path = arquivo.readline()
        opera_path = arquivo.readline()

        op = int(input("Iniciar o codigo?\n1 - Sim / 2 - Nao :  "))

        if op == 2:
            exit()
    if window == janela4 and event == 'SAIR':
        janela4.hide()
        janela1.un_hide()
exit()
