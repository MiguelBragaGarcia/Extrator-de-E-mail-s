from PIL import Image # Importando o módulo Pillow para abrir a imagem no script

import os
import pytesseract # Módulo para a utilização da tecnologia OCR

#Caso tiver utilizando windows terá que passar onde o arquivo pytesseract.exe está em seu computador para que ele possa executar corretamente
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
LocalDosArquivos = "C:\\Users\\Nome do Usuário\\Desktop\\Teste de projeto"

#Esta variável recebe todos os nomes das imagens, a partir do caminho da pastas para fazer a automatização da estração dos textos
NomesdasImagens = os.listdir(LocalDosArquivos+"\\Imagens")


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

for P in range(len(NomesdasImagens)):
 Dados= pytesseract.image_to_string( Image.open(LocalDosArquivos+"\\Imagens\\"+str(NomesdasImagens[P])) )  # Extraindo o texto da imagem
 Dados = Dados.split() #transformando os textos em listas

 for I in range(len(Dados)):
         if (("@" in Dados[I]) and (primeiraposicao(Dados[I])) and (temponto(Dados[I])) ):
              arq=open (LocalDosArquivos+"\\E-mail.txt",'a')
              arq.write(Dados[I]+"\n")
              arq.close()
              print(Dados[I])
