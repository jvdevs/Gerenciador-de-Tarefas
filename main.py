import tkinter as tk
from tkinter import messagebox
import json

ARQUIVO_TAREFAS = "tarefas.json"


def carregar_tarefas():
    try:
        with open(ARQUIVO_TAREFAS, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def salvar_tarefas():
    with open(ARQUIVO_TAREFAS, "w") as f:
        json.dump(tarefas, f, indent=4)


def adicionar_tarefa():
    tarefa = entrada_tarefa.get()
    if tarefa:
        tarefas.append({"tarefa": tarefa, "concluida": False})
        salvar_tarefas()
        atualizar_lista()
        entrada_tarefa.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "Digite uma tarefa!")


