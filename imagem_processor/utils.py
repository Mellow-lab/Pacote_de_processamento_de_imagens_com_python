from PIL import Image

def process_image(image_path):
    try:
        # Verifica se o caminho da imagem é válido
        with Image.open(image_path) as img:
            # Aqui você pode fazer o processamento desejado, como redimensionamento ou conversão
            img = img.convert("RGB")  # Exemplo de conversão para RGB, dependendo da sua necessidade
            img.save("processed_image.jpg")  # Salva a imagem processada
            print("Imagem processada com sucesso!")
    except Exception as e:
        print(f"Erro ao processar a imagem: {e}")

# Exemplo de chamada da função
process_image('path/to/your/image.jpg')