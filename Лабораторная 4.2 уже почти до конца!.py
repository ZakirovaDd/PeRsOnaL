#dict= {}
def get_count_char(str_):
    clear_str = "".join(a for a in str_ if a.isalpha())
    clear_str = clear_str.lower()
    def_count = 0
    dict = {}
    for i in clear_str:
        dict[i] = dict.get(i, def_count) + 1
        x = dict

    return x

def prozent_bukv(dict):
    #dict = {'д': 13, 'а': 18, 'н': 13, 'о': 29, 'е': 23, 'п': 9, 'р': 13, 'л': 16, 'ж': 2, 'и': 14, 'б': 5, 'у': 5, 'т': 18, 'з': 2, 'в': 14, 'ь': 6, 'с': 16, 'я': 4, 'ы': 5, 'к': 6, 'ч': 2 , 'г': 1, 'м': 8, 's': 1, 'p': 1, 'l': 1, 'i': 2, 't': 1, 'х': 3, 'ф': 1, 'щ': 1, 'ю': 1, 'j': 1, 'o': 1, 'n': 1}
    dict = get_count_char(dict)
    key = []
    value = []
    for key, value in dict.items():
        DEF_COUNT = sum(dict.values())
        value_1 = (value / DEF_COUNT)*100
        #print(key, value_1, "%")
        print(f'Буква "{key}" в процентном соотношении составляет {round(value_1,1)} %')
       #я понимаю что на выходе не словарь поучаем, но я если честно не совсем поняла, как сделать словарь)

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
prozent_bukv(main_str)

