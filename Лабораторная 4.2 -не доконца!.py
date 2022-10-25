def get_count_char(str_):
    clear_str = "".join(a for a in str_ if a.isalpha())
    clear_str = clear_str.lower()
    def_count = 0
    dict = {}
    for i in clear_str:
        #if str_.isalpha() is True:
        dict[i] = dict.get(i, def_count) + 1
        x = dict

    return x



main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))

#Функция должна вернуть новый словарь,
#где количество каждого элемента заменено на процентное
# отношение ко всем символам.