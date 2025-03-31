from imagem_processor.core import open_image, resize_image, save_image

image = open_image("caminho/para/imagem.jpg")
resized_image = resize_image(image, (200, 200))
save_image(resized_image, "caminho/para/imagem_redimensionada.jpg")