# Решение задания на второй этап отбора
## В репозитории представлено два файла:
**main.py** - код на языке python, решающий задачу, данную в презентации. Он использует уже заранее созданный словарь с даннами, взятыми из примера представленного в презентации
![Пример графа взятого из презентации для **main.py**](/example.png)
Пример графа взятого из презентации для **main.py**
### Способ запуска:
В командной строке в директории с исходным файлом запустить команду: `python3 main.py`

**main_input.py** - код реализация того же самого алгоритма на python, однако имеющий возможность записать собственный дорожный граф. Для этого требуется в первой строчке написать количество вершин n, а в последующих n строках ввести сначала номер вершины, а затем все номера вершин, с которыми она связана

Пример входных данных:  
3  
1 2  
2 1 3  
3 2  
### Способ запуска:
В командной строке в директории с исходным файлом запустить команду: `python3 main_input.py`
## Выходные данные:
Выходные данные представляют собой словарь, в котором ключ - это номер вершины, а значение - это все номера вершин с которыми она связана
