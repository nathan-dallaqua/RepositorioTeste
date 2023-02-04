#teste de python no visual studio code
notas=[]
cont=[]
while True:
    nota=float(input('Digite a nota do aluno: '))
    notas.append(nota)
    cont+=1
    pergunta=str(input('Deseja continuar? S/N: ')).upper()
    if pergunta in 'Nn':
        break
media= sum(notas) / cont
print(f'A média do aluno foi {media}')
