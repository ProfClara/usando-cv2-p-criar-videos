#import cv2
import cv2
#crie uma  variável que guarda as imagens fornecidas pela webcam  do  pc
video=cv2.VideoCapture(0)
#video=cv2.VideoCapture(meuvideo.mp4)

"""Etapa para evitar dor de cabeça: 
Peça p/ o computador avisar caso algo dê errado 
na captura do vídeo"""
if(video.isOpened()==False):
    print("Deu ruim... :( ")

# capturando a altura do vídeo
altura=int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(altura)
# capturando a largura do vídeo
largura=int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
print(largura)
# capturando os frames por segundo do vídeo
fps=int(video.get(cv2.CAP_PROP_FRAME_FPS))
print(fps)

#Loop para ler os frames depois exibir(em forma de vídeo)
while(True):
  ret,frame=video.read()
  cv2.imshow("Resultado da webCam ",frame)
  if cv2.waitKey(25)==27:
    break
video.release()    
