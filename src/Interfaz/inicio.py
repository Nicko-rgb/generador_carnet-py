import tkinter as tk
from PIL import Image, ImageTk
from src.Interfaz.formulario import iniciar_formulario
from src.complement.centrar import centrar_ventana

def iniciar_inicio():
    
    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Inicio")
    
    # Definir el tamaño de la ventana
    window_width = 700
    window_height = 500
    
    # Centrar la ventana
    centrar_ventana(ventana, window_width, window_height)

    ventana.configure(bg="#e5e5e5", borderwidth=4, relief="ridge")  # Color de fondo

    # Ocultar la barra de título
    ventana.overrideredirect(True)

    # Crear un marco para los logos
    frame_logos = tk.Frame(ventana, bg="#e5e5e5")
    frame_logos.pack(side=tk.TOP, fill=tk.X, pady=15, padx=20)
    
    # Crear un frame para el pie
    frame_pie = tk.Frame(ventana, bg="#e5e5e5")
    frame_pie.pack(side=tk.BOTTOM, fill=tk.X, padx=20, pady=20)

    # Cargar y mostrar el logo izquierdo
    try:
        logo_izquierdo = Image.open("IMG/logo.png")  # Cambia esta ruta por la ubicación de tu logo izquierdo
        logo_izquierdo = logo_izquierdo.resize((60, 60), Image.LANCZOS)  # Redimensionar el logo
        logo_img_izquierdo = ImageTk.PhotoImage(logo_izquierdo)

        label_logo_izquierdo = tk.Label(frame_logos, image=logo_img_izquierdo, bg="#e5e5e5")
        label_logo_izquierdo.pack(side=tk.LEFT, padx=(0, 0))  # Espacio horizontal alrededor del logo izquierdo
    except Exception as e:
        print(f"No se pudo cargar el logo izquierdo: {e}")

    # Cargar y mostrar el logo derecho
    try:
        logo_derecho = Image.open("IMG/dsiLogo.png")  # Cambia esta ruta por la ubicación de tu logo derecho
        logo_derecho = logo_derecho.resize((60, 60), Image.LANCZOS)  # Redimensionar el logo
        logo_img_derecho = ImageTk.PhotoImage(logo_derecho)

        label_logo_derecho = tk.Label(frame_logos, image=logo_img_derecho, bg="#e5e5e5")
        label_logo_derecho.pack(side=tk.RIGHT, padx=(0, 0))  # Espacio horizontal alrededor del logo derecho
    except Exception as e:
        print(f"No se pudo cargar el logo derecho: {e}")

    # Cargamos un texto entre medio de los logos
    txt_intitu = tk.Label(frame_logos, text='INSTITUTO DE EDUCACION SUPERIOR TECNOLÓGICO\nPÚBLICO SUIZA', font=('Arial', 12, 'bold'), bg='#e5e5e5', fg='#0077ce')
    txt_intitu.pack(pady=20, padx=0)

    # Etiqueta de bienvenida en el centro
    label_bienvenida = tk.Label(ventana, text="Programa de Generador de Carnet!", font=("Helvetica", 15, "bold"), bg="#e5e5e5", fg="#00a0b0")
    label_bienvenida.pack(pady=10)

    # Descripción del programa
    label_descripcion = tk.Label(ventana, text="Este es un programa increíble que hará cosas geniales.", 
                                  font=("Helvetica", 12), bg="#e5e5e5", fg="#555")
    label_descripcion.pack(pady=5)
    
    # Cargar la imagen del icono
    icon_path = "IMG/inicia.png"
    icon_image = Image.open(icon_path)
    icon_image = icon_image.resize((20, 20), Image.LANCZOS) 
    icon = ImageTk.PhotoImage(icon_image)
    
    def on_enter(event):
        event.widget['bg'] = '#00808d'  # Cambia a color verde claro al pasar el cursor
        
    def on_leave(event):
        event.widget['bg'] = '#00a0b0'

    # Botón para iniciar el programa
    boton_iniciar = tk.Button(ventana, text="Iniciar Programa", image=icon, compound=tk.LEFT, command=lambda: [ventana.destroy(), iniciar_formulario()],
                               font=("Helvetica", 12, 'bold'), bg="#00a0b0", fg="white", activebackground='#00808d', padx=10, pady=10, borderwidth=2, relief='groove')
    boton_iniciar.pack(pady=40)
    boton_iniciar.bind('<Enter>', on_enter)
    boton_iniciar.bind('<Leave>', on_leave)

    # Botón para salir (cerrar la aplicación)
    boton_salir = tk.Button(frame_pie, text="✕ CERRAR", command=ventana.destroy,
                            font=("Helvetica", 10, 'bold'), bg="#f57576", fg="white", padx=10, pady=5, borderwidth=2, relief='groove')
    boton_salir.pack(side=tk.RIGHT, padx=(0, 0))
    
    # Label de derechos reservados
    label_derechos = tk.Label(frame_pie, text="© Derechos Reservados IESTP Suiza - 2024", 
                                font=('calibri', 9), bg="#e5e5e5", fg="#333")
    label_derechos.pack(side=tk.LEFT, padx=(0, 0))  # Espacio a la izquierda del label

    # Ejecutar el bucle principal
    ventana.mainloop()
