# SISTEMA DE AMORTIZAÇÃO CONSTANTE
cont = 1
pv = float(input('Digite o valor do pv: '))
n = int(input('Digite o número de parcelas: '))
jam = float(input('Taxa de juros a.m: '))
jam = jam / 100
amtz = pv / n
while cont < n + 1:
    juros = pv * jam
    parcela = amtz + juros
    pv = pv - amtz
    valor_juros = "R${:,.2f}".format(juros).replace(",", "X").replace(".", ",").replace("X", ".")
    valor_prc = "R${:,.2f}".format(parcela).replace(",", "X").replace(".", ",").replace("X", ".")
    valor_pv = "R${:,.2f}".format(pv).replace(",", "X").replace(".", ",").replace("X", ".")
    valor_amtz = "R${:,.2f}".format(amtz).replace(",", "X").replace(".", ",").replace("X", ".")
    print(
        'N {} | Amortização: {} | Valor da parcela: {} | Valor do juros: {} | Divida restante: {}'.format(
            cont, valor_amtz, valor_prc, valor_juros, valor_pv))
    cont += 1