# Guard the wrong keyboard layout.
# Developer - Mazenkov A.
import dictionary as dt

while True:

    print('Введите текст, который нужно исправить'.center(100, '-'))
    text = input()

    check = ''
    for _ in range(len(text)):
        check += text[_]
        if text[_] in dt.symbol:
            check = check.replace(text[_], '')

    while not check.isalpha():
        print('Ошибка. Попробуйте еще раз.'.center(100, '-'))
        print('Введите текст, который нужно исправить'.center(100, '-'))
        text = input()
        check = ''
        for _ in range(len(text)):
            check += text[_]
            if text[_] in dt.symbol:
                check = check.replace(text[_], '')

    text = text.upper().lstrip()

    if text[0] in dt.dict_EN:
        letter_ru = ''
        for i in range(len(text)):
            letter_en = dt.dict_EN[text[i]]
            letter_ru += dt.dict_ru[letter_en]
        print(letter_ru.capitalize())

    elif text[0] in dt.dict_RU:
        letter_en = ''
        for i in range(len(text)):
            letter_ru = dt.dict_RU[text[i]]
            letter_en += dt.dict_en[letter_ru]
        print(letter_en.capitalize())

    print('Повторить ещё раз? (y/n)'.center(100, '-'))
    cont = input()
    if cont == 'n':
        break
