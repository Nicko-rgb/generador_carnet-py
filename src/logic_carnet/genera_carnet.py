from PIL import Image, ImageDraw, ImageFont
import qrcode
import tkinter as tk
from src.logic_carnet.ajusta_foto_user import ajustar_foto_user

def generar_carnet(nombre, apellido, dni, universidad, carrera, cod_estudiante, vigencia, foto_path, foto_logo, ruta_guardar):
    
    def datos_validos(*args):
        return all(args)  # Devuelve True si todos los argumentos son no vacíos y no nulos
    
    # verificar datos
    if not datos_validos(nombre, apellido, dni, universidad, carrera, cod_estudiante, vigencia, foto_path, foto_logo):
        tk.messagebox.showwarning("Información", "Todos los campos deben ser completados.")
        return
    
    # dimensiones del carnet (5.4 x 8.6 cm a 300 dpi)
    # ancho, alto = 1012, 638 # Tamaño estándar de un DNI
    ancho, alto = 800, 500 
     # Cargar imagen de fondo
    try:
        fondo = Image.open('IMG/fondo.png').resize((ancho, alto))  # Redimensionar al tamaño del carnet
        carnet = fondo.copy()  # Usar la imagen como base
    except FileNotFoundError:
        print("Advertencia: No se encontró el archivo del fondo. Usando fondo sólido.")
        carnet = Image.new('RGB', (ancho, alto), '#D4E8FC')  # Fondo azul claro como respaldo

    draw = ImageDraw.Draw(carnet)

    # Cargar fuentes
    try:
        fuente_titulo = ImageFont.truetype("arialbd.ttf", 25)
        fuente_texto = ImageFont.truetype("arial.ttf", 20)
        fuente_vigen = ImageFont.truetype('arialbd.ttf', 20)
        fuente_indicador = ImageFont.truetype('calibri', 18)
        fuente_dni = ImageFont.truetype('arialbd.ttf', 22)
        fuente_negrita = ImageFont.truetype("arialbd.ttf", 27)
    except IOError:
        fuente_titulo = fuente_texto = fuente_negrita = ImageFont.load_default()
        
    #funcion para centrar texto
    def centrar_text(texto, fuente_letra):
        bbox = draw.textbbox((0, 0), texto, font=fuente_letra)
        ancho_texto = bbox[2] - bbox[0]
        centro = (ancho - ancho_texto) / 2
        return centro

    # Texto a centrar
    def dividir_texto(texto, fuente, ancho_maximo):
        palabras = texto.split()
        lineas = []
        linea_actual = ""
        draw = ImageDraw.Draw(Image.new("RGB", (1, 1)))  # Canvas temporal para medir el texto

        for palabra in palabras:
            # Prueba agregar la palabra actual a la línea actual
            prueba_linea = f"{linea_actual} {palabra}".strip()
            ancho_texto = draw.textbbox((0, 0), prueba_linea, font=fuente)[2]

            if ancho_texto <= ancho_maximo:
                # Si la línea cabe, actualizamos la línea actual
                linea_actual = prueba_linea
            else:
                # Si no cabe, guardamos la línea actual y comenzamos una nueva
                lineas.append(linea_actual)
                linea_actual = palabra

        # Añadir la última línea
        if linea_actual:
            lineas.append(linea_actual)

        return lineas
    
    # Texto a centrar
    descr = 'CARNET DE ESTUDIANTE'
    ancho_maximo_texto = 600  # Ancho máximo permitido

    # Dividir el texto de la universidad si es necesario
    lineas_universidad = dividir_texto(universidad, fuente_titulo, ancho_maximo_texto)

    # Dibujar las líneas centradas
    y_actual = 20  # Coordenada inicial en el eje Y
    for linea in lineas_universidad:
        x = centrar_text(linea, fuente_titulo)  # Centrar cada línea
        draw.text((x - 60, y_actual), linea, font=fuente_titulo, fill="#124aca")
        y_actual += 25  # Espaciado entre líneas (ajustable según la altura del texto)
        
    #Dibujar linea
    
    draw.line((50, y_actual + 10, 620, y_actual+10), fill="#0f41b0", width=2)
    
    # Dibujar el título del carnet
    xx = centrar_text(descr, fuente_dni)
    draw.text((xx - 60, y_actual + 20), descr, font=fuente_dni, fill="black")

    # Cargar y colocar el logo
    try:
        logo = Image.open(foto_logo).convert("RGBA")  # Convertir a RGBA para soportar transparencia
        
        # Procesar el fondo del logo para hacerlo transparente
        datas = logo.getdata()
        nueva_imagen = []
        for item in datas:
            # Revisar si el píxel es negro (o blanco)
            if item[:3] == (0, 0, 0):  # Si el color es negro (RGB: 0, 0, 0)
                nueva_imagen.append((0, 0, 0, 0))  # Hacerlo transparente
            else:
                nueva_imagen.append(item)
        
        # Aplicar los cambios al logo
        logo.putdata(nueva_imagen)
        
        # Redimensionar el logo y colocarlo en el carnet
        logo = logo.resize((100, 100))
        carnet.paste(logo, (680, 20), logo)  # El tercer argumento permite manejar transparencias
    except FileNotFoundError:
        print("Advertencia: No se encontró el archivo del logo.")

    # Foto del estudiante
    foto_final = ajustar_foto_user(foto_path)
    if foto_final:
        carnet.paste(foto_final, (20, 140))

    # Añadir datos del estudiante
    draw.text((230, 145), 'Nombres Completos:', font=fuente_indicador, fill='black')
    draw.text((230, 165), apellido, font=fuente_negrita, fill='black')
    draw.text((230, 190), nombre, font=fuente_negrita, fill='black')
    draw.text((230, 235), 'Carrera profesional', font=fuente_indicador, fill='black')
    ancho_carrera = 350
    linea_carrera = dividir_texto(carrera, fuente_negrita, ancho_carrera)
    y_carre = 255  # coordenada inicial en el eje Y
    for linea in linea_carrera:
        x = centrar_text(linea, fuente_negrita)  # Centrar cada línea
        draw.text((230, y_carre), linea, font=fuente_negrita, fill="black")
        y_carre += 30  # espaciado entre líneas
    
    draw.text((230, y_carre + 10), 'Código de Estudiante:', font=fuente_indicador, fill='black')
    draw.text((230, y_carre + 30), cod_estudiante, font=fuente_negrita, fill='black')
    dnix = centrar_text(f'DNI: {dni}', fuente_dni)
    draw.text((dnix - 280, 380), f"DNI: {dni}", font=fuente_dni, fill="black")
    draw.text((20, 460), f"Vigencia: {vigencia}", font=fuente_vigen, fill="black")

    # generar código QR
    qr_data = (f"Nombres: {nombre} {apellido}\n"
               f"DNI: {dni}\n"
               f"Carrera: {carrera}\n"
               f"Universidad o Instituto: {universidad}\n"
               f"Codigo de Estudiante: {cod_estudiante}\n"
               f"Vigencia: {vigencia}")
    qr = qrcode.make(qr_data).resize((170, 170))  # Ajustar tamaño del QR
    carnet.paste(qr, (610, 310))

    # guardar el carnet
    if not ruta_guardar:
        tk.messagebox.showwarning("Advertencia", "Debe configurar una ruta para guardar los carnets antes de generar.")
        return
    
    output_path = f"{ruta_guardar}/carnet-{dni}.png"
    try:
        carnet.save(output_path)
        carnet.show()
        print(f"Carnet generado y guardado en: {output_path}")
        return True 
    except Exception as e:
        print(f"Error al generar el carnet: {e}")
        return False  # Indica fallo
    
    
