# Описание проекта scrapy_parser_pep:

Учебный проект парсинга документации Python:
- главная страница c информацией о PEP (https://peps.python.org/)
- парсинг страниц с документами, ссылки на которые получены с главной страницы

### Используемые технологии:

Python 3.7, Scrapy 2.5.1

### Как запустить проект:
Клонировать репозиторий, перейти в него в командной строке:
```
git clone https://github.com/olegtsss/scrapy_parser_pep.git
cd scrapy_parser_pep
python -m venv venv
. venv/Scripts/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
scrapy crawl pep
```

### Вывод информации осуществляется в папку results:
- файл со списком PEP, в котором указаны «Номер», «Название» и «Статус»;  
- Файл со сводкой по статусам;


### Примеры файлов:

```
# pep_2023-06-07T03-22-54.csv

number,name,status
1,PEP Purpose and Guidelines,Active
12,Sample reStructuredText PEP Template,Active
11,CPython platform support,Active
5,Guidelines for Language Evolution,Active
2,Procedure for Adding New Modules,Active
20,The Zen of Python,Active
4,Deprecation of Standard Modules,Active
10,Voting Guidelines,Active
13,Python Language Governance,Active
3,Guidelines for Handling Bug Reports,Withdrawn
```

```
# status_summary_2023-06-07_06-23-41.csv

Статус,Количество
Active,31
Withdrawn,56
Final,273
Rejected,122
Deferred,37
Accepted,49
Draft,24
Superseded,20
April Fool!,1
Total,613
```

### Разработчик:
[Тимощук Олег](https://github.com/olegtsss)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=whte)
