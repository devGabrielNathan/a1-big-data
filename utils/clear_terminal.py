import os

def clear_terminal():

    if os.name == 'nt':
        _ = os.system('cls')    # Limpa o terminal no Windows
    else:
        _ = os.system('clear')  # Limpa o terminal no Linux/macOS