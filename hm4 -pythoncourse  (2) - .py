# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

my_list = [1, 2, 4, 0]
sq_list = [a ** 2 for a in my_list]
print(sq_list)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruit_list = ['банан', 'апельсин', 'яблоко', 'груша']
another_list = ['киви', 'банан', 'персик', 'яблоко']
sort_list = list (set (fruit_list) & set (another_list))
print(sort_list)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

my_list = [1, 2, 4, 9, 0, -3, 16, -23, -9]
sort_list = [el for el in my_list if el % 3 == 0 and el >=0 and el % 4 !=0]
print(sort_list)

Normal 1 
Вывести символы в нижнем регистре, которые окружают 1 или более символа в верхнем регистре.
Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
Решить задачу двумя способами: с помощью re и без.
=================================================================================================================
"""

import re

line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalp' \
       'PLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzKTUfSYtBydXaVIpxWjNKgXANv' \
       'IoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkp' \
       'YOlqXEFIxPqqqgAWdJsOvqppOfyIVjXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSA' \
       'fJMchgBWAsGnBnWetekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAb' \
       'fCvzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXbJrwTRNyA' \
       'xDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCCEUZShGofaFpuespaZWLFN' \
       'IsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUf' \
       'lwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZC' \
       'nZjLeMiFlxnPkqfJFbCfKCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxy' \
       'GPvbnhWHuXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFaXi' \
       'UWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'


# 1st option: for xxAAAyyy

print("1st option:")
regx = re.compile(r'([a-z]+)[A-Z]+([a-z])')
result = regx.findall(line)
print(result)


# 2nd option: for AAxxBByyCCCzzzRRR

print("2nd option:")
regx = re.compile(r'(?<=[A-Z]{1})[a-z]+(?=[A-Z]+)')
result = regx.findall(line)
print(result)


# 3rd option: for xxAAAyyy without 're'

print("3rd option:")
b = []
a = str()
for i in line:
    if i.islower():
        a += i
    else:
        b.append(a)
        a = str()
for j in b:
    b.remove('')
print(b)



# Задача-3 normal :
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла) произвольными целыми
# числами, в результате в файле должно быть 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр в вышезаполненном файле.



import random
import re
 
n = (random.randint(0, 9) for i in range(2500)) 
str = ''.join(str(i) for i in n) 
 
with open('test.txt', 'w', )  as f: 
    f.write(str) 
    found = re.findall(r'[0-9]', str)
    print(found)

	
# Задание-2 hard:
# Найдите наибольшее произведение пяти последовательных цифр в 1000-значном числе.
# Выведите произведение и индекс смещения первого числа последовательных 5-ти цифр.
# Пример 1000-значного числа:
number = """
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450"""

