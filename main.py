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


def concluir_tarefa():
    try:
        indice = lista_tarefas.curselection()[0]
        tarefas[indice]["concluida"] = not tarefas[indice]["concluida"]
        salvar_tarefas()
        atualizar_lista()
    except IndexError:
        messagebox.showwarning("Aviso", "Selecione uma tarefa!")


def remover_tarefa():
    try:
        indice = lista_tarefas.curselection()[0]
        del tarefas[indice]
        salvar_tarefas()
        atualizar_lista()
    except IndexError:
        messagebox.showwarning("Aviso", "Selecione uma tarefa!")


def atualizar_lista():
    lista_tarefas.delete(0, tk.END)
    for t in tarefas:
        status = "✅" if t["concluida"] else "❌"
        lista_tarefas.insert(tk.END, f"{status} {t['tarefa']}")


janela = tk.Tk()
janela.title("Gerenciador de Tarefas")
janela.geometry("400x400")


entrada_tarefa = tk.Entry(janela, width=40)
entrada_tarefa.pack(pady=10)


botao_adicionar = tk.Button(janela, text="Adicionar", command=adicionar_tarefa)
botao_adicionar.pack()

botao_concluir = tk.Button(janela, text="Concluir", command=concluir_tarefa)
botao_concluir.pack()

botao_remover = tk.Button(janela, text="Remover", command=remover_tarefa)
botao_remover.pack()


