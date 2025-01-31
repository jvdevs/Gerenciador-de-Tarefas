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
