import tkinter as tk
from tkinter import scrolledtext
import openai
import re

# Configuración de OpenAI
openai.api_key = "null"
model_engine = "gpt-3.5-turbo"

# Crear la interfaz gráfica
window = tk.Tk()
window.title("Chat con ChatGPT")

# Crear el campo de entrada de texto y el botón para enviar el mensaje
input_field = tk.Entry(window, width=50)
input_field.pack(side=tk.LEFT, padx=5, pady=5)
input_field.focus()

def send_message(event=None):
    # Obtener el mensaje ingresado por el usuario
    message = input_field.get()
    # Limpiar el mensaje de caracteres especiales
    message = re.sub(r'[^\w\s]', '', message)
    # Agregar el mensaje al historial
    chat_history.configure(state='normal')
    chat_history.insert(tk.END, "Usuario: " + message + "\n")
    chat_history.configure(state='disabled')
    chat_history.yview(tk.END)
    # Generar la respuesta de ChatGPT
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "user", "content": message}
      ]
    )
    """response = openai.Completion.create(
        engine=model_engine,
        prompt=message,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.7,
    )"""
    # Agregar la respuesta al historial
    chat_history.configure(state='normal')
    chat_history.insert(tk.END, "ChatGPT: " + str(response.choices[0].message.content) + "\n")
    chat_history.configure(state='disabled')
    chat_history.yview(tk.END)
    # Limpiar el campo de entrada
    input_field.delete(0, tk.END)

send_button = tk.Button(window, text="Enviar", command=send_message)
send_button.pack(side=tk.LEFT, padx=5, pady=5)

# Crear el historial del chat
chat_history = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=60, height=10)
chat_history.pack(side=tk.BOTTOM, padx=5, pady=5)
chat_history.configure(state='disabled')

# Iniciar la ventana
window.bind('<Return>', send_message)
window.mainloop()
