alunos = []
alunos.append(
    {'nome': 'Aluno 01', 'curso': 'Ciências da Computação', 'AV1': 8})
alunos.append(
    {'nome': 'Aluno 02', 'curso': 'Sistemas de Informação', 'AV1': 7})
alunos.append(
    {'nome': 'Aluno 03', 'curso': 'Sistemas de Informação', 'AV1': 6})
alunos.append(
    {'nome': 'Aluno 04', 'curso': 'Sistemas de Informação', 'AV1': 6})
alunos.append(
    {'nome': 'Aluno 05', 'curso': 'Sistemas de Informação', 'AV1': 6})
alunos.append(
    {'nome': 'Aluno 06', 'curso': 'Análise e Desenvolvimento de Sistemas', 'AV1': 7})
alunos.append(
    {'nome': 'Aluno 07', 'curso': 'Análise e Desenvolvimento de Sistemas', 'AV1': 9})
alunos.append(
    {'nome': 'Aluno 08', 'curso': 'Ciências da Computação', 'AV1': 10})
alunos.append(
    {'nome': 'Aluno 09', 'curso': 'Ciências da Computação', 'AV1': 10})
alunos.append(
    {'nome': 'Aluno 10', 'curso': 'Ciências da Computação', 'AV1': 4})
alunos.append(
    {'nome': 'Aluno 11', 'curso': 'Análise e Desenvolvimento de Sistemas', 'AV1': 5})
alunos.append(
    {'nome': 'Aluno 11', 'curso': 'Análise e Desenvolvimento de Sistemas', 'AV1': 5})
alunos.append(
    {'nome': 'Aluno 12', 'curso': 'Análise e Desenvolvimento de Sistemas', 'AV1': 9})
alunos.append(
    {'nome': 'Aluno 13', 'curso': 'Análise e Desenvolvimento de Sistemas', 'AV1': 9})
alunos.append(
    {'nome': 'Aluno 14', 'curso': 'Ciências da Computação', 'AV1': 7})
alunos.append(
    {'nome': 'Aluno 15', 'curso': 'Análise e Desenvolvimento de Sistemas', 'AV1': 7})
alunos.append(
    {'nome': 'Aluno 16', 'curso': 'Ciências da Computação', 'AV1': 6})
alunos.append(
    {'nome': 'Aluno 17', 'curso': 'Análise e Desenvolvimento de Sistemas', 'AV1': 8})
alunos.append(
    {'nome': 'Aluno 18', 'curso': 'Ciências da Computação', 'AV1': 4})
alunos.append(
    {'nome': 'Aluno 19', 'curso': 'Sistemas de Informação', 'AV1': 2})
alunos.append(
    {'nome': 'Aluno 20', 'curso': 'Análise e Desenvolvimento de Sistemas', 'AV1': 9})

cursos = {}
notas = []

for aluno in alunos:
   

    for chave, valor in aluno.items():
        
       

    
        if chave == 'curso':
            cursos.update({valor: notas})

for curso in cursos:
    notas = []
    for aluno in alunos:
        for chave, valor in aluno.items():
            if valor == curso:
                notas.append(aluno.get('AV1'))

    cursos.update({curso: notas})
   




for curso in cursos:
  notaCurso = cursos.get(curso)
  tamanho = len(notaCurso)
  media = 0 
  print('Curso...: ',curso)
  print(notaCurso)
  


  maior = menor = notaCurso[0]
  for i in range(0, tamanho):
    media += notaCurso[i]
    if notaCurso[i] > maior:
      maior = notaCurso[i]
    if notaCurso[i] < menor:  
      menor = notaCurso[i]

  print('A MENOR nota é: ', menor)


  print('A MAIOR nota é: ', maior)
  print(f'A Média: {media / tamanho :.2f}')
  print('--------------------------')