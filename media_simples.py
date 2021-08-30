nome = input('Nome do Aluno: ')
nt1 = float(input('Primeira nota: '))
nt2 = float(input('Segunda nota: '))
nt3 = float(input('Terceira nota: '))
nt4 = float(input('Quarta nota: '))
media = (nt1+nt2+nt3+nt4) / 4
if media <= 7:
    print('O aluno(a) {}'.format(nome), 'obteve a média de: ', media, 'e foi reprovado(a)!')
else:
    print('O aluno(a) {}'.format(nome), 'obteve a média de: ', media, 'e foi aprovado(a)!')

