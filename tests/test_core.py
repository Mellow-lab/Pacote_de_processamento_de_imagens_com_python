import unittest
from imagem_processor.core import resize_image
from PIL import Image

class TestImageProcessor(unittest.TestCase):
    def test_resize_image(self):
        """Testa se a função de redimensionamento funciona corretamente."""
        img = Image.new('RGB', (100, 100), color=(255, 0, 0))  # Cria uma imagem vermelha
        resized_img = resize_image(img, (50, 50))
        self.assertEqual(resized_img.size, (50, 50))

if __name__ == "__main__":
    unittest.main()