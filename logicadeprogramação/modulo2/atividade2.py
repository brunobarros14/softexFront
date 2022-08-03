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

#A, A é para veículos motorizados de duas ou três rodas.
#A, B é para 4 rodas ou mais, desde que com peso até 3.500 quilos ou até 8 passageiros mais o motorista.
#A, C é para veículo motorizado utilizado em transporte de carga, cujo peso bruto total seja maior que três mil e quinhentos quilos.
#A, D é para veículo motorizado utilizado no transporte de passageiros, cuja lotação exceda a oito lugares + o motorista
#E a E, é aí que complica…, é para combinação de veículos em que a unidade tratora se enquadre nas 
# categorias B, C ou D e cuja unidade acoplada, reboque, semirreboque, 
# trailer ou articulada tenha 6.000 kg (seis mil quilogramas) ou mais de peso bruto total, ou cuja 
# lotação exceda a 8 (oito) lugares

if rodas <=3:
    print ("categoria A")
elif rodas == 4 and pasageiros <= 8 and peso <=3500:
    print ("categoria B")
    else:
        if peso >3500: 
            print("categoria C")
        else:
            if pasageiros >8:
                print("categoria D")
            else:
                if peso >=6000:
                    print("categoria E")                