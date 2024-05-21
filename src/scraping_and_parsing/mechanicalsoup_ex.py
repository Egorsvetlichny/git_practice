# Для имитации действий пользователя при скрапинге часто используют Selenium,
# однако есть и более легкое решение – библиотека MechanicalSoup.
# MechanicalSoup исполняет роль браузера без графического интерфейса. Помимо имитации нужного взаимодействия с
# элементами страниц, MechanicalSoup также парсит HTML-код, используя для этого все функции BeautifulSoup.

# Использование MechanicalSoup для отправки формы заказа пиццы.

import mechanicalsoup

url = 'http://httpbin.org/'
browser = mechanicalsoup.StatefulBrowser()
browser.open(url)
browser.follow_link('forms')
browser.select_form('form[action="/post"]')
print(browser.form.print_summary())

print()

# Имитация заполнения полей формы
browser["custname"] = "Egor"
browser["custtel"] = "88888888888"
browser["custemail"] = "svetlichal@mail.ru"
browser["size"] = "large"
browser["topping"] = ("cheese", "mushroom", "bacon", "onion")
browser["comments"] = "Please do it faster, i'm very hungry"

response = browser.submit_selected()
print(response.text)
