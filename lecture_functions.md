- Синтаксис объявления функций
- Работа функции
- Строки документации Python
- Вызов функции
- Аргументы функций
- Локальные переменные
- Области видимости переменных
- Анонимная (лямбда) функция
- Функция filter
- Функция map
- Функция zip

# Синтаксис объявления функций.
<pre>
def function_name(apryментl, аргумент2, ...)
"" "строка документации" ""
оператор_1
оператор_2
...
return выражение
def greet(name): 
"""
Эта функция приветствует персону 
  имя которой передается как параметр
"""  
print("Hello, " + паше + ". Good morning!")
greet('Иван') 
a=input() 
greet(a)
</pre>

# Синтаксис объявления функций.
<pre>
def spring_force (fO , fk , h, x): 
  if 0 < x < h: 
    res = 0
  else :
    res = fO-(fO-fk)*x/h
  return res
</pre>                                            
- Ключевое слово def, имя функции, список аргументов.<br>
- Результат возвращается при помощи оператора return.<br>
- Если оператор return отсутствует, то функция возвращает None.<br>
<pre>
spring_force(10, 2, 0.1, 0.05)
Результат: 6
</pre>

# Работа функции.
<pre>
![image](https://github.com/tvgVita69/python_functions/assets/98489171/7ee09717-9d74-4159-ae10-cc2440b157b9)
</pre> 
# Типы функций.
- Встроенные функции - функции, встроенные в Python.
- Пользовательские функции - функции, определяемые самими пользователями.<br>
![image](https://github.com/tvgVita69/python_functions/assets/98489171/a674486c-c524-41ff-a287-b895fb515a6f)

# Строки документации Python.
- Для документации функции используются строковые литералы
<pre>
»> def foo():
...	"""I return 42."""
...	return 42
...

- После объявления функции документация доступна через специальный атрибут »» foo.__)doc__
  'I return 42.'
- В интерпретаторе удобней пользоваться встроенной функцией »» help(foo) #или foo? в IPython.<br>
</pre>                                                                                                
# Строки документации Python.
<pre>
def avg_number(х? y):
"""
  Вычислите и распечатайте среднее двух чисел.
    Создано 29.12.2012. python-docstring-exaraple.py
"""
print("Average of ",х/' and ",y, " is ",(х+у)/2)
</pre>  
<br>

# Аргументы функций.
Объявление функции:
<pre>
def spring_force(fO , fk, h, x) :
) ...  
Вызов функции:
spring_force(10.0 , 2.0, 0.1, 0.05):
- Аргументы функции spring_force должны передаваться в том порядке, в котором это задумано автором функции
- При вызове функции необходимо помнить смысловой порядок аргументов 
</pre>

# Аргументы функций передаются по ссылке.
<pre>
def changeme(mylist):
"This changes a passed list into this function" 
  mylist.append([l,2,3,4])
print ("Values inside the function: ", mylist) return
# Вызывем функцию changeme
mylist = [10,20,30]
changeme(mylist)
print( "Values outside the function: ",	mylist)
Values inside the function: [10, 20, 36, [1, 2, 3, 4]]
Values outside the function: [10, 20, 30, [1, 2, 3, 4]] 
</pre>  

# Именованные аргументы функций.
Объявление функции:
<pre>
def spring_force (fO , fk , h, x):
...
</pre>  
Возможна передача функции именованных аргументов
<pre>
f = spring_force (h = 0.3 ,f0 = 10,fk=2,х = 0.15)
</pre>  
- Порядок аргументов может быть произвольным<br>
- Такой способ вызова позволяет исключить ошибки<br> 

# Параметры по умолчанию.
<pre>
def eight_max (vO, g = 9.81):
"'Максимальная высота подъёма груза, брошенного вверх с начальной скоростью vO (м/с), 
  при ускорении свободного падения g (м/с**2)
"'
return O.5*vO**2/g
Высота подъёма груза на Земле, g~9.81 м/с2
» height_max(10)
5.098399102681758
Высота подъёма груза на Луне, g~1.62 м/с2
» round (height_max (10,1.62),1)
30.9 
</pre>

# Параметры по умолчанию.
При использовании ссылочных типов в параметрах по умолчанию их значение при изменении внутри функции сохраняется и до следующего вызова этой функции:
<pre>
def add_element_to_b(а , Ь = []): 
  b.append(а)
  return Ь
При первом вызове функции: b - пустой список
add_element_to_b(4)
[4]
При втором вызове функции: b “вспомнит” последнее значение
add_element_to_b(5)
[4,5]
</pre>

# Переменное число аргументов.
Упаковка позиционных аргументов в кортеж args
<pre>
def zeros(*args):
    print('Аргументы: ', args)
    if len(args) == 1:
        return [0]*args[0]
    if len(args) == 2:
        return [[0]*args[0]]*args[1]
</pre>
Переданные аргументы будут собраны в кортеж args
<br><pre>
zeros(3,3)
» Аргументы:(3,3)
[[0, 0, 0],
[0, 0, 0],
[0, 0, 0]]
</pre>

# Переменное число аргументов.
<pre>
def zeros(n1, *args):
    if len(args) == 0:
        return [0]*n1
    if len(args) == 1:
        return [[0]*n1]*args[0]

zeros()
» TypeError: zeros() missing 1 required positional argument: 'n1'
def zeros(n, *args):
    if len(args) == 0:
        return [0] * n
    if len(args) == 1:
        return [[0] * n]*args[0]
print(zeros(3))
» [0, 0, 0]
</pre>

# Переменное число аргументов Именованные аргументы.
<pre>
def zeros(**kwargs):
    if kwargs.get('diml'):
        res = [0] * kwargs['diml']
    if kwargs.get('dim2'):
        res = [res] * kwargs['dim2']
        return res
Переданные аргументы будут собраны в словарь kwargs
print(zeros(diml=3))  
zeros (diml = 3)
» None
print(zeros(diml=2, dim2=2))
» [[0, 0], [0, 0]] 
</pre>

# Локальные переменные.
При каждом вызове функции создаётся новое локальное пространство имён.
<pre>
a = 1 #Глобальная переменная модуля
def fun(х):
    а = 2 #Локальная переменная
    return х + а
print(fun (3))
» 5
</pre>

# Области видимости переменных.
<pre>
def my_func():
        х = 10
        print("Значение внутри функции:", х)
x = 20
my_func()
print("Значение внутри функции:", x)
» Значение внутри функции: 10
» Значение внутри функции: 20  
</pre>

# Инструкция global.
<pre>
a = 1 # Глобальная переменная модуля 
def fun(х):
    b = 10 + а  #а из глобальной области
    а = 1	#ОШИБКА!
    return Ь
</pre>  
» Local variable ’a’ referenced before assignment.<br> 
Изменить глобальную переменную можно, объявив её глобальной:
<pre>
а = 1 #Глобальная переменная модуля
def fun(x):
    global а
    а = 3
    b = 10 + а
    return b
print(fun(5)) 
» 13
</pre>

# Инструкция nonlocal.












