import tkinter as tk
from tkinter import Canvas, Button, Label
from PIL import Image, ImageDraw

# Variabile globale pentru desenare
last_x, last_y = None, None
color = "black"

# Funcție pentru a desena pe canvas
def draw(event):
    global last_x, last_y
    x, y = event.x, event.y
    canvas.create_line((last_x, last_y, x, y), fill=color, width=5)
    last_x, last_y = x, y

# Funcție pentru a reține ultimele coordonate ale mouse-ului
def start_draw(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y

# Funcție pentru a opri desenarea
def stop_draw(event):
    global last_x, last_y
    last_x, last_y = None, None

# Funcție pentru ghicirea desenului
# Funcție pentru ghicirea desenului
# Funcție pentru ghicirea desenului
# Funcție pentru ghicirea desenului
# Funcție pentru ghicirea desenului
def guess_drawing():
    # Obținem coordonatele desenului
    coords = canvas.coords("all")
    min_x = min(coords[::2])
    max_x = max(coords[::2])
    min_y = min(coords[1::2])
    max_y = max(coords[1::2])

    # Calculăm lungimea și lățimea desenului
    width = max_x - min_x
    height = max_y - min_y

    # Aici putem adăuga logica pentru a ghici desenul
    # Vom verifica raportul dintre lungime și lățime pentru a determina forma

    # Verificăm dacă desenul seamănă cu un cerc
    if abs(width - height) < 20 and min(width, height) > 50:
        label_result.config(text="Ai desenat un cerc!")

    # Verificăm dacă desenul seamănă cu un dreptunghi
    elif abs(width - height) < 10:
        label_result.config(text="Ai desenat un dreptunghi!")

    # Verificăm dacă desenul seamănă cu o linie
    elif width < 20 or height < 20:
        label_result.config(text="Ai desenat o linie!")

    # Dacă nu recunoaștem nicio formă specifică, afișăm un mesaj generic
    else:
        label_result.config(text="Nu pot ghici ce ai desenat!")

def clear_canvas():
    canvas.delete("all")
    label_result.config(text="")

# Crearea unei ferestre principale
root = tk.Tk()
root.title("Ghicește desenul")

# Crearea unui canvas pentru desenare
canvas = Canvas(root, width=200, height=200, bg='white')
canvas.pack()

# Legarea funcțiilor de desenare la evenimentele de mouse
canvas.bind("<B1-Motion>", draw)
canvas.bind("<Button-1>", start_draw)
canvas.bind("<ButtonRelease-1>", stop_draw)

# Crearea unui buton pentru curățarea canvasului
clear_button = Button(root, text="Curăță", command=clear_canvas)
clear_button.pack()

# Crearea unui buton pentru ghicirea desenului
guess_button = Button(root, text="Ghicește", command=guess_drawing)
guess_button.pack()

# Eticheta pentru afișarea rezultatului ghicirii
label_result = Label(root, text="")
label_result.pack()

# Rularea interfeței grafice
root.mainloop()
