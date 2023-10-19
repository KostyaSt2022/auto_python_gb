"""
Часто встречающиеся слова
В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых.
Не учитывать знаки препинания и регистр символов.
Слова разделяются пробелами, апостроф не считается за пробел.
Такие слова как dont, its, didnt итд (после того, как убрали знак препинания апостроф) считать одним словом.
*Пример*
На входе:
text = 'Hello world. Hello Python. Hello again.'

На выходе:
[('hello', 3), ('world', 1), ('python', 1), ('again', 1)]
"""
# # Решение №1:
# import re
# from collections import Counter
#
# text = 'Hello world. Hello Python. Hello again.'
#
#
# def top_10_words(text):
#     words = re.findall(r'\b\w+\b', text.lower())
#     return Counter(words).most_common(10)
#
#
# print(top_10_words(text))



# Решение №2:
import re
from collections import Counter

text = "Python 3.9 is the latest version of Python. It's awesome!"

# Удаляем знаки препинания и приводим текст к нижнему регистру
cleaned_text = ''.join(char.lower() if char.isalpha() or char.isspace() else ' ' for char in text)

# Разбиваем текст на слова и считаем их количество
words = cleaned_text.split()
word_counts = {}

for word in words:
    if word not in word_counts:
        word_counts[word] = 1
    else:
        word_counts[word] += 1

# Получаем 10 самых часто встречающихся слов
top_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:10]

print(top_words)