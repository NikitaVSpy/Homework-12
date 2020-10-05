import requests
import string

URL = 'https://api.hh.ru/vacancies'
params = {'text': 'Python',
          'city': 'Москва',
          'only_with_salary': True,
          'per_page': 100}

response = requests.get(URL, params=params).json()
pages = response['pages']
quantity_vacancies = response['found']
result = ''

for page in range(pages):
    params = {'text': 'Python',
              'city': 'Москва',
              'only_with_salary': True,
              'page': page}

    response = requests.get(URL, params=params).json()

    for item in response['items']:
        snippet = item['snippet']
        requirement = snippet['requirement']
        responsibility = snippet['responsibility']
        result += str(requirement)
        result += str(responsibility)

for punct in string.punctuation:
    result = result.replace(punct, ' ')
result = result.lower()
result = result.split()

skills = ['python', 'sql', 'git', 'linux', 'javascript', 'django', 'hive', 'sas', 'scrum', \
          'aosp', 'unix', 'ruby', 'php', 'nodejs', 'matlab', 'frontend', 'backend', 'web', \
          'office', 'qt', 'pyqt', 'java', 'c+', 'c#', 'r', 'pandas', 'numpy']

dict = {}
for i in result:
    dict[i] = result.count(i)

list = list(dict.items())

#Функция сортировки по второму элементу
def sort_count(inputStr):
    return inputStr[1]

list = sorted(list, key=sort_count, reverse=True)


n = 1
print('Топ 10 навыков профессии и процент их встречаемости:')

for i in range(len(list)):
    if list[i][0] in skills:
       print(f'{n}) {list[i][0].capitalize()}: встречаемость: в {round(list[i][1]*100/quantity_vacancies, 2)} % вакансий')
       n += 1
    if n == 11:
        break
