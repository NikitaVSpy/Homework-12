import requests

URL = 'https://www.cbr-xml-daily.ru/daily_json.js'
response = requests.get(URL).json()

usd_value = response['Valute']['USD']['Value']
euro_value = response['Valute']['EUR']['Value']


URL = 'https://api.hh.ru/vacancies'
params = {'text': 'Python',
          'city': 'Москва',
          'only_with_salary': True,
          'per_page': 100}

response = requests.get(URL, params = params).json()
pages = response['pages']

min_salary = []
max_salary = []

for page in range(pages):
    params = {'text': 'Python',
              'city': 'Москва',
              'only_with_salary': True,
              'page': page}

    response = requests.get(URL, params = params).json()

    for item in response['items']:
        salfrom = item['salary']['from']
        salto = item['salary']['to']
        salcurr = item['salary']['currency']

        if salcurr == 'RUR':
            if salfrom is not None:
                min_salary.append(salfrom)
            if salto is not None:
                max_salary.append(salto)

        elif salcurr == 'USD':
            if salfrom is not None:
                min_salary.append(int(salfrom * usd_value))
            if salto is not None:
                max_salary.append(int(salto * usd_value))

        elif salcurr == 'EUR':
            if salfrom is not None:
                min_salary.append(int(salfrom * euro_value))
            if salto is not None:
                max_salary.append(int(salto * euro_value))

print(f'Средняя з/п разработчиков по запросу Python в Москве \
от {sum(min_salary) // len(min_salary)} \
до {sum(max_salary) // len(max_salary)} RUR')

