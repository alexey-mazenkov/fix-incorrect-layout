# Guard the wrong layout.
# Developer - Mazenkov A.

print('Введите текст, который нужно исправить'.center(100, '-'))
text = input()

while not text.isalnum():
     print('Ошибка. Попробуйте еще раз.'.center(100, '-'))
     print('Введите текст, который нужно исправить'.center(100, '-'))
     text = input()
