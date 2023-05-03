import openai
import requests
from io import BytesIO
from PIL import Image, ImageTk
import tkinter as tk
import os

# Configuración de OpenAI
openai.api_key = "null"
model_engine = "image-alpha-001"

# Función para generar la imagen a partir del texto
def generate_image(text):
    data = {
        "model": model_engine,
        "prompt": f"Create an image of {text}",
        "num_images": 1,
        "size": "512x512",
    }


    response = openai.Image.create(
        prompt=text,
        n=2,
        size="512x512"
    )
    image_url = response['data'][0]['url']
    
    return Image.open(requests.get(image_url, stream=True).raw)

# Función para mostrar la imagen generada
def display_image(image):
    global image_label
    # Eliminar la imagen anterior
    if image_label:
        image_label.destroy()
    # Convertir la imagen para mostrarla en Tkinter
    image = ImageTk.PhotoImage(image)
    image_label = tk.Label(window, image=image)
    image_label.image = image
    image_label.pack()

# Crear la interfaz gráfica
window = tk.Tk()
window.title("Generador de Imágenes DALL-E 2")

# Crear el campo de texto y el botón para generar la imagen
text_field = tk.Entry(window, width=50)
text_field.pack()
generate_button = tk.Button(window, text="Generar imagen", command=lambda: display_image(generate_image(text_field.get())))
generate_button.pack()

# Mostrar la ventana
image_label = None
window.mainloop()
