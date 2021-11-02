import requests
from bs4 import BeautifulSoup
from tkinter import Tk, Button, Label


# Сохраняем адреса страниц, с которых будем собирать информацию
url1 = 'https://pythonru.com/'
url2 = 'https://pythonist.ru/category/topnews/'
url3 = 'https://pythondigest.ru/'


# Создаем запросы на сайты с помощью метода get библиотеки requests
# Результат запроса сохраняется в переменную response
response1 = requests.get(url1)
response2 = requests.get(url2)
response3 = requests.get(url3)


# Используем BeautifulSoup для получения текста ответа
soup1 = BeautifulSoup(response1.text, 'lxml')
soup2 = BeautifulSoup(response2.text, 'lxml')
soup3 = BeautifulSoup(response3.text, 'lxml')


# Находим статьи на сайтах с их ссылками
articles1 = soup1.find_all('h3', class_='entry-title td-module-title')
articles2 = soup2.find_all('h2', class_='entry-title')
articles3 = soup3.find_all('a', class_='issue-item-title')


# Создаем списки статей каждого сайта
article_list1 = []
for article in articles1:
    article_list1.append(article.text)

article_list2 = []
for article in articles2:
    article_list2.append(article.text)

article_list3 = []
for article in articles3:
    article_list3.append(article.text)

# Создаем списки ссылок
link_list1 = []
for article in articles1:
    link_list1.append(article.a.get('href'))

link_list2 = []
for article in articles2:
    link_list2.append(article.a.get('href'))

link_list3 = []
for article in articles3:
    link_list3.append(article.get('href'))


# Создаем словари статей и ссылок на них
article_list_dict1 = dict(zip(article_list1, link_list1))
article_list_dict2 = dict(zip(article_list2, link_list2))
article_list_dict3 = dict(zip(article_list3, link_list3))


def output_func():
    '''Функция выводит статьи и ссылки к ним.'''

    print('PythonRu')
    print()
    # С сайта 'PythonRu'
    for article, link in article_list_dict1.items():
        print(article + ' -> ' + link)

    print()
    print('PYTHONIST')
    print()
    # С сайта 'PYTHONIST'
    for article, link in article_list_dict2.items():
        print(article, '->', link)

    print()
    print('Python Дайджест')
    print()
    # С сайта 'Python Дайджест'
    for article, link in article_list_dict3.items():
        print(article, '->', link)


# Создаем окно программы
window = Tk()
# Заголовок программы
window.title('Parser python sites')
# Размер окна программы
window.geometry('650x80')
# Задаем цвет окна
window['bg'] = 'PaleGreen1'

# Делаем надпись
lb = Label(window, text='Программа показывает последние статьи и ссылки на них'
                        'с сайтов "PythonRU", "PYTHONIST", "Python Дайджест".')
# Расположение надписи
lb.place(x=10, y=10)
# Цвет надписи
lb['bg'] = 'PaleGreen1'

# Кнопка для запуска программы
btn = Button(window, text='Поиск статей', height=2, width=20, command=output_func)
# Расположение кнопки
btn.place(x=255, y=35)
# Цвет кнопки
btn['bg'] = 'aquamarine'

# Бесконечный цикл для отображения окна программы
window.mainloop()

