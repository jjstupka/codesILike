import cv2
import numpy as np

# Input video
cap = cv2.VideoCapture(0) #"0" endereço da camera principal.

# Verifica se a camera abriu.
if (cap.isOpened() == False):
    print("Error opening video file")

# Roda até finalizar o vídeo
while (cap.isOpened()):

    # Captura frame por frame
    ret, frame = cap.read()
    if ret == True:
        # Mostra os frames
        cv2.imshow('Frame', frame)

        # Pressione Q para sair
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Fim do loop
    else:
        break

cap.release()
cv2.destroyAllWindows()
