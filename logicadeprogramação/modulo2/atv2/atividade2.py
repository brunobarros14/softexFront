#Desenvolva um código que utilize as seguintes características de um veículo:
#- quantidade de rodas
#- Peso bruto em quilogramas;
#- Quantidade de pessoas no veículo.

#Com essas informações, o programa mostrará qual é a melhor categoria de habilitação para o veículo informado a partir das condições:
#A: Veículos com duas ou três rodas;
#B: Veículos com quatro rodas, que acomodam até oito pessoas e seu peso é de até 3500 kg;
#C: Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg;
#D: Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas;
#E: Veículos com quatro rodas ou mais e com mais de 6000 kg.

from time import monotonic


print ("ola, para saber a melhor categoria de habilitação me diga!")

rodas = int (input("quantas rodas tem?") )
peso = int (input("qual e o pesso do veiculo?"))
pasageiros = int (input("quantos pasageiros comporta?"))

if rodas <=3:
    print ("categoria A")
elif rodas == 4 and pasageiros <= 8 and peso <=3500:
    print ("categoria B")
elif rodas >= 4 and pasageiros <=8 and peso >3500 and peso <= 6000:
    print ("categoria c")
elif rodas >=4 and pasageiros > 8:
    print ("categoria D")
elif rodas >=4 and peso > 6000:
    print ("categoria E")
else: print ("informaçoes nao condis com nehuma categoria")