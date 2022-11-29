import os
import sys

# Função responsável pela print inicial do menu
def menu():
    os.system('clear')
    print("  _____             _______             _             ")
    print(" |  __ \           |__   __|           | |            ")
    print(" | |__) |__ _  ___ ___| |_ __ __ _  ___| | _____ _ __ ")
    print(" |  _  // _` |/ __/ _ \ | '__/ _` |/ __| |/ / _ \ '__|")
    print(" | | \ \ (_| | (_|  __/ | | | (_| | (__|   <  __/ |   ")
    print(" |_|__\_\__,_|\___\___|_|_|  \__,_|\___|_|\_\___|_|   ")
    print("  / ____|                        | ____|____  |       ")
    print(" | |  __ _ __ _   _ _ __   ___   | |__     / /        ")
    print(" | | |_ | '__| | | | '_ \ / _ \  |___ \   / /         ")
    print(" | |__| | |  | |_| | |_) | (_) |  ___) | / /          ")
    print("  \_____|_|   \__,_| .__/ \___/  |____/ /_/           ")
    print("                   | |                                ")
    print("                   |_|                                ")
    print("                                                      ")
    print("                 BEM-VINDO                            ")
    print("                                                      ")
    
    
# Função responsável por printar para o file 
def printar_file(linha):
    original_stdout = sys.stdout
    with open('mapa.txt', 'a') as f:
        sys.stdout = f # Change the standard output to the file we created.
        print(linha)
        sys.stdout = original_stdout # Reset the standard output to its original value


# Função que printa o mapa para o terminal -> nao esta a ser usada
def print_matrix():
    file = open('text2.txt') 
    print(file.read())