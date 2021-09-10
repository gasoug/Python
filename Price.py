# SISTEMA DE FRANCÊS
pv = float(input('Digite o valor do pv: '))
n = int(input('Digite o número de parcelas: '))
jam = float(input('Taxa de juros a.m: '))
jam = jam / 100
cont = 1
pmt = pv/((((1 + jam)**n)-1)/(((1 + jam)**n)*jam))
while cont <= n:
    juros = jam * pv
    amtz = pmt - juros
    pv = pv - amtz
    valor_juros = "R${:,.2f}".format(juros).replace(",", "X").replace(".", ",").replace("X", ".")
    valor_pmt = "R${:,.2f}".format(pmt).replace(",", "X").replace(".", ",").replace("X", ".")
    valor_pv = "R${:,.2f}".format(pv).replace(",", "X").replace(".", ",").replace("X", ".")
    valor_amtz = "R${:,.2f}".format(amtz).replace(",", "X").replace(".", ",").replace("X", ".")
    print(
        'TABELA PRICE\n|N {} | Saldo Devedor: {} | Amortização: {} | Valor do juros: {} | Parcela: {}'.format(
            cont, valor_pv, valor_amtz, valor_juros, valor_pmt))
    cont += 1
