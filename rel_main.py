### Reloj ###

import tkinter as tk
import time
import locale

# le decimos que lo queremos en español
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

def update_time():
    current_time = time.strftime("%H:%M:%S") # así se obtiene la hora actual
    current_date = time.strftime("%A, %d %B") # aquí el día de la semana, número y mes

    # actualizamos las etiquetas
    time_label.config(text=current_time)
    date_label.config(text=current_date)

    # actualizar cada segundo (se indica en milisegundos)
    root.after(1000, update_time)

# se crea una ventana simple
root = tk.Tk()
root.title("Reloj Digital")
root.geometry("500x200")
root.configure(bg="black") # fondo de la ventana

# se crean etiquetas para la hora y la fecha
time_label = tk.Label(root, font=("Helvetica bold", 45) , fg="#00f0ff", bg="black")
time_label.pack(pady=10)

date_label = tk.Label(root, font=("Rouge", 15), fg="#00f0ff", bg="black")
date_label.pack(pady=10)

# llamar la función de tiempo
update_time()

# ejecutar el bucle principal
root.mainloop()
