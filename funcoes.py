import os
import time
import random
import pyautogui as pg
import webbrowser
import PySimpleGUI as sg
from PIL import Image

def search(file, path):
    for (root, dirs, files) in os.walk(path, topdown=True):
        if file in files:
            return True
        else:
            return False


def aquecer(df, df_leads, cont_num, chrome_path, brave_path, edge_path, opera_path, WIDTH, HEIGHT ):
    nav = [chrome_path, brave_path, edge_path, opera_path]
    nn = 0
    navegadores = []
    tp_envio = random.randint(10, 15)

    print(f"Tempo para envio de mensagem: {tp_envio} Segundos.")
    # time.sleep(tp_envio)
    for n in range(len(nav)):
        print(nav[n])
        if nav[n] != '':
            navegadores.append(nav[n])
            nn += 1
    max_nav = len(navegadores) - 1
    choice = random.randint(0, max_nav)
    choice_is_equal = 0
    if max_nav > 0:
        if choice_is_equal == choice:
            if choice <= 1:
                choice = choice + 1
            if choice > 1:
                choice = choice - 1


    for c in range(cont_num):
        ms = df_leads[c]
        webbrowser.get(navegadores[choice]).open("https://web.whatsapp.com/send?phone=" + ms)
        print("ENVIANDO MENSAGEM...")
        time.sleep(5 + tp_envio)
        pg.click(WIDTH / 2, HEIGHT / 2)
        pg.typewrite(df['msg'].sample(ignore_index=True)[0])
        time.sleep(5)
        pg.press('enter')
        time.sleep(2)
        pg.hotkey('ctrl', 'w')
        choice_is_equal = choice

def salvarImagens(logo):
    if logo not in [None, '']:
        file_logo = Image.open(logo)
        file_logo.save('logo.png')
