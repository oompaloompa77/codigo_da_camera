import cv2
import numpy as np

# criamos a url no celular e dps acessamos pelo pc para fazer os nossos testes
url_camera = "http://172.25.252.214:4747/video"

# criamos uma função para fazer toda a captura de tela desejada
def acessar_camera_celular(url):
   
    cap = cv2.VideoCapture(url)
    # verificando o acesso a camera do nosso celular
    if not cap.isOpened():
        print("Erro! Não foi possível abrir o stream de vídeo na URL fornecida.")
        print("Verifique se o celular e o PC estão na mesma rede e se a URL está correta.")
        return

    print("Conexão com a câmera estabelecida. Pressione 'Q' para sair.")
   
    # aqui criamos um loop para que
    while True:
        ret, frame = cap.read()
        # aqui estamos tentando acessar e pegar os frames da camera
        if not ret:
            print("Fim do stream ou falha na leitura do frame.")
            break

        # Exibe o frame na tela
        cv2.imshow('Camera do Celular (cv2)', frame)
       
        # faz esperar 1ms caso apertamos a tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # fechar todas as janelas do opencv
    cap.release()
    cv2.destroyAllWindows()

# estamos chamando a função principal que criamos
acessar_camera_celular(url_camera)