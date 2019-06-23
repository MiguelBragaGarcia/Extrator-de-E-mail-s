from PIL import Image # Importando o módulo Pillow para abrir a imagem no script

import os
import pytesseract # Módulo para a utilização da tecnologia OCR

#Caso tiver utilizando windows terá que passar onde o arquivo pytesseract.exe está em seu computador para que ele possa executar corretamente
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


#Esta variável recebe todos os nomes das imagens, a partir do caminho da pastas para fazer a automatização da estração dos textos
nomearquivo = os.listdir(" EX: C:\\Users\\nome do usuário\\Desktop\\Nova pasta\\Imagens")


#-----------------------------Funções----------------------------------------------------#
#Basicamente 2 funções de filtro
def primeiraposicao(dado):
    if ("@" not in dado[0]):
        return True
    else:
        return False

def temponto(dado):
     if ("." in dado):
        return True
     else:
        return False

#----------------------------------------------------------------------------------------#

for P in range(len(nomearquivo)):
 Dados= pytesseract.image_to_string( Image.open(" EX: C:\\Users\\nome do usuário\\Desktop\\Nova pasta\\Imagens\\"+str(nomearquivo[P])) )  # Extraindo o texto da imagem
 Dados = Dados.split() #transformando os textos em listas

 for I in range(len(Dados)):
         if (("@" in Dados[I]) and (primeiraposicao(Dados[I])) and (temponto(Dados[I])) ):
              arq=open ("EX: C:\\Users\\nome do usuário\\Desktop\\Nova pasta\\E-mail.txt",'a')
              arq.write(Dados[I]+"\n")
              arq.close()
              print(Dados[I])


          

