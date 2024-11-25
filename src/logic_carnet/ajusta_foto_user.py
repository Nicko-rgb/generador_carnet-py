from PIL import Image


def ajustar_foto_user(foto_path):
    if foto_path:
        try:
            foto = Image.open(foto_path)
            foto = foto.convert("RGBA")  # Asegurar canal alfa para manejar transparencias

            # Dimensiones deseadas para el carnet
            ancho_deseado, alto_deseado = 200, 240

            # Obtener dimensiones originales de la imagen
            ancho_original, alto_original = foto.size

            # Calcular proporciones para mantener la relación de aspecto
            proporción_ancho = ancho_deseado / ancho_original
            proporción_alto = alto_deseado / alto_original

            # Escalar la imagen para cubrir completamente el espacio
            if proporción_ancho > proporción_alto:
                nuevo_ancho = ancho_deseado
                nuevo_alto = int(alto_original * proporción_ancho)
            else:
                nuevo_ancho = int(ancho_original * proporción_alto)
                nuevo_alto = alto_deseado

            # Redimensionar la imagen
            foto_redimensionada = foto.resize((nuevo_ancho, nuevo_alto), Image.LANCZOS)

            # Calcular las coordenadas para recortar el centro
            left = (nuevo_ancho - ancho_deseado) // 2
            top = (nuevo_alto - alto_deseado) // 2
            right = left + ancho_deseado
            bottom = top + alto_deseado

            # Recortar la imagen al tamaño deseado
            foto_final = foto_redimensionada.crop((left, top, right, bottom))
            return foto_final

        except FileNotFoundError:
            print("Advertencia: No se encontró el archivo de la foto.")
            return None
