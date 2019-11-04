# Guard the wrong layout.
# Developer - Mazenkov A.
import dictionary as dt

print('Введите текст, который нужно исправить'.center(100, '-'))
text = input()
check = text.replace(' ', '')

while not check.isalnum():
    print('Ошибка. Попробуйте еще раз.'.center(100, '-'))
    print('Введите текст, который нужно исправить'.center(100, '-'))
    text = input()

text = text.capitalize().lstrip()

if text[0] in dt.dict_EN:
    print('English'.center(100, '-'))

elif text[0] in dt.dict_RU:
     print('Русский'.center(100, '-'))
