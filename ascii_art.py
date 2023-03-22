import tkinter as tk 
from art import *


window = tk.Tk() 
window.geometry("1200x800")
window.title("ASCII ART ")
window.grid_columnconfigure(0, weight=1)
global textwidget


def download_ascii():
    global textwidget
    if text_input.get():
        user_input = text_input.get()
        font = "block"  # Font di default
        if font_selection.get():  # Se è stato selezionato un font diverso da quello di default
            font = font_selection.get()
        chr_ignore = True  # Valore di default per chr_ignore
        if chr_ignore_selection.get() == "No":  # Se chr_ignore è stato selezionato come False
            chr_ignore = False
        color = "black"
        if color_selection.get():  # Se è stato selezionato un font diverso da quello di default
            color = color_selection.get()
        text_response = text2art(user_input, font=font, chr_ignore=chr_ignore)
    else:
        text_response = "Aggiungi una parola o una frase al campo input!"

    textwidget = tk.Text()
    textwidget.insert(tk.END, text_response)
    textwidget.grid(row=3, column=0, sticky="WE", padx=10, pady=10)
    textwidget.tag_config("color", foreground=color)
    textwidget.tag_add("color", "1.0", "end")
    credits_label = tk.Label(window, text="ASCII ART")
    credits_label.grid(row=8, column=0, sticky="S", pady=10)

def reset_window():
    global textwidget
    # Reimposta l'input dell'utente
    text_input.delete(0, tk.END)
    
    # Reimposta il testo del risultato
    textwidget.delete(1.0, tk.END)
   
    # Imposta textwidget come invisibile
    textwidget.grid_remove()
    color_selection.set("black")  # colore di default

 # Reimposta i crediti
   # credits_label.config(text="ascii art by Alessandro Castaldi")

    
    # Se vuoi reimpostare anche il valore di default delle opzioni di menu, rimuovi il commento dalle seguenti righe
    # font_selection.set("block")
    # chr_ignore_selection.set("Yes")

welcome_label = tk.Label(window,
                         text="Welcome! Aggiungi una parola o una frase da scaricare:",
                         font=("Helvetica", 15))
welcome_label.grid(row=0, column=0, sticky="N", padx=20, pady=10)                       

text_input = tk.Entry()
text_input.grid(row=1, column=0, sticky="WE", padx=10)


font_options = ["block", "bubble", "rounded", "cybermedium", "mini", "standard", "fancy", "script", "shadow", "slant"]
font_selection = tk.StringVar(window)
font_selection.set("block")  # Font di default
font_label = tk.Label(window,
                         text="Seleziona Font:",
                         font=("Helvetica", 15))
font_label.grid(row=3, column=0, sticky="W", padx=20, pady=10) 
font_menu = tk.OptionMenu(window, font_selection, *font_options)
font_menu.grid(row=3, column=0, sticky="E", padx=10, pady=10)

chr_ignore_selection = tk.StringVar(window)
chr_ignore_selection.set("Yes")  # Valore di default
chr_ignore_yes = tk.Radiobutton(window, text="Yes", variable=chr_ignore_selection, value="Yes")
chr_ignore_yes.grid(row=4, column=0, sticky="E", padx=10, pady=10)
chr_ignore_no = tk.Radiobutton(window, text="No", variable=chr_ignore_selection, value="No")
chr_ignore_no.grid(row=4, column=1, sticky="E", padx=10, pady=10)
chr_label = tk.Label(window,
                         text="Chr Ignore:",
                         font=("Helvetica", 15))
chr_label.grid(row=4, column=0, sticky="W", padx=20, pady=10) 

color_options = ["black","white","red","green","blue","yellow","orange","purple","pink","brown","gray","silver","gold"]
color_selection = tk.StringVar(window)
color_selection.set("black")  # Font di default
color_label = tk.Label(window,
                         text="Seleziona Colore Testo:",
                         font=("Helvetica", 15))
color_label.grid(row=5, column=0, sticky="W", padx=20, pady=10) 
color_menu = tk.OptionMenu(window, color_selection, *color_options)
color_menu.grid(row=5, column=0, sticky="E", padx=10, pady=10)

download_button = tk.Button(text=" ASCII ART", command=download_ascii)
download_button.grid(row=6, column=0, sticky="WE", pady=10, padx=10)
reset_button = tk.Button(text="RESET", command=reset_window)
reset_button.grid(row=7, column=0, sticky="WE", pady=10, padx=10)

if __name__ == "__main__":
    window.mainloop()


