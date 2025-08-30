import tkinter as tk
from tkinter import PhotoImage

# Função que será chamada quando o botão for pressionado
def mostrar_imagem():
    # Cria o label com a imagem e exibe na janela
    imagem = PhotoImage(file="download.jpg")  # Altere para o caminho da sua imagem
    label_imagem.config(image=imagem)
    label_imagem.image = imagem  # Necessário para evitar que a imagem desapareça

# Cria a janela principal
janela = tk.Tk()
janela.title("Exemplo de Imagem com Tkinter")
janela.geometry("600x600")
# Cria um botão que chama a função mostrar_imagem ao ser pressionado
botao = tk.Button(janela, text="clique", command=mostrar_imagem)
botao.pack()

# Cria um label vazio que será preenchido com a imagem
label_imagem = tk.Label(janela)
label_imagem.pack()

# Inicia o loop da interface gráfica
janela.mainloop()