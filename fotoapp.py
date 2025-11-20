from PIL import Image, ImageFilter, ImageOps
import numpy as np
import cv2
import matplotlib.pyplot as plt

# 1) REDIMENSIONAR IMAGEN

def redimensionar_imagen(ruta, plataforma):
    plataforma = plataforma.lower()
    tamaños = {
        "youtube":  (1280, 720),
        "instagram": (1080, 1080),
        "twitter":  (1200, 675),
        "facebook": (1200, 630)
    }

    if plataforma not in tamaños:
        raise ValueError("Plataforma inválida.")
    
    try:
        img = Image.open(ruta)
    except:
        raise FileNotFoundError(f"No se encontró la imagen: {ruta}")

    new_w, new_h = tamaños[plataforma]
    img.thumbnail((new_w, new_h), Image.Resampling.LANCZOS)

    lienzo = Image.new("RGB", (new_w, new_h), (0, 0, 0))
    x = (new_w - img.width) // 2
    y = (new_h - img.height) // 2
    lienzo.paste(img, (x, y))

    nombre = f"imagen_{plataforma}.jpg"
    lienzo.save(nombre)
    return nombre



# 2) AJUSTE DE CONTRASTE 

def equalizar_contraste(ruta_imagen):
    img = cv2.imread(ruta_imagen)
    if img is None:
        raise FileNotFoundError(f"No se pudo cargar la imagen: {ruta_imagen}")

    # Equalización 
    ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    ycrcb[:,:,0] = cv2.equalizeHist(ycrcb[:,:,0])
    img_eq = cv2.cvtColor(ycrcb, cv2.COLOR_YCrCb2BGR)

    # Convertir 
    orig_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    eq_rgb   = cv2.cvtColor(img_eq, cv2.COLOR_BGR2RGB)

    # Mostrar comparación
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1); plt.imshow(orig_rgb); plt.title("Original"); plt.axis("off")
    plt.subplot(1, 2, 2); plt.imshow(eq_rgb);   plt.title("Ecualizada"); plt.axis("off")
    plt.show()

    # Guardar
    salida = ruta_imagen.rsplit('.', 1)[0] + "_comparacion.png"
    plt.savefig(salida, bbox_inches='tight')
    print("Guardado:", salida)

    return img, img_eq


# 3) FILTROS

FILTROS = {
    "ORIGINAL": None,
    "BLUR": ImageFilter.BLUR,
    "CONTOUR": ImageFilter.CONTOUR,
    "DETAIL": ImageFilter.DETAIL,
    "EDGE ENHANCE": ImageFilter.EDGE_ENHANCE,
    "EDGE ENHANCE MORE": ImageFilter.EDGE_ENHANCE_MORE,
    "EMBOSS": ImageFilter.EMBOSS,
    "FIND EDGES": ImageFilter.FIND_EDGES,
    "SHARPEN": ImageFilter.SHARPEN,
    "SMOOTH": ImageFilter.SMOOTH
}


def aplicar_filtro(imagen_path, filtro_usuario):
    filtro_usuario = filtro_usuario.upper()
    if filtro_usuario not in FILTROS:
        raise ValueError("Filtro inválido. Use: " + ", ".join(FILTROS))

    img = Image.open(imagen_path)

    # Aplicar filtro elegido
    img_filtrada = img if FILTROS[filtro_usuario] is None else img.filter(FILTROS[filtro_usuario])

    # Mostrar solo el filtro elegido
    plt.figure(figsize=(4, 4))
    plt.imshow(img_filtrada)
    plt.axis("off")
    plt.title(f"Filtro elegido: {filtro_usuario}", color="red")
    plt.show()

    img_filtrada.save(f"resultado_{filtro_usuario}.jpg")
    print(f"Imagen guardada como: resultado_{filtro_usuario}.jpg")

    # Mostrar todos los filtros 
    plt.figure(figsize=(12, 10))
    for i, (nombre, filtro) in enumerate(FILTROS.items(), start=1):
        nueva = img if filtro is None else img.filter(filtro)
        plt.subplot(4, 3, i)
        plt.imshow(nueva)
        plt.axis("off")
        plt.title(nombre, color="red" if nombre == filtro_usuario else "black")

    plt.tight_layout()
    plt.savefig("todos_los_filtros.jpg")
    plt.show()
    print("Figura completa guardada como: todos_los_filtros.jpg")


# 4) FUNCION PARA PINTORES

def generar_boceto(imagen_path, modo="lapiz"):

    img = cv2.imread(imagen_path)
    if img is None:
        raise FileNotFoundError("No se encontró la imagen.")

    gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    bordes = cv2.Canny(cv2.GaussianBlur(gris, (5, 5), 0), 60, 150)
    bordes_pil = Image.fromarray(bordes)

    if modo == "lapiz":
        boceto = ImageOps.autocontrast(ImageOps.invert(bordes_pil)).filter(ImageFilter.SMOOTH_MORE)

    elif modo == "binarizado":
        boceto = Image.fromarray((bordes > 70).astype(np.uint8) * 255)

    else:
        raise ValueError("Modo debe ser 'lapiz' o 'binarizado'.")

    # Mostrar Original + Boceto
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.figure(figsize=(10, 5))

    for i, (titulo, im) in enumerate([("Original", img_rgb), (f"Boceto ({modo})", boceto)], 1):
        plt.subplot(1, 2, i)
        plt.imshow(im, cmap="gray" if i == 2 else None)
        plt.axis("off")
        plt.title(titulo)

    plt.show()

    return boceto


# 5) MENÚ

def menu():

    imagen_cargada = None
    persona_detectada = True  # EL PROYECTO MARCA QUE OTRA FUNCION HACE ESTO
    while True:
        print("\n========== MENU FOTOAPP ==========")
        print("1) Cargar y redimensionar imagen (OBLIGATORIO)")
        print("2) Ajustar contraste")
        print("3) Aplicar filtro")
        print("4) Generar boceto artístico")
        print("5) Salir")

        opcion = input("Seleccione opción: ")

        try:
            if opcion == "1":
                ruta = input("Ruta de la imagen: ")
                plataforma = input("Plataforma: ")
                imagen_cargada = redimensionar_imagen(ruta, plataforma)
                print("Imagen cargada:", imagen_cargada)

            elif opcion in ["2", "3", "4"]:
                if imagen_cargada is None:
                    raise RuntimeError("Primero debe cargar la imagen (opción 1).")
                        
                if opcion == "2":
                    equalizar_contraste(imagen_cargada)

                elif opcion == "3":
                    print("\nFiltros disponibles:")
                    for f in FILTROS.keys():
                        print(" -", f)
                    filtro = input("Ingrese filtro: ")
                    aplicar_filtro(imagen_cargada, filtro)

                elif opcion == "4":
                    modo = input("Modo de boceto (lapiz/binarizado): ")
                    generar_boceto(imagen_cargada, modo)

            elif opcion == "5":
                print("Saliendo...")
                break

            else:
                print("Opción inválida.")
        except Exception as error:
            print("Error:", error)


# MENU 

if __name__ == "__main__":
    menu()