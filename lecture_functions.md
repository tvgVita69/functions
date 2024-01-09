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
def spring_force(fo, fk, h, x):
    if 0 < x < h:
        res = 0
    else:
        res = fo - (fo - fk) * x / h
        return res
</pre>                                            
- Ключевое слово def, имя функции, список аргументов.<br>
- Результат возвращается при помощи оператора return.<br>
- Если оператор return отсутствует, то функция возвращает None.<br>
<pre>
print(spring_force(6, 5, -1, 2))
Результат: 8.0
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
spring_force(10.0, 2.0, 0.1, 0.05):
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
def spring_force(fO , fk , h, x):
...
</pre>  
Возможна передача функции именованных аргументов
<pre>
f = spring_force(h = 0.3, f0 = 10, fk=2, х = 0.15)
</pre>  
- Порядок аргументов может быть произвольным<br>
- Такой способ вызова позволяет исключить ошибки<br> 

# Параметры по умолчанию.
<pre>
def eight_max(vo, g = 9.81):
"'Максимальная высота подъёма груза, брошенного вверх с начальной скоростью vo(м/с), 
  при ускорении свободного падения g(м/с**2)
"'
return O.5*vo**2/g
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
def add_element_to_b(а, Ь = []): 
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
print(fun(3))
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
» Local variable 'a' referenced before assignment.<br> 
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
При необходимости изменить переменную объемлющей области её необходимо объявить nonlocal.<br>
<pre>
a = 1 #Глобальная переменная модуля
def fun(х):
    a = 10 #Локальная переменная модуля функции fun
    def inner_fun(x):
        nonlocal a #Переменная из объемлющей области
        a = a + 5  #Было 10, стало 15
        b = a + x
        return b
    res = inner_fun(x)
    return (a,res)
print(fun(1))
» (15, 16)
</pre>

# Имя функции как переменная.
<pre>
def step_function (х0, у0, y1) 
    def step(х):
        if х < х0:
          return у0 
        else:
          return y1 
    return step
</pre>    
Вызов функции step_f unction создает объект функцию step с заданными значениями х0, у0, у 1:
<pre>
unit_step = step_function (0.0, 0.0, 1.0)
unit_step(-2)
» О
unit_step(l)
» 1 
</pre>

# Замыкание.
- Функция (внутренняя), определяемая в теле другой (внешней) функции и создаваемая каждый раз во время выполнения внешней функции.
- Внутренняя функция содержит ссылки на локальные переменные внешней функции.

# Анонимная(лямбда) функция.
Синтаксис: lambda[argl[,arg2,...argn]]:expression<br>
- Короткие однострочные функции могут быть объявлены при помощи lambda-функций
<pre>mean = Lambda х,у: (х + у)*0.5</pre>
Вызов функции<br>
<pre>
mean(l,6)
» 3.5 </pre>
- Лямбда-функция обычно используется в паре с функциями filter, map, sort

# Функция filter.
Применение лямбда-функции с функцией filter<br>
<pre>
» data = {1, 7, 3, 2, 6, 8}
» filteг(lambda x: x % 2 == 0, data)
{2, 6, 8}
</pre>
# Функция filter.
Применение лямбда-функции с функцией filter<br>
<pre>
data = {1, 7, 3, 2, 6, 8}
def less_than_5(х): return x < 5 
» filter(less_than_5, data) 
{1, 3, 2}
</pre>  
но лучше:

<pre>
def less_than(value): return Lambda x: x < value
</pre>
<pre>
» filter(less_than(5), data) 
{1. 5, 2}
</pre>                                           
или совсем просто:
<pre>» filteг(lambda x: x < 5, data)</pre> 

# Функция map.
Функция map(function, data) применяет function к каждому элементу последовательности data:
<pre>
data = [4,5,6,7]
» map(Lambda x: x‘*2, data)
cbuiltins .map at 0xa8d36bcc></pre>
Функция map - ленивая функция. Функция возвращает не весь обработанный список, а ссылку на функцию-генератор, которая вычисляет значения по мере необходимости, подобно функции range:
<pre>
» List (map(lambda х: х**2, data))
[16, 25, 36, 49] 
</pre>

