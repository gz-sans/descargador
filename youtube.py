import sys
from pytube import YouTube
from tkinter import *
from tkinter import ttk, messagebox
import os

def obtener_ruta_destino():
    # Obtener la ruta del script o del ejecutable en ejecución
    if getattr(sys, 'frozen', False):
        # Cuando se ejecuta como un ejecutable con PyInstaller
        return os.path.dirname(sys.executable)
    else:
        # Cuando se ejecuta como script en el entorno de desarrollo
        return os.path.dirname(os.path.abspath(__file__))

def descargar_video():
    enlace = url_entry.get()

    try:
        video = YouTube(enlace)
        descarga = video.streams.get_highest_resolution()

        # Carpeta de destino (en este caso, la carpeta "Descargas" en el mismo directorio)
        carpeta_destino = os.path.join(obtener_ruta_destino(), "Descargas")

        # Verificar si la carpeta de destino existe, si no, crearla
        if not os.path.exists(carpeta_destino):
            os.makedirs(carpeta_destino)

        # Descargar el video en la carpeta de destino
        descarga.download(output_path=carpeta_destino)

        messagebox.showinfo("Éxito", f"Descarga completada correctamente en la carpeta '{carpeta_destino}'.")
    except Exception as e:
        messagebox.showerror("Error", f"Hubo un error: {str(e)}")

# Resto del código permanece igual

def mostrar_sobre_mi():
    messagebox.showinfo("Sobre mí", "Visita mi canal de YouTube: https://www.youtube.com")

# Creación de la ventana del programa
root = Tk()
root.title("Descargador de YouTube")
root.geometry("600x250")
root.config(bg="#f0f0f0")

# ignora esta imagen
"""
imagen = PhotoImage(file="you.png")
foto_label = Label(root, image=imagen, bg="#f0f0f0")
foto_label.grid(row=0, column=0, padx=20, pady=(10, 10), rowspan=5)
"""
# Título
titulo_label = Label(root, text="Descargador de YouTube", font=("Helvetica", 16), bg="#f0f0f0")
titulo_label.grid(row=0, column=1, columnspan=2, pady=(10, 20))

# Menú
menubar = Menu(root)
root.config(menu=menubar)

file_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Archivo", menu=file_menu)
file_menu.add_command(label="Salir", command=root.destroy)

help_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Ayuda", menu=help_menu)
help_menu.add_command(label="Sobre mí", command=mostrar_sobre_mi)

# Etiqueta de instrucciones
instrucciones_label = Label(root, text="Ingresa el enlace del video de YouTube:", bg="#f0f0f0")
instrucciones_label.grid(row=1, column=1, columnspan=2, pady=(10, 5), sticky="w")

# Entrada de URL
url_entry = Entry(root, width=30)
url_entry.grid(row=2, column=1, columnspan=2, pady=(0, 10), sticky="w")

# Botón de descarga
descargar_button = Button(root, text="Descargar", command=descargar_video, bg="#4285f4", fg="white")
descargar_button.grid(row=3, column=1, columnspan=2, pady=(0, 20), sticky="w")

root.mainloop()
