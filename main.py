s = input()
print(s[2])
print(s[-2])
print(s[:5])
print(s[:-2])
print(s[0:-2])
print(s[1::2])
print(s[::-1])
print(s[::-2])
print(len(s))

s = input()
print(s.count(' ')+ 1)


s = input()
print(s[(len(s) + 1) // 2:] + s[:(len(s) + 1) // 2])


s = input()
a = s.find('f')
b = s.rfind('f')
print(a,b)


s = input()
s = s[:s.find('h')] + s[s.rfind('h') + 1:]
print(s)


print(input().replace('1', 'one'))


print(input().replace('@', ''))

s = input()
a = s[:s.find('h') + 1]
b = s[s.find('h') + 1:s.rfind('h')]
c = s[s.rfind('h'):]
s = a + b.replace('h', 'H') + c
print(s)

