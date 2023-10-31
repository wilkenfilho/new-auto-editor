## Feito pelo Wilken Perez##
## Acredito que seja necessário a instalação do auto-editor##
# Nesse caso, utilize o comando no CMD pip install auto-editor e o comando pip install tk


import tkinter as tk
from tkinter import filedialog
import sys
import os
import subprocess


old_string = '""'

new_string = old_string.replace('"', "")


def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def main():
    # Cria uma janela do Tkinter
    root = tk.Tk()
    root.title("Removedor de silêncio")
    root.geometry(f"{500}x{300}")
    root.resizable(False, False)

    # Cria um botão para selecionar o arquivo
    button_selecionar = tk.Button(
        root, text="1º Selecionar arquivo", command=selecionar_arquivo
    )
    button_selecionar.grid(row=0, column=0, sticky="W" + "E")
    # Cria um label para mostrar o caminho do arquivo
    label_arquivo = tk.Label(root, text="O arquivo deve ser MP4")
    label_arquivo.grid(row=1, column=0, sticky="W")

    # Cria um botão para exportar o arquivo
    button_exportar = tk.Button(
        root, text="2º Selecionar a pasta para exportar", command=exportar
    )
    button_exportar.grid(row=2, column=0, sticky="W" + "E")
    # Cria um label para mostrar o caminho do exportar
    label_exportar = tk.Label(
        root, text="Escolha a pasta para exportar o arquivo, pode ser qualquer uma"
    )
    label_exportar.grid(row=3, column=0, sticky="W")

    # Cria um botão para rodar o script
    button_run = tk.Button(
        root,
        text="Tirar silêncio e exportar para Adobe Premiere ou Sony Vegas",
        command=rodar,
    )
    button_run.grid(row=4, column=0, sticky="W" + "E")

    # Cria um botão para rodar o script bruto
    button_run = tk.Button(root, text="Tirar silêncio e exportar bruto", command=bruto)
    button_run.grid(row=6, column=0, sticky="W" + "E")

    # Cria um botão para rodar o script Da vinci
    button_run = tk.Button(
        root, text="Tirar silêncio e exportar para DaVinci Resolve", command=vinci
    )
    button_run.grid(row=5, column=0, sticky="W" + "E")

    # Cria um label para mostrar o caminho do arquivo
    label_arquivo = tk.Label(root, text="Criado e desenvolvido por @wilkenfilho")
    label_arquivo.grid(row=7, column=0, sticky="W")

    # Inicia o loop principal do Tkinter
    root.mainloop()


def selecionar_arquivo():
    # Abre uma caixa de diálogo para selecionar o arquivo
    filename = filedialog.askopenfilename(filetypes=[("Arquivos MP4", "*.mp4")])

    # Verifica se o arquivo é válido
    if not filename.endswith(".mp4"):
        print("O arquivo deve ter a extensão .mp4")
        return

    tk.messagebox.showinfo("Parabuains", "Arquivo selecionado!")

    # Armazena o caminho do arquivo
    global caminho_arquivo
    caminho_arquivo = filename


def exportar():
    # Verifica se o caminho do arquivo está definido
    if caminho_arquivo is None:
        print("Selecione um arquivo primeiro")
        # Exibe uma caixa de aviso
        tk.messagebox.showinfo("Aviso", "Selecione um arquivo primeiro")
        return

    # Exibe um prompt para solicitar o destino de exportação
    folder_path = filedialog.askdirectory()
    tk.messagebox.showinfo("Parabuains", "Pasta selecionada!")

    # Realiza a exportação


def rodar():
    if caminho_arquivo is None:
        print("selecione o arquivo")
        return

    subprocess.run(
        ["auto-editor", caminho_arquivo, "--export", "premiere", "--margin", "0.1sec"],
        shell=False,
    )
    tk.messagebox.showinfo(
        "Parabéns", "Exportação para o Premiere ou Sony Vegas concluída"
    )


def bruto():
    if caminho_arquivo is None:
        print("selecione o arquivo")
        return

    subprocess.run(["auto-editor", caminho_arquivo])
    tk.messagebox.showinfo("Parabéns", "Exportação concluída")


def vinci():
    if caminho_arquivo is None:
        print("selecione o arquivo")
        return

    subprocess.run(["auto-editor", caminho_arquivo, "--export", "resolve"])
    tk.messagebox.showinfo("Parabéns", "Exportação concluída")


if __name__ == "__main__":
    main()
