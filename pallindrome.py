s = input('Enter a string: ')

rev = ""
for i in s:
    rev = i + rev
if rev.upper() == s.upper():
    print('Pallindrome')
else:
    print('No')