########O.K
def donuts(count):
    s = 'Number of donuts: '
    return s + str(count) if count < 10 else s + 'many'
# str() converte número em string 
    
########O.K
def both_ends(s):
    return '' if len(s) < 2 else s[0:2] + s[len(s)-2:]  
# Ex: s = banana retorna bana

########O.K
def fix_start(s):
    return s[0] + s[1:].replace(s[0], '*')

########O.K
def mix_up(a,b):
    return a.replace(a[0:2], b[0:2]) + ' ' + b.replace(b[0:2], a[0:2])
    

def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print(('%s got: %s expected: %s' % (prefix, repr(got), repr(expected))))

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

if __name__ == '__main__':
  main()

