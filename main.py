# Guard the wrong keyboard layout.
# Developer - Mazenkov A.
import dictionary as dt
import localization as lc
import langdetect as ldect

while True:

    print(lc.start_message.center(100, '-'))
    text = input()

    check = ''
    for _ in range(len(text)):                                                 # Verification of input data.
        check += text[_]
        if text[_] in dt.symbol:
            check = check.replace(text[_], '')

    while not check.isalpha():                                                 # If unsupported characters are entered.
        print(lc.error_message.center(100, '-'))
        print(lc.start_message.center(100, '-'))
        text = input()
        check = ''
        for _ in range(len(text)):
            check += text[_]
            if text[_] in dt.symbol:
                check = check.replace(text[_], '')

    text = text.upper().lstrip()

    if text[0] in dt.dict_EN:                                                  # If Latin characters are entered.
        letter_ru = ''
        if ldect.detect(text) == 'en':                                         # If the text is typed correctly.
            print(lc.correct_layout.center(100, '-'))
            continue

        for i in range(len(text)):
            letter_en = dt.dict_EN[text[i]]
            letter_ru += dt.dict_ru[letter_en]
        print(letter_ru.capitalize())

    elif text[0] in dt.dict_RU:                                                # If Cyrillic characters are entered.
        letter_en = ''
        for i in range(len(text)):
            letter_ru = dt.dict_RU[text[i]]
            letter_en += dt.dict_en[letter_ru]
        if ldect.detect(letter_en) != 'en':                                    # If the text is typed correctly.
            print(lc.correct_layout.center(100, '-'))
            continue
        print(letter_en.capitalize())

    print(lc.try_again.center(100, '-'))                                       # Repeat the program or not.
    cont = input()
    if cont == 'n':
        break
