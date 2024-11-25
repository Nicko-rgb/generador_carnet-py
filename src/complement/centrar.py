
def centrar_ventana(window, width, height):
    # Obtener dimensiones de la pantalla
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calcular las coordenadas x e y
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    # Establecer la geometría de la ventana
    window.geometry(f"{width}x{height}+{x}+{y}")