# Функция map.
Функцию map можно использовать для обработки нескольких списков.
<pre>
vec1 = [1,4,3,7]
vec2 = [8,5,1,3]
prod = map(lambda x,y: x*y, vec1,vec2)
scalar_product = sum(prod)
52
a,b,c = map(int,input().slip())
2 6 9
</pre>

# Списочные выражения.
Вместо функции map<br>
<pre>
data = [10, 12, 13, 14]
>> list(map(Lambda х: х**2, data))
[16, 25, 36, 49] 
<br>можно использовать списочные выражения
res = [х**2 for х in data]
рrint(res)
[16, 25, 36, 49]
</pre>

# Списочные выражения.
Выражение формирует список квадратов только чётных элементов из range(10):
<pre>
х**2 for х in range(10) if х % 2 == 0
[0, 4, 16, 36, 64]
Эту же последовательность можно сгенерировать при помощи функций тар и filter:
list(map(lambda х: х**2,
      filter(lambda x: x%2==0, range(10))))
[0, 4, 16, 36, 64] 
</pre>
# Выражения с вложенными циклами.
Списочные выражения могут содержать несколько вложенных циклов:
<pre>
[ х+'-'+у for х in ('А','В') for у in ('1', '2')]
['А-Г', 'А-2', 'В-Г', 'В-2']
</pre>
# Функции-генераторы.
При помощи ключевого слова yield создаются функции, “лениво” генерирующие последовательности, подобно функции range<br>
В определении такой функции return заменяется на yield:
<pre>
def progression(a1, d, n = 5):
    # an = a1 + d (n-1) 
    for i in range (n):
          yield a1+d*i
» progression (1, 3)
<generator object progression at 0xa8dc68c4>
» list(progression (1, 3)) 
[1, 4, 7, 10, 13]
</pre>  

# Функции-генераторы.
Функция-генератор чисел Фибоначчи 
<pre>
def fib(count): 
    n0, nl = 0, 1
    for i in range(count):
        n0, nl = nl, n0+n1 
        yield n0
</pre>        
Все элементы можно получить создав список по этому итератору <br>
list(fib(10))
[1,1,2,3,5,8,13,21,34,55]

# Функции-генераторы.
- Функция-генератор чисел Фибоначчи
<pre>
def fib (count):
    n0, nl = 0, 1
    for i in range(count): 
        n0, nl = nl, n0+nl 
        yield n0
</pre>
- Последовательно получить элементы можно при помощи функции next:
<pre>
а = fib (10)
» next(a)
1
» next(a)
1
» next(a)
2
</pre>

# Пример.
<pre>text = "Feci quod potui, faciant meliora potentes" </pre>
- Формирование множества букв предложения:
<pre>
letters_set = set(text)
Letters_set.remove (' ')
Letters_set.remove (',')
</pre>  
- Формирование списка пар (буква, частота):
<pre>res = [(х, text.count(х)) for х in Letters_set]</pre>
Сортировка по второму элементу пары:
<pre>res.sort(key = Lambda pair: pair[l], reverse = True)</pre>
Вывод первых пяти наиболее встречающихся букв:
<pre>print(res[: 5])
[('О', 4),('f', 4),('e', 4),('i', 4),('a', 3)]
</pre>

# Списочные выражения и генераторы.
- Списочное выражение формирует сразу весь список(list)<br>
<pre>
res = [(х, text.count(х)) for х in letters_set]
» type(res) list
</pre>  
- Это выражение создаёт итератор, который будет вычислять следующее значение по требованию:
<pre>res = ( (х, text.count(х)) for х in letters_set] )
» type(res)
iterator
</pre>  
Итератор можно пройти только один раз!<br>

# Функция zip.
Функция zip( il, i2, ...) объединяет итераторы-аргументы и создаёт итератор по кортежам элементов аргументов:
<pre>
word = "Qapla"
for i, j in zip(range(len(word)), word): print(i +1, "буква ", j)
1	буква Q
2	буква a
3	буква p
4	буква l
5	буква a 
</pre>
Если аргументы-итераторы (последовательности) разной длины, то результирующий итератор будет иметь длину минимального аргумента.<br> 




