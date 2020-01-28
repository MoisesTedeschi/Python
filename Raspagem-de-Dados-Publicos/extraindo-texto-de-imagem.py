"""
O que é OCR?
OCR é uma sigla em inglês da expressão Optical Character Recognition – que pode ser traduzida como “reconhecimento
óptico de caracteres”. Na prática, essa tecnologia faz a leitura de um arquivo em imagem para identificar padrões e/ou
transcrever textos que estão contidos na peça e transcrever.

Essa tecnologia têm diversas variações e aplicações. Veja alguns exemplos comuns do cotidiano em que o OCR é aplicado:

registro de informações em formulários quadriculados,
identificação apostas de loteria,
registro de alternativas nos cartões de respostas de vestibulares e concursos,
digitalização de documentos impressos,
digitalização de livros antigos.
Além disso, a tecnologia OCR pode ser conectada a outros recursos, como identificação de dados a partir de uma
imagem – como uma foto do rosto identificar o número de RG, por exemplo.

Mesmo que muitos documentos já sejam digitais, ainda existem outros que estão apenas impressos e são utilizados
para confirmação de identidade, por exemplo.

Fonte: https://blog.cedrotech.com/entenda-o-que-e-ocr-optical-character-recognition/

A engine OCR que vamos utilizar é a Tesseract, a mesma foi inicialmente desenvolvida nos laboratórios da HP e
tem seu projeto hospedado em: https://github.com/tesseract-ocr/tesseract.

Instalação - https://github.com/tesseract-ocr/tesseract/wiki
Instalação no Windows: https://github.com/UB-Mannheim/tesseract/wiki

"""
#from PIL import Image
#import pytesseract
#print(pytesseract.image_to_string(Image.open('img/enough-blah-blah.jpg')))

from PIL import Image
import pytesseract


def img_core_file(imgfile):
    """
    A função manipulará o processamento principal de imagens OCR.
    """
    text_extracao = pytesseract.image_to_string(Image.open(imgfile), lang='por')
    # Usaremos a classe Image do Pillow para abrir a imagem e
    # o pytesseract para detectar a string na imagem
    # É muito IMPORTANTE que o valor “lang” esteja em português, pq o valor
    # padrão é inglês. Logo, afeta no resultado de saída do texto.

    return text_extracao

print(img_core_file('img/vaidarcerto.jpg'))
