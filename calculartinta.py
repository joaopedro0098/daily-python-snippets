# Aqui iremos calcular a quantidade de latas necessárias para pintar uma área assim como o valor que será gasto


# 1 - Aqui pegaremos a área em questão
def pegar_area_usuario():
    area = int(input("Qual a área a ser pintada (m²): "))
    return area

# 2 - Considerando que 1L de tinta faz 6m², dividiremos a área por 6 para saber quantos litros precisar
def calcular_litros_precisamos(area):
    litros = area / 6
    return litros
    
'''3 - Aqui calcularemos a quantidade de latas necessárias considerando que uma lata possui 18L. Além disso
       se a quantidade de latas der número quebrado (o que não prática é possível) o sistema adicionará mais uma lata
       para que tenha tinta o suficiente'''
def calcular_latas(litros):
    latas = litros / 18
    if int(latas) != latas:
        latas = int(latas) + 1
    return latas

# 4 - Considerando que o preço da lata é R$250, calcularemos o preço total 
def calcular_preco(latas):
    preco = latas * 250
    return preco
    

# 5 - Armazenei as funções em variáveis
area = pegar_area_usuario()
litros = calcular_litros_precisamos(area)
latas = calcular_latas(litros)
preco = calcular_preco(latas)


# 6 - chamei as funções armazenadas nas variaveis
print("Quantidade de latas ", latas)
print("Preço: ", preco)