
word = input("Введите слово из маленьких латинских букв: ")

# Cчетчики для гласных букв
count_a = word.count('a')
count_e = word.count('e')
count_i = word.count('i')
count_o = word.count('o')
count_u = word.count('u')

if count_a > 0 or count_e > 0 or count_i > 0 or count_o > 0 or count_u > 0:
    print(f'Количество букв "a": {count_a}')
    print(f'Количество букв "e": {count_e}')
    print(f'Количество букв "i": {count_i}')
    print(f'Количество букв "o": {count_o}')
    print(f'Количество букв "u": {count_u}')
else:
    print('False')


vowels = count_o + count_i + count_e + count_a + count_u
consonants = 26 - vowels

print('Гласные =', vowels)
print('Согласные =', consonants)