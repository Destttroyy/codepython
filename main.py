import os
print("Привет! Это программа-объяснялка мемов.")

meme_dict = {
    "КРИНЖ": "Что-то очень странное или стыдное",
    "ЛОЛ": "Что-то очень смешное",
    "РОФЛ": "Шутка",
    "ЩИЩ": "Одобрение или восторг",
    "КРИПОВЫЙ": "Страшный, пугающий",
    "АГРИТЬСЯ": "Злиться"
}

for _ in range(5):
    word = input("Введите непонятное слово (большими буквами!): ")

    
    if word in meme_dict:
        print("Значение слова '{}': {}".format(word, meme_dict[word]))
    else:
        new_definition = input("Значение для слова '{}' не найдено. Введите его значение: ".format(word))
        meme_dict[word] = new_definition
        print("Слово '{}' добавлено в словарь с значением '{}'.".format(word, new_definition))


    
    input("Нажмите Enter, чтобы продолжить...")

    os.system('cls' if os.name == 'nt' else 'clear')


print("Спасибо за использование программы-объяснялки мемов!")
