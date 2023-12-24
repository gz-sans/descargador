import sys
import os
from pytube import YouTube
from tkinter import *
from tkinter import ttk, messagebox

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
    calidad = calidad_combobox.get()

    try:
        video = YouTube(enlace)
        descarga = video.streams.filter(res=calidad).first()

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

# Creación de la ventana del programa
root = Tk()
root.title("Descargador de YouTube")
root.geometry("400x200")
root.config(bg="#f0f0f0")

# Marco principal
main_frame = Frame(root, bg="#f0f0f0")
main_frame.grid(row=0, column=0)

# Etiqueta de instrucciones
instrucciones_label = Label(main_frame, text="Ingresa el enlace del video de YouTube:", bg="#f0f0f0", font=("Helvetica", 10))
instrucciones_label.grid(row=0, column=0, columnspan=2, pady=(10, 5), sticky="w")

# Entrada de URL
url_entry = Entry(main_frame, width=30, font=("Helvetica", 10))
url_entry.grid(row=1, column=0, columnspan=2, pady=(0, 10), padx=10, sticky="w")

# Etiqueta de calidad
calidad_label = Label(main_frame, text="Selecciona la calidad:", bg="#f0f0f0", font=("Helvetica", 10))
calidad_label.grid(row=2, column=0, columnspan=2, pady=(0, 5), padx=10, sticky="w")

# Combobox para seleccionar la calidad
calidades_disponibles = ["144p", "240p", "360p", "480p", "720p", "1080p"]
calidad_combobox = ttk.Combobox(main_frame, values=calidades_disponibles, state="readonly", font=("Helvetica", 10))
calidad_combobox.set("720p")  # Calidad predeterminada
calidad_combobox.grid(row=3, column=0, columnspan=2, pady=(0, 10), padx=10, sticky="w")

# Botón de descarga
descargar_button = Button(main_frame, text="Descargar", command=descargar_video, bg="#4285f4", fg="white", font=("Helvetica", 10))
descargar_button.grid(row=4, column=0, columnspan=2, pady=(0, 20), padx=10, sticky="w")

root.mainloop()
