import PySimpleGUI as sg

default_theme = 'DefaultNoMoreNagging'
def janela_menu():
    sg.theme(default_theme)
    columns_menu_center = [
                           [sg.Text('Bem-Vindo!', font=("Arial", 32), text_color="White", background_color="red", justification='center')],
                            [sg.Text('Selecione os Navegadores e inicie o Aquecimento.', font=("Arial", 14),justification='center')],
                            [sg.Image('logo.png',key='-IMAGE-',size=(200,200), expand_x=True, expand_y=True)],
                           ]
    columns_right= [
        [sg.Text('Quais Navegadores vão ser usados?', font=("Arial", 12), justification='center')],
        [sg.Checkbox('Chrome', key='chrome_check', enable_events=True,  font=("Arial", 10)),
        sg.Checkbox('Edge', key='edge_check', enable_events=True,  font=("Arial", 10)),
        sg.Checkbox('Brave', key='brave_check', enable_events=True, font=("Arial", 10)),
        sg.Checkbox('Opera', key='opera_check', enable_events=True, font=("Arial", 10))],
        # [sg.Checkbox('Caminho dos navegadores definidos manualmente.', key='path_check', enable_events=True, font=("Arial", 12))],
        [sg.Button('Iniciar Aquecimento', font=("Arial", 12),size=(30,1), border_width=0)],
        [sg.Button('Iniciar Disparo', font=("Arial", 12),size=(30,1),border_width=0)],
        [sg.Button('Configurações', font=("Arial", 12),size=(30,1),border_width=0)],

    ]
    layout = [[sg.VPush(),sg.Column(columns_menu_center), sg.VSeparator( color='white'), sg.Column(columns_right),sg.VPush()]]
    return sg.Window('PoupaZap - 2.0.0', layout, icon='icone.ico', size=(800, 400), finalize=True)


def janela_aquecer():
    sg.theme(default_theme)
    layout_center_aquecer = [ [sg.Text('',key='loading-frase', font=("Arial", 22), size=(40,1))],
        [sg.ProgressBar(100, orientation='h', size=(100,20), border_width=4, key='-PROGRESS-BAR-', bar_color=('darkblue','white'))],
        [
        sg.Button('SAIR', font=("Arial", 12), size=(20, 1), button_color="red", border_width=0),
        sg.Button('COMEÇAR', font=("Arial", 12), size=(20, 1), border_width=0)]
        ]
    layout2 = [[sg.Column(layout_center_aquecer), sg.VPush()]]
    return sg.Window('PoupaZap - 2.0.0', layout=layout2, icon='icone.ico', size=(600, 200), finalize=True)


def janela_disparar():
    sg.theme(default_theme)
    layout_center_disparar = [[sg.Button('SAIR', font=("Arial", 16), size=(20, 1), button_color="red")],
               [sg.Button('COMEÇAR', font=("Arial", 16), size=(40, 1), button_color="green")]]
    layout3 = [[sg.VPush(), sg.Column(layout_center_disparar, element_justification='c'), sg.VPush()]]
    return sg.Window('PoupaZap - 2.0.0', layout3, icon='icone.ico', size=(600, 600), finalize=True)


def janela_config():
    sg.theme(default_theme)
    layout_center_config = [
        [sg.Text('Configurações', font=("Arial", 20))],
        [sg.Text('', font=("Arial", 20))],
        [sg.Button('Personalizar', size=(20,2)), sg.Button('Como Funciona',size=(20,2)), sg.Button('Voltar',size=(20,2))]
    ]
    layout3 = [[sg.Column(layout_center_config,pad=(100,20))]]
    return sg.Window('PoupaZap - 2.0.0', layout3, icon='icone.ico', size=(800, 400), finalize=True)


def custom_program():
    sg.theme(default_theme)
    layout_custom = [
        [sg.Text('Logo:')],
        [sg.InputText(key="-LOGO-",size=(70,3)),
        sg.FileBrowse('Buscar',file_types=[("*.png *.jpg")],size=(10,2))],
        [
        sg.Exit('Sair',size=(20,2),button_color='red'),
        sg.Button('Salvar', size=(20,2))
         ]
    ]
    layoutC = [[sg.VPush(), sg.Column(layout_custom),sg.VPush()]]
    return sg.Window('PoupaZap - 2.0.0', layoutC, icon='icone.ico', size=(600,200), finalize=True)