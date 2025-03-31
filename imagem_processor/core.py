from PIL import Image, ImageFilter

def open_image(image_path):
    """Abre uma imagem a partir de um caminho fornecido."""
    try:
        return Image.open(image_path)
    except Exception as e:
        print(f"Erro ao abrir a imagem: {e}")
        return None

def save_image(image, output_path, format=None):
    """Salva a imagem em um caminho específico com formato opcional."""
    try:
        image.save(output_path, format=format)
    except Exception as e:
        print(f"Erro ao salvar a imagem: {e}")

def resize_image(image, size):
    """Redimensiona a imagem para o tamanho especificado."""
    return image.resize(size)

def blur_image(image):
    """Aplica um filtro de desfoque na imagem."""
    return image.filter(ImageFilter.BLUR)

def convert_to_grayscale(image):
    """Converte a imagem para escala de cinza."""
    return image.convert("L")