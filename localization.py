print('Choose the language (ru, en, cn, fr)'.center(100, '-'))
print('RU - Русский '.center(100, '-'))
print('EN - English'.center(100, '-'))
print('CN - 中文'.center(98, '-'))
print('FR - Français'.center(100, '-'))
lang_choose = input()

if lang_choose.lower() == 'ru':
    start_message = 'Введите текст, который нужно исправить'
    error_message = 'Ошибка. Попробуйте еще раз'
    try_again = 'Повторить ещё раз? (y/n)'

elif lang_choose.lower() == 'en':
    start_message = 'Enter the text you want to correct'
    error_message = 'Mistake. Try again'
    try_again = 'To repeat again? (y/n)'

elif lang_choose.lower() == 'cn':
    start_message = '输入要更正的文本'
    error_message = '错误 再试一次'
    try_again = '再重复一次？ (y/n)'

elif lang_choose.lower() == 'fr':
    start_message = 'Saisissez le texte à corriger'
    error_message = 'Erreur. Essayez à nouveau'
    try_again = 'Répéter encore une fois? (y / n)'
