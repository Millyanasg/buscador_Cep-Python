import requests
import json
from tkinter import *

# Função para buscar o CEP


def buscar_cep():
    cep = cep_entry.get()
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url)
    data = json.loads(response.content)
    if 'erro' not in data:
        logradouro = data['logradouro']
        bairro = data['bairro']
        cidade = data['localidade']
        estado = data['uf']
        resultado_label.config(
            text=f'Logradouro: {logradouro}\nBairro: {bairro}\nCidade: {cidade}\nEstado: {estado}')
    else:
        resultado_label.config(text='CEP não encontrado.')


# Configuração da interface gráfica
janela = Tk()
janela.geometry('300x250')
janela.title('Buscador de CEP')

titulo_label = Label(janela, text='Buscador de CEP', font=('Arial', 14))
titulo_label.pack(pady=10)

cep_entry = Entry(janela, width=30)
cep_entry.pack(pady=14)

buscar_button = Button(janela, text='Buscar', command=buscar_cep)
buscar_button.pack(pady=5)

resultado_label = Label(janela, text='')
resultado_label.pack(pady=10)

janela.mainloop()
