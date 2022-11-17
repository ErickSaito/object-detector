import cv2 as cv
from image_measurements import ImageMeasurements
import inquirer


print("MC920 - Introdução ao Processamento de Imagem Digital - Trabalho 4")
print("Feito por Erick Saito")
print("Todas as imagens processadas serão salvas na pasta /results")

def main():
  while(True): 
    print()
    image_path = inquirer.list_input("Escolha a imagem que deseja realizar o filtro:",
                                  choices=['objetos1.png', 'objetos2.png', 'objetos3.png'])
    
    img = ImageMeasurements(f'images/{image_path}')

    process_choise = inquirer.list_input("Qual medida deseja tirar da imagem?",
                                  choices=['Transformação de cores', 'Contorno', 'Propriedades', 'Histograma'])
    
    measurements = {
      'Transformação de cores': lambda: img.color_tranformation(), 
      'Contorno': lambda: img.border_detection(),
      'Propriedades': lambda: img.properties(),
      'Histograma': lambda: img.histogram()
    }
    
    measurements[process_choise]()

    redo_process = inquirer.confirm('Fazer outro processamento?', default=True)

    if not redo_process:
      break

main()