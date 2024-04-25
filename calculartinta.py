# Aqui iremos calcular a quantidade de latas necessárias para pintar uma área assim como o valor que será gasto

# - Aqui pegaremos a área em questão
def pegar_area_usuario():
    area = int(input("Informe a área (M²) a ser pintada: "))
    return area

# - Pegaremos quanto a tinta faz por litro
def rendimento_tinta(): 
    rendimento = int(input("Informe quantos M² essa tinta faz por litro: "))
    return rendimento

# - Pediremos o valor da lata que ele deseja comprar
def valor_da_lata(): 
    valor = float(input("Informe o valor da lata: "))
    return valor

# - Considerando que 1L de tinta faz 6m², dividiremos a área por 6 para saber quantos litros precisar
def calcular_litros_precisamos(area, rendimento):
    litros = area / rendimento
    return litros

'''- Aqui calcularemos a quantidade de latas necessárias considerando que uma lata possui 18L. Além disso
       se a quantidade de latas der número quebrado (o que não prática é possível) o sistema adicionará mais uma lata
       para que tenha tinta o suficiente'''
def calcular_latas(litros):
    latas = litros / 18
    if int(latas) != latas:
        latas = int(latas) + 1
    return latas

# - Considerando que o preço da lata é R$250, calcularemos o preço total
def calcular_preco(latas, valor):
    preco = latas * valor
    return preco



# - Armazenei as funções nas variáveis
area = pegar_area_usuario()
rendimento = rendimento_tinta ()
valor = valor_da_lata()
litros = calcular_litros_precisamos(area, rendimento)
latas = calcular_latas(litros)
preco = calcular_preco(latas, valor)

# - mandei printar na tela
print("-----------------------------------------")
print("- Você precisará de", latas, "lata(s)")
print("- O valor a pagar será: R$", preco)
