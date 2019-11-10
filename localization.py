print('Choose the language (ru, en)'.center(100, '-'))
print('RU - Русский'.center(100, '-'))
print('EN - English'.center(100, '-'))
lang_choose = input()

while lang_choose.lower() != 'ru' and lang_choose.lower() != 'en':
    print('You have selected an unsupported language'.center(100, '-'))
    print('Try again'.center(100, '-'))
    lang_choose = input()

if lang_choose.lower() == 'ru':
    start_message = 'Введите текст, который нужно исправить'
    error_message = 'Ошибка. Попробуйте еще раз'
    correct_layout = 'Вы ввели текст на корректной раскладке. Исправление не требуется'
    try_again = 'Повторить ещё раз? (y/n)'

elif lang_choose.lower() == 'en':
    start_message = 'Enter the text you want to correct'
    error_message = 'Mistake. Try again'
    correct_layout = 'You entered the text in the correct layout. No correction required'
    try_again = 'To repeat again? (y/n)'

