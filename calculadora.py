
def linha (tam = 90):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(90))
    print(linha())



print(linha())
cabeçalho('CALCULADORA - DIVULGA TUDO')
print(linha())

while True:
    valorInv = ''
    print('ATENÇÃO: use ponto para digitar o valor desejado exemplo: 25.00 (vinte e cinco reais)')
    valorInv = float(input('Informe a seguir o valor que deseja investir na divulgação do seu anúncio: R$ ' + valorInv))
    print(linha())

    vizSemComp = float(valorInv * 30)
    cliques = int(vizSemComp * 0.12)
    comp = int(cliques * 0.15) + 4 #4 COMPARTILHAMENTOS EM SEQUENCIA
    vizComp = int(comp * 40)
    vizuTotal = int(vizSemComp + vizComp + ( 4 * 40 ))#VIZUALIZAÇÕES DOS COMPARTILHAMENTOS EM SEQUENCIA  
    print('Quantidade aproximada de vizualizações: ' + str(vizuTotal))   
    print(linha())
    break



