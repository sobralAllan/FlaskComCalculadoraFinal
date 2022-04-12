import this
import soma
import subtracao
import multiplicacao
import divisao
import tabuada
import vetores
this.opcao = 0 #Crio a variável global
num1 = 0
num2 = 0

def coletarNum1():
    print('Informe o primeiro número: ')
    this.num1 = float(input())

def coletarNum2():
    print('Informe o segundo número: ')
    this.num2 = float(input())

def mostrarMenu():
    print('Escolha uma das opções abaixo: ' +
          '\n1. Soma'          +
          '\n2. SUbtração'     +
          '\n3. Multiplicação' +
          '\n4. Divisão'       +
          '\n5. Tabuada'       +
          '\n6. Vetor'         +
          '\n0. Sair')
    this.opcao = int(input()) #Coletar a digitação do usuário

def operacao():
    #Mostrar o menu em tela
    while this.opcao != 5:
        mostrarMenu()
        #Realizar as operações
        if this.opcao == 1:
            #Operacao para a soma
            coletarNum1()
            coletarNum2()
            print(soma.somar(this.num1, this.num2))
        elif this.opcao == 2:
            #Operacao para a subtração
            coletarNum1()
            coletarNum2()
            print(subtracao.subtrair(this.num1, this.num2))
        elif this.opcao == 3:
            #Operacao para a multiplicação
            coletarNum1()
            coletarNum2()
            print(multiplicacao.multiplicar(this.num1, this.num2))
        elif this.opcao == 4:
            #Operacao para a divisão
            coletarNum1()
            coletarNum2()
            print(divisao.dividir(this.num1, this.num2))
        elif this.opcao == 5:
            coletarNum1()
            coletarNum2()
            print(tabuada.calcularTabuada(int(this.num1), int(this.num2)))
        elif this.opcao == 6:
            vetores.mostrarVetor()
        elif this.opcao == 0:
            print('Obrigado!')
        else:
            print('Opção escolhida invalida, tente novamente!')

