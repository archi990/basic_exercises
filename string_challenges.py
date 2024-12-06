# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'

vowels = 'аеёиоуыэюя'
count = 0
for char in word.lower():
    if char in vowels:
        count += 1 
print(count)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
words = sentence.split()
num_words = len(words)
print(num_words)

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
words = sentence.split()
for word in words:
    print(word[0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
char_cnt=0
words = sentence.split()
words_cnt = len(words)
for word in words:
    char_cnt += len(word)
avg_word_len = round(char_cnt/words_cnt, 2)
print(avg_word_len)