import tkinter as tk

def clicar_botao(valor):
    texto_atual = visor.get()
    novo_texto = texto_atual + valor
    visor.set(novo_texto)

def calcular():
    try:
        resultado = eval(visor.get())
        visor.set(resultado)
    except Exception as e:
        visor.set("Erro")

def limpar():
    visor.set("")

root = tk.Tk()
root.title("Calculadora")

visor = tk.StringVar()

visor_display = tk.Entry(root, textvariable=visor, font=('arial', 20, 'bold'), bd=10, insertwidth=4, width=14, justify='right')
visor_display.grid(row=0, column=0, columnspan=4)

botoes = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('LIMPAR', 5, 0, 4)
]

for (texto, linha, coluna, *opcoes) in botoes:
    if texto == 'LIMPAR':
        botao = tk.Button(root, text=texto, padx=20, pady=20, bg='#cbaacb', fg='black', command=limpar)
        botao.grid(row=linha, column=coluna, columnspan=4, sticky='nsew')
    elif texto == '=':
        botao = tk.Button(root, text=texto, padx=20, pady=20, bg='#f3b0c3', fg='black', command=calcular)
        botao.grid(row=linha, column=coluna, sticky='nsew')
    elif texto in ['+', '-', '*', '/', '.']:
        botao = tk.Button(root, text=texto, padx=20, pady=20, bg='#a3c2e0', fg='black', command=lambda t=texto: clicar_botao(t))
        botao.grid(row=linha, column=coluna, sticky='nsew')
    else:
        cor_fundo = '#ffffb5'
        cor_texto = 'black'
        botao = tk.Button(root, text=texto, padx=20, pady=20, bg=cor_fundo, fg=cor_texto, command=lambda t=texto: clicar_botao(t))
        botao.grid(row=linha, column=coluna, sticky='nsew')

for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
