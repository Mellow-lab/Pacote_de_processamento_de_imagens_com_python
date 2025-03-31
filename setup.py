from setuptools import setup, find_packages

setup(
    name='imagem_processor',
    version='0.1.0',
    description='Um pacote para processamento de imagens com Python',
    author='Eduardo Melo',
    author_email='edumelo2205@gmail.com',
    url='https://github.com/seunome/imagem_processor',
    packages=find_packages(),
    install_requires=[
        'Pillow',  # Depende do Pillow para manipulação de imagens
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)