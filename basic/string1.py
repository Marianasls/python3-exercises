#!/usr/bin/python3 -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Exercícios básicos com string
# Preencha o código das funções a seguir. main() está configurado
# para chamar com várias entradas diferentes,
# mostrando 'OK' quando cada função está correta.
# O código inicial para cada função inclui um 'return'
# que é só uma indicação onde seu código vai terminar.
# Tudo bem se você não completar todas as funções. Há mais
# funções adicionais para tentar no arquivo string2.py.


# A. donuts
# Dado um inteiro com o número de donuts, retorna uma string
# do formato 'Number of donuts: <count>', onde <count> é o número
# passado como entrada. Entretanto, se a número é 10 ou maior, então use a palavra 'many'
# no lugar do número.
# Por exemplo, donuts(5) retorna 'Number of donuts: 5'
# e donuts(23) retorna 'Number of donuts: many'
def donuts(count):
  # +++seu código aqui+++
  return


# B. both_ends
# Dado uma string s, retorna uma string feita com as duas primeiras
# e as duas últimas letras da string original,
# então 'spring' retorna 'spng'. Entretanto, se o cumprimeito da string
# é menor que 2, retorne uma string vazia.
def both_ends(s):
  # +++seu código aqui+++
  return


# C. fix_start
# Dado uma string s, retorne uma string
# onde todas as ocorrências da primeira letra é alterada
# para '*', exceto a primeira letra da string.
# por exemplo, 'babble' retorna 'ba**le'
# Assuma que a string tem tamanho 1 ou maior.
# Dica: s.replace(stra, strb) retorna uma versão da string s
# onde todas as instâncias de stra são substituídas por strb.
def fix_start(s):
  # +++seu código aqui+++
  return


# D. MixUp
# Dado as strings a e b, retorne uma única string com a e b separados
# por um espaço '<a> <b>', exceto trocando as 2 primeiras letras de cada string.
# e.g.
#   'mix', pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Assuma a e b tem tamanho 2 ou maior.
def mix_up(a, b):
  # +++seu código aqui+++
  return


# Provê uma função simples test() usada em main() para mostrar
# o que cada função retorna vs o que deveria retornar.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print(('%s got: %s expected: %s' % (prefix, repr(got), repr(expected))))


# Função main() chama as outras funções com várias entradas,
# usando test() para verificar se cada resultado está correto ou não.
def main():
  print('donuts')
  
  test(donuts(4), 'Number of donuts: 4')
  test(donuts(9), 'Number of donuts: 9')
  test(donuts(10), 'Number of donuts: many')
  test(donuts(99), 'Number of donuts: many')

  print()
  print('both_ends')
  test(both_ends('spring'), 'spng')
  test(both_ends('Hello'), 'Helo')
  test(both_ends('a'), '')
  test(both_ends('xyz'), 'xyyz')

  
  print()
  print('fix_start')
  test(fix_start('babble'), 'ba**le')
  test(fix_start('aardvark'), 'a*rdv*rk')
  test(fix_start('google'), 'goo*le')
  test(fix_start('donut'), 'donut')

  print()
  print('mix_up')
  test(mix_up('mix', 'pod'), 'pox mid')
  test(mix_up('dog', 'dinner'), 'dig donner')
  test(mix_up('gnash', 'sport'), 'spash gnort')
  test(mix_up('pezzy', 'firm'), 'fizzy perm')


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()
