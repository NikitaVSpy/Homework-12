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
          'office', 'qt', 'pyqt', 'java', 'c+', 'c#', 'experience', 'r', 'pandas', 'numpy']

dict = {}
for i in result:
    dict[i] = result.count(i)

list = list(dict.items())

for i in range(len(list)):
    if list[i][0] in skills:
       print(f'встречаемость:{list[i]}, т.е. в {round(list[i][1]*100/quantity_vacancies, 2)} % вакансий')
