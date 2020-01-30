import speech_recognition as sr
 
 
def main():

    # Inicializando o "Reconhecedor"
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        # Objeto reconhecedor, também para remover ruídos, precisamos adicionar esta linha de código.
        r.adjust_for_ambient_noise(source, duration=1)
        
        print("Por favor, diga alguma coisa.")
        
        audio = r.listen(source)
        
        print("Reconhecendo agora... ")
        
        # Reconhecer fala usando o google
        try:
            # Aqui estamos reconhecendo o discurso (a fala) usando o Google Speech.
            # Lembrando: Não gerei uma API para o projeto. Logo estou usando uma API KEY
            # padrão do Google. Assim sendo, para projetos mais elaborados, cinceramente,
            # recomendo a geração de uma API própria e evitar o uso da API KEY padrão.
            print("Você disse:\n" + r.recognize_google(audio, language="pt-BR"))
            print("Áudio gravado com sucesso!\n")

            # Escrever áudio
            with open("gravando.wav", "wb") as f:
                # Aqui vamos gravar o áudio.
                f.write(audio.get_wav_data())
            
        except sr.UnknownValueError:
            print("O Google Cloud Speech não conseguiu entender o áudio.")
        
        except sr.RequestError as e:
            print("Não foi possível solicitar resultados do serviço Google Cloud Speech. {0}".format(e))
            

if __name__ == "__main__":
    main()
