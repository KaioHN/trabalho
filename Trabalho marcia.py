#Questao 1
matriz = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

#Seleciona os elementos dentro da linhas e colunas.
numero1 = matriz[0][0]
numero2 = matriz[1][0]
numero3 = matriz[2][0]
numero4 = matriz[3][0]
#soma todos os elementos.
result = numero1 + numero2 + numero3 + numero4
print(result)

#Questao 2

#Seleciona os elementos da linha
num1 = matriz[0][0]
num2 = matriz[0][1]
num3 = matriz[0][2]
num4 = matriz[0][3]

#multiplica todos os elementos
Result = num1 * num2 * num3 * num4
print(Result)


#Questao 3
Soma = 0
#Seleciona I = linhas e J = colunas 
for i in range (4): 
    for j in range(4):
        #atribui a variavel media a soma dos elementos da matriz
        Soma = Soma + matriz[i] [j]

print(Soma)


#Questao 4

#Consulta os valores das posicoes da diagonal 
nu1 = matriz[0][0]
nu2 = matriz[1][1]
nu3 = matriz[2][2]
nu4 = matriz[3][3]

#faz o produto dos elemntos selecionados 

Resultado = nu1 * nu2 * nu3 * nu4
print(Resultado)