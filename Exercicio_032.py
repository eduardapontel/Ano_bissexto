from datetime import date

bordas = '\033[037m-=-\033[m' * 12
print(bordas)
print('{:^35}'.format('ANALISE DE ANO BISSEXTO'))
print(bordas)
print()

ano = ''

while type(ano) != int:
    try:
        ano = int(input('Digite um ano para verificar se é bissexto [0 -> ano atual]: '))
    except:
        print('Por favor digite um valor válido!')

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO!'.format(ano))
else:
    print('O ano {} não é BISSEXTO'.format(ano))
