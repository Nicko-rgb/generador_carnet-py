import tkinter as tk
from tkinter import filedialog
from src.complement.centrar import centrar_ventana
from src.logic_carnet.genera_carnet import generar_carnet
from PIL import Image, ImageTk

foto_path = None
foto_logo = None
ruta_guardar = None

def seleccionar_foto():
    global foto_path
    foto_path = filedialog.askopenfilename(
        title="Seleccionar Foto", filetypes=[("Archivos de imagen", "*.jpg;*.png")]
    )
    foto_label.config(text=f"{foto_path.split('/')[-1]}")

def selecciona_logo():
    global foto_logo
    foto_logo = filedialog.askopenfilename(
        title="Seleccionar Logo", filetypes=[("Archivos de imagen", "*.jpg;*.png")]
    )
    label_logo.config(text=f"{foto_logo.split('/')[-1]}")

def abrir_ruta_config():
    
    def seleccionar_ruta():
        global ruta_guardar
        ruta_guardar = filedialog.askdirectory(title="Seleccionar Carpeta de Destino")
        ruta_entry.delete(0, tk.END)  # Limpiar el campo de entrada
        ruta_entry.insert(0, ruta_guardar)  # Insertar la ruta seleccionada en el Entry

    def guardar_ruta():
        global ruta_guardar
        if ruta_guardar:
            print(f"Ruta guardada: {ruta_guardar}")
            config_window.destroy()
        else:
            tk.messagebox.showwarning("Advertencia", "Debe configurar una ruta para guardar los carnets.")

            
    config_window = tk.Toplevel()
    config_window.configure(bg="#e6f6f4", padx=10, borderwidth=4, relief="groove")
    config_window.transient()  # Asegura que esta ventana esté sobre la principal
    config_window.grab_set()  # Bloquea la interacción con otras ventanas
    
    win_height = 150
    win_width = 370
    
    centrar_ventana(config_window, win_width, win_height)
    
    # Ocultar la barra de título
    config_window.overrideredirect(True)

    tk.Label(config_window, text="Seleccione la carpeta para guardar los carnets:", 
             font=("Arial", 12, 'italic'), bg="#e6f6f4").grid(row=0, column=0, columnspan=2, pady=10)

    # Campo de entrada para la ruta
    frame_ruta = tk.Frame(config_window, bg="#e6f6f4")
    frame_ruta.grid(row=1, column=0, columnspan=2, pady=5)

    ruta_entry = tk.Entry(frame_ruta, width=35, font=("Arial", 11), borderwidth=2, relief="ridge")
    ruta_entry.grid(row=0, column=0, padx=10, ipady=3)

    btn_browse = tk.Button(frame_ruta, text="•••", command=seleccionar_ruta, font=("Arial", 10), bg="#69d2cd", fg="black")
    btn_browse.grid(row=0, column=1)

    #frame para buttons
    frame_buttons = tk.Frame(config_window, bg='#e6f6f4')
    frame_buttons.grid(sticky='e', row=2, column=0, columnspan=2, pady=5)

    # Botones de Guardar y Cerrar
    btn_guardar = tk.Button(frame_buttons, text="Guardar ✓", command=guardar_ruta,
                            font=("Arial", 11, 'bold'), bg="#4CAF50", fg="white", width=10, borderwidth=2, relief="groove")
    btn_guardar.grid(row=0, column=0, padx=(0, 15), pady=2)

    btn_cerrar = tk.Button(frame_buttons, text="Cerrar ✕", command=config_window.destroy,
                           font=("Arial", 11, 'bold'), bg="#f57576", fg="white", width=10, borderwidth=2, relief="groove")
    btn_cerrar.grid(row=0, column=1, padx=0, pady=2)

