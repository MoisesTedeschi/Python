## Usando Python, Google Speech e sua Voz para criar textos, gravar áudios e navegar na internet

![](https://github.com/MoisesTedeschi/Python/blob/master/Python%20-%20Google%20Speech%20-%20Sua%20Voz/img/python-google-speech.png)

## Objetivo
Mostrar o reconhecimento de fala e como você pode converter sua voz em texto com Python usando o Google Speech. 
Usaremos uma biblioteca de reconhecimento para a realização do "reconhecimento da fala". Ela tem suporte para vários mecanismos e API's.

## Mecanismo ou API's de Reconhecimento de Fala

* Reconhecimento de fala do Google
* API do Google Cloud Speech
* Reconhecimento de voz do Microsoft Bing
* Fala da IBM em Texto
* Detecção de palavras-chave do Snowboy (funciona offline)

## Bibliotecas Usadas

* [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
* [pyaudio](https://pypi.org/project/PyAudio/)

* OBS: Se não for possível instalar o Pyaudio com o comando do PIP, o problema pode ser resolvido
com a instalação da LIB: [pipwin](https://pypi.org/project/pipwin/) (Idem ao link do stackoverflow abaixo sobre o possível problema.). Assim sendo, a instalação ficaria assim: 

```sh
pip install pipwin 
pipwin install pyaudio
```

## Erro de Instalação no Windows

[Para possíveis erros na instalação da Lib Pyaudio no Windows](https://stackoverflow.com/questions/53866104/pyaudio-failed-to-install-windows-10)

## Referências

[Sobre as Chaves de API do Google](http://www.chromium.org/developers/how-tos/api-keys)

[Referência Speech Recognition](https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rst)


Por: [@TheMOA](https://twitter.com/TheMoaMe)
E-mail: moisestedeschi@gmail.com
