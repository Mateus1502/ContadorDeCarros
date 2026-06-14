import cv2
import numpy as np

video = cv2.VideoCapture('contacarros.mp4')

contador = 0
liberado = False

# Detector de movimento
detector = cv2.createBackgroundSubtractorMOG2(
    history=100,
    varThreshold=40,
    detectShadows=False
)

while True:

    ret, img = video.read()

    if not ret:
        break

    img = cv2.resize(img, (1100, 720))

    # Área de contagem
    x = 180
    y = 320
    w = 450
    h = 180
    # Detecta movimento
    mascara = detector.apply(img)

    # Limpeza da máscara
    kernel = np.ones((5, 5), np.uint8)

    mascara = cv2.morphologyEx(
        mascara,
        cv2.MORPH_OPEN,
        kernel
    )

    imgDil = cv2.dilate(
        mascara,
        kernel,
        iterations=2
    )

    # Região monitorada
    recorte = imgDil[y:y+h, x:x+w]

    carros = cv2.countNonZero(recorte)

    # Captura tecla
    tecla = cv2.waitKey(20) & 0xFF

    # Lógica de contagem
    if carros > 6000 and liberado:
        contador += 1
        liberado = False

    if carros < 3000:
        liberado = True

    # Desenha região
    if liberado:
        cor = (255, 0, 255)
    else:
        cor = (0, 255, 0)

    cv2.rectangle(
        img,
        (x, y),
        (x + w, y + h),
        cor,
        4
    )

    cv2.rectangle(
        imgDil,
        (x, y),
        (x + w, y + h),
        255,
        3
    )

    cv2.putText(
    img,
    str(contador),
    (500, 220),
    cv2.FONT_HERSHEY_SIMPLEX,
    4,
    (255, 255, 255),
    6
)
    cv2.imshow('video original', img)
    #usei somente para testes da biblioteca, para mostrar a mascara de movimento
    #cv2.imshow('mascara', cv2.resize(imgDil, (600, 500)))

    if tecla == 27:  # ESC
        break

video.release()
cv2.destroyAllWindows()