def iniciar_formulario():
    from src.Interfaz.inicio import iniciar_inicio
    global foto_label, label_logo, nombre_entry, apellido_entry, dni_entry, carrera_entry, cod_entry, vigencia_entry

    root = tk.Tk()
    root.title("Generador de Carnet")
    
    # Definir el tamaño de la ventana
    window_width = 700
    window_height = 560
    
    # Centrar la ventana
    centrar_ventana(root, window_width, window_height)

    root.configure(bg="#e5e5e5",  borderwidth=4, relief="ridge", pady=20) 
    # Ocultar la barra de título
    root.overrideredirect(True)

    # Crear un marco para el formulario
    frame_formulario = tk.Frame(root, bg="#d2d2d2", borderwidth=2, relief='groove')
    frame_formulario.pack(padx=20)
    
    #texto formulario
    label_form = tk.Label(frame_formulario, text='FORMULARIO DE DATOS', font=('Helvetica', 15, 'bold'), bg='#d2d2d2', fg='#0195b9')
    label_form.grid(column=0, row=0, columnspan=2)
    
    # Cargar la imagen del icono
    icon_path = "img/ico-config.png"
    icon_image = Image.open(icon_path)
    icon_image = icon_image.resize((20, 20), Image.LANCZOS) 
    ico_config = ImageTk.PhotoImage(icon_image)
    
    #Crear button de configuracion
    button_configuracion = tk.Button(frame_formulario, bg='#a0a0a0', image=ico_config, width=25, height=25, 
                                 command=abrir_ruta_config, borderwidth=2, relief='ridge')
    button_configuracion.grid(row=0, column=0, columnspan=2, sticky='e', padx=10, pady=10)

    # Crear un marco para la parte izquierda (Nombre, Apellido y DNI)
    frame_izquierda = tk.Frame(frame_formulario, bg="#d2d2d2")
    frame_izquierda.grid(row=1, column=0, padx=10)

    tk.Label(frame_izquierda, text="Nombre 🖍", bg="#d2d2d2", font=("Arial", 11, 'bold')).grid(row=0, column=0, sticky="w")
    nombre_entry = tk.Entry(frame_izquierda, font=("Arial", 12), width=33, borderwidth=2, relief="ridge")
    nombre_entry.grid(row=1, column=0, ipady=3)

    tk.Label(frame_izquierda, text="Apellido 🖍", bg="#d2d2d2", font=("Arial", 11, 'bold')).grid(row=2, column=0, sticky="w", pady=(10, 0))
    apellido_entry = tk.Entry(frame_izquierda, font=("Arial", 12), width=33, borderwidth=2, relief="ridge")
    apellido_entry.grid(row=3, column=0, ipady=3)

    tk.Label(frame_izquierda, text="DNI 🖍", bg="#d2d2d2", font=("Arial", 11, 'bold')).grid(row=4, column=0, sticky="w", pady=(10, 0))
    dni_entry = tk.Entry(frame_izquierda, font=("Arial", 12), width=33, borderwidth=2, relief="ridge")
    dni_entry.grid(row=5, column=0, ipady=3)
    
    tk.Label(frame_izquierda, text='Universidad o Escuela 🖍', font=('Arial', 11, 'bold')).grid(row=6, column=0, sticky='w', pady=(10, 0))
    uni_entry = tk.Entry(frame_izquierda, font=('arial', 12), width=33, borderwidth=2, relief='ridge')
    uni_entry.grid(row=7, column=0, ipady=3)

    # Crear un marco para la parte derecha (Carrera, Universidad y Fecha de Vigencia)
    frame_derecha = tk.Frame(frame_formulario, bg="#d2d2d2")
    frame_derecha.grid(row=1, column=1, padx=10)

    tk.Label(frame_derecha, text="Carrera Profesional 🖍", bg="#d2d2d2", font=("Arial", 11, 'bold')).grid(row=0, column=0, sticky="w")
    carrera_entry = tk.Entry(frame_derecha, font=("Arial", 12), width=33, borderwidth=2, relief="ridge")
    carrera_entry.grid(row=1, column=0, ipady=3)

    tk.Label(frame_derecha, text="Código Estudiante 🖍", bg="#d2d2d2", font=("Arial", 11, 'bold')).grid(row=2, column=0, sticky="w", pady=(10, 0))
    cod_entry = tk.Entry(frame_derecha, font=("Arial", 12), width=33, borderwidth=2, relief="ridge")
    cod_entry.grid(row=3, column=0, ipady=3)

    tk.Label(frame_derecha, text="Fecha Vigencia 🖍", bg="#d2d2d2", font=("Arial", 11, 'bold')).grid(row=4, column=0, sticky="w", pady=(10, 0))
    vigencia_entry = tk.Entry(frame_derecha, font=("Arial", 12), width=33, borderwidth=2, relief="ridge")
    vigencia_entry.grid(row=5, column=0, ipady=3)
    
    tk.Label(frame_derecha, text='Selecciona un Logo 🖍', bg="#d2d2d2", font=("Arial", 11, 'bold')).grid(row=6, column=0, sticky='w', pady=(10, 0))
    
    frame_logo = tk.Frame(frame_derecha, bg='#d2d2d2')
    frame_logo.grid(row=7, columnspan=2, sticky='w')
    
    label_logo = tk.Label(frame_logo, text='No se ha selecciona logo', bg="#d2d2d2", font=("Arial", 10))
    label_logo.grid(row=0, column=1)
    
    logo_button = tk.Button(frame_logo, text='Seleciona logo', command=selecciona_logo, font=('arial', 11), bg="#8999ad", fg="black", borderwidth=2, relief="groove")
    logo_button.grid(row=0, column=0)
    
    #crear un frama select image
    frame_img = tk.Frame(frame_formulario, bg='#d2d2d2')
    frame_img.grid(row=2, columnspan=2)    

    # Label para mostrar la foto seleccionada
    foto_label = tk.Label(frame_img, text="No se ha seleccionado foto", bg="#d2d2d2", font=("Arial", 10))
    foto_label.grid(row=0, column=1, pady=20)
    
    # Cargar la imagen del icono
    icon_path = "img/img-ico.png"
    icon_image = Image.open(icon_path)
    icon_image = icon_image.resize((20, 20), Image.LANCZOS) 
    ico_img = ImageTk.PhotoImage(icon_image)

    # Botón para seleccionar la foto
    foto_btn = tk.Button(frame_img, text="Seleccionar Foto", command=seleccionar_foto, image=ico_img, compound=tk.LEFT,
                         font=("Arial", 11), bg="#8999ad", fg="black", borderwidth=2, relief="groove")
    foto_btn.grid(row=0, column=0, padx=0)
    
     # Cargar la imagen del icono
    icon_path = "img/carnet-ico.png"
    icon_image = Image.open(icon_path)
    icon_image = icon_image.resize((20, 20), Image.LANCZOS) 
    icon = ImageTk.PhotoImage(icon_image)

    # Botón para generar el carnet
    generar_btn = tk.Button(
        frame_formulario,
        text="Generar Carnet",
        image=icon,
        compound=tk.LEFT,
        command=lambda: generar_carnet(
            # nombre_entry.get(),
            # apellido_entry.get(),
            # dni_entry.get(),
            # uni_entry.get(),
            # carrera_entry.get(),
            # cod_entry.get(),
            # vigencia_entry.get(),
            # foto_path,
            # foto_logo,
            # ruta_guardar,
            
            'Ana Maria',
            'Padilla Linares',
            '12345678',
            'INSITUTO DE EDUCACION SUPERIOR TECNOLOGICO PUBLICO "SUIZA"',
            'Desarrollo de Sistemas de Informacion',
            '3020',
            '12-12-2024',
            foto_path,
            foto_logo,
            ruta_guardar
        ),
        font=("Helvetica", 12, 'bold'),
        bg="#5ea5ff",
        fg="black",
        padx=5,
        pady=5,
        borderwidth=2,
        relief='groove'
    )
    generar_btn.grid(row=3, column=0, columnspan=2, pady=(17, 30))
    
    # Crear un frame para el pie
    frame_pie = tk.Frame(root, bg="#e5e5e5")
    frame_pie.pack(side=tk.BOTTOM, fill=tk.X, padx=20, pady=0)
    
    # Botón para salir (cerrar la aplicación)
    boton_salir = tk.Button(frame_pie, text="✕ CERRAR", command=root.destroy,
                            font=("Arial", 10, 'bold'), bg="#f57576", fg="#d2d2d2", padx=10, pady=5, borderwidth=2, relief='groove')
    boton_salir.pack(side=tk.RIGHT, padx=(0, 0))
    
    #Btn para volver
    boton_volver = tk.Button(frame_pie, text="❮ VOLVER", command=lambda: [root.destroy(), iniciar_inicio()], 
                            font=("Helvetica", 10, 'bold'), bg="#d5ded9", fg="black", padx=10, pady=5, borderwidth=2, relief='groove')
    boton_volver.pack(side=tk.RIGHT, padx=(0, 20))
    
    # Label de derechos reservados
    label_derechos = tk.Label(frame_pie, text="© Derechos Reservados IESTP Suiza - 2024", 
                                font=('calibri', 9), bg="#e5e5e5", fg="#333")
    label_derechos.pack(side=tk.LEFT, padx=(0, 0)) 


    root.mainloop()
