import os
import time
import random
import pyautogui as pg
import webbrowser
import pywhatkit as pwt


def search(file, path):
    for (root, dirs, files) in os.walk(path, topdown=True):
        if file in files:
            return True
        else:
            return False


def aquecer(df, df_leads, cont_num, choice_is_equal, choice, chrome_path, brave_path, edge_path, opera_path, WIDTH, HEIGHT ):
    navegadores = [chrome_path, brave_path, edge_path, opera_path]
    tp_envio = random.randint(1, 10)  # 30seg a 3min
    print(f"Tempo para envio de mensagem: {tp_envio} Segundos.")
    time.sleep(tp_envio)
    if choice_is_equal == choice:
        if choice == 0:
            choice = choice + 1
        if choice == 3:
            choice = choice - 1

    for c in range(cont_num):
        webbrowser.get(navegadores[choice]).open("https://web.whatsapp.com/send?phone=" + df_leads[c])
        print("ENVIANDO MENSAGEM...")
        time.sleep(10)
        pg.click(WIDTH / 2, HEIGHT / 2)
        pg.typewrite(df['msg'].sample(ignore_index=True)[0])
        pg.press('enter')
        time.sleep(4)
        pg.hotkey('ctrl', 'w')
        return choice_is_equal