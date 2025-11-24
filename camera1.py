import cv2
import numpy as np

# URL da câmera do celular
url_camera = "http://172.25.252.214:4747/video"

# Carrega o classificador de rosto
cascade_face = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

def acessar_camera_celular(url):

    cap = cv2.VideoCapture(url)

    if not cap.isOpened():
        print("Erro! Não foi possível abrir o stream de vídeo na URL fornecida.")
        print("Verifique se o celular e o PC estão na mesma rede e se a URL está correta.")
        return

    print("Conexão com a câmera estabelecida. Pressione 'Q' para sair.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Fim do stream ou falha na leitura do frame.")
            break

        # Converte para preto e branco
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detecta os rostos
        faces = cascade_face.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(60, 60)
        )

        # Número de rostos detectados
        num_faces = len(faces)

        # Escreve a contagem na tela
        cv2.putText(frame, f"Rostos detectados: {num_faces}",
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 255, 255), 2)

        # Desenha retângulos nos rostos detectados
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, "Rosto", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        # Exibe o vídeo
        cv2.imshow("Deteccao de Rosto - OpenCV", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


acessar_camera_celular(url_camera)
