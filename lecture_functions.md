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
def function_name(apryMeHTl, аргумент2, .
"" "строка документации" ""
оператор_1
оператор_2
« « «
return выражение
def greet(name): IT IT IT
Эта функция приветствует персону имя которой передается как параметр 1Г 1Г 1Г
print("Hello, " + паше + ". Good morning!")
greet('Иван') a=input() greet(a)
</pre>

# Синтаксис объявления функций.
<pre>
def spring_force (fO , fk , h, x) : i f 0 < x < h: res = 0 else :
res = fO-(fO-fk)‘x/h
return res
</pre>                                            
Ключевое слово def, имя функции, список аргументов.<br>
Результат возвращается при помощи оператора return.<br>
Если оператор return отсутствует, то функция возвращает None.<br>
<pre>
spring_force (10 , 2, 0.1, 0.05)
Результат: 6
</pre>

# Работа функции.
<pre>
def functionName() 	
* <—> * * * * * * • •
functionName(); 
</pre> 
# Типы функций.
Встроенные функции - функции, встроенные в Python.<br>
Пользовательские функции - функции, определяемые самими пользователями.<br>
![image](https://github.com/tvgVita69/python_functions/assets/98489171/a674486c-c524-41ff-a287-b895fb515a6f)

# Строки документации Python.
- Для документации функции используются строковые литералы
<pre>
»> def foo():
...	"""I return 42."""
...	return 42
• • •
</pre>
- После объявления функции документация доступна через специальный атрибут »> foo.	doc	'I return 42.'
- В интерпретаторе удобней пользоваться встроенной функцией »> help(foo) #или foo? в IPython.<br>
                                                                                                
# Строки документации Python.
<pre>
def avg_number(х? y):
- Вычислите и распечатайте среднее двух чисел.
- Создано 29.12.2012. python-docstring-exaraple.py
'"""
print("Average of ",х/' and ",y, " is ",(х+у)/2)
</pre>  
Параметры отладки оболочки редактирования файла Справка Windows.<br>
Python 3.2.3 (default, Apr 11 2012, 07:15:24) [MSC v.1500 32 bit (Intel)] on Win32 Type "copyright", "credits" or "licensed" for more information. »> ================================ RESTART	=»> print (avg_nuiuher .	doc)<br>
Calculate and Print Average of two Numbers.<br>
Created on 29/12/2012. python-docstring-exaraple.py<br>

# Аргументы функций.
Объявление функции:
<pre>
def spring_force (fO , fk, h, x) :
) ■ • • •  
Вызов функции:
spring_force (10.0 , 2.0, 0.1, 0.05):
- Аргументы функции spring_force должны передаваться в том порядке, в котором это задумано автором функции
- При вызове функции необходимо помнить смысловой порядок аргументов 
</pre>

# Аргументы функций передаются по ссылке.
<pre>
def changeme( mylist ):
"This changes a passed list into this function mylist.append([lJ2J3J4])j
print ("Values inside the function: ", mylist) return
# Вызывем функцию changeme
mylist = [10,20,30];
changeme( mylist );
print( "Values outside the function:	mylist)|
Values inside the function: [10, 20, 36, [1, 2, 3, 4]]
Values outside the function: [10, 20, 30, [1, 2, 3, 4]] 
</pre>  

# Именованные аргументы функций.
Объявление функции:
<pre>
1	def spring_force (fO , fk , h, x):
2	...
</pre>  
Возможна передача функции именованных аргументов
<pre>
i f = spring_force (h = 0.3 ,f0 = 10,fk=2,х = 0.15)
</pre>  
® Порядок аргументов может быть произвольным<br>
• Такой способ вызова позволяет исключить ошибки<br> 































