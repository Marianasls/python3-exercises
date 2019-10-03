def verbing(s):
    t = len(s)
    if(t < 3): return s
    nova = s + 'ly' if(s[t-3:t] == 'ing') else s + 'ing'

    return nova

def not_bad(s):
    a = s.find('not')
    b = s.find('bad')
    return s.replace(s[a:], 'good') + s[b+3:] if a < b else s  

def front_back(aa, bb):
    a = len(aa)
    b = len(bb)
    frontA = int(a/2) if a%2 == 0 else int(a/2 +1)
    backA = int(a/2)

    frontB = int(b/2) if b%2 == 0 else int(b/2 +1)
    backB = int(b/2)
    return aa[0:frontA] + bb[0:frontB] + aa[a-backA:] + bb[b-backB:]
#a-front + b-front + a-back + b-back

def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))

def main():
  print('verbing')
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')

  print()
  print('not_bad')
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")

  print()
  print('front_back')
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')


if __name__ == '__main__':
  main()
