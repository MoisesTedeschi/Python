import speech_recognition as sr
import webbrowser as web
 
 
def main():

    # Adicionando o drive do Chrome no projeto.
    path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"

    # Inicializando o "Reconhecedor"
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        # Objeto reconhecedor, também para remover ruídos, precisamos adicionar esta linha de código.
        r.adjust_for_ambient_noise(source, duration=1)
        
        print("Por favor, fale o endereço do site.")
        
        # "Ouvindo" o arquivo falado. 
        audio = r.listen(source)
        
        print("Reconhecendo agora... ")

        # Reconhecer fala usando o google
        try:
            # Aqui estamos reconhecendo o endereço falado usando o Google Speech.
            # language="pt-BR" para Português do Brasil, é claro.

            # Lembrando: Não gerei uma API para o projeto. Logo estou usando uma API KEY
            # padrão do Google. Assim sendo, para projetos mais elaborados, cinceramente,
            # recomendo a geração de uma API própria e evitar o uso da API KEY padrão.
            
            destino = r.recognize_google(audio)

            # Mostrando na saída do áudio.
            print("Você disse: " + destino)

            # Abrindo o navegador e indo até o site informado por voz.
            web.get(path).open(destino)
            
        except sr.UnknownValueError:
            print("O Google Cloud Speech não conseguiu entender o áudio.")
        
        except sr.RequestError as e:
            print("Não foi possível solicitar resultados do serviço Google Cloud Speech. {0}".format(e))
            # ERRO : recognition request failed: Forbidden


if __name__ == "__main__":
    main()
