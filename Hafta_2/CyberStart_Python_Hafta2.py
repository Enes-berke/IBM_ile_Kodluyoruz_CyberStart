### 1) List
#Listeler, birden çok öğeyi tek bir değişkende saklamak için kullanılır. Değiştirilebilirler ve sıralıdırlar.

#**Örnek:**
#```python
my_list = [1, 2, 3, 4, 5]
my_list.append(6)  # Listeye 6 ekler
print(my_list)  # [1, 2, 3, 4, 5, 6]
#```

### 2) Tuple
#Tuple'lar sıralı ve değiştirilemez veri yapılarıdır. Parantez içinde tanımlanırlar.

#**Örnek:**
#```python
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[1])  # 2
#```

### 3) Set
#Set'ler, benzersiz öğelerden oluşan, sırasız ve indekslenemeyen veri yapılarıdır.

#**Örnek:**
#```python
my_set = {1, 2, 3, 4, 5}
my_set.add(6)  # Set'e 6 ekler
print(my_set)  # {1, 2, 3, 4, 5, 6}
#```

### 4) Dictionary
#Dictionary'ler anahtar-değer çiftlerinden oluşan değiştirilebilir ve sıralı veri yapılarıdır.

#**Örnek:**
#```python
my_dict = {"name": "Alice", "age": 25}
print(my_dict["name"])  # Alice
#```

### 5) Non-Scalar For
#Listeler, tuple'lar, set'ler ve dictionary'ler gibi veri yapıları üzerinde iterasyon yapmak için kullanılır.

#**Örnek:**
#```python
my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item)
#```

### 6) Split - Join
#`split()` bir stringi belirli bir ayırıcıya göre bölerken, `join()` bir iterable'ın öğelerini bir string olarak birleştirir.

#**Örnek:**
#```python
s = "Hello World"
words = s.split()  # ['Hello', 'World']
joined = " ".join(words)  # 'Hello World'
#```

### 7) List Comprehension
#Listeleri daha kısa ve okunabilir bir şekilde oluşturmak için kullanılır.

#**Örnek:**
#```python
squares = [x**2 for x in range(10)]  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
#```

### 8) Variable Unpacking
#Listeler, tuple'lar ve diğer iterable'ların öğelerini değişkenlere atamak için kullanılır.

#**Örnek:**
#```python
my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(a, b, c)  # 1 2 3
#```

### 9) Enumerate - Zip
#`enumerate()` bir iterable'ın indekslerini ve öğelerini döndürürken, `zip()` iki veya daha fazla iterable'ı birleştirir.

#**Örnek:**
#```python
my_list = ['a', 'b', 'c']
for index, value in enumerate(my_list):
    print(index, value)

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
for item1, item2 in zip(list1, list2):
    print(item1, item2)
#```

### 10) Fonksiyon Giriş
#Fonksiyonlar, belirli görevleri gerçekleştiren kod bloklarıdır.

#**Örnek:**
#```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
#```

### 11) Return
#Fonksiyonlar bir değer döndürebilir.

#**Örnek:**
#```python
def add(a, b):
    return a + b

result = add(3, 5)
#print(result)  # 8
#```

### 12) Fonksiyonlar Multiple Input - Output
#Fonksiyonlar birden fazla girdi alabilir ve birden fazla çıktı döndürebilir.

#**Örnek:**
#```python
def add_and_subtract(a, b):
    return a + b, a - b

sum, diff = add_and_subtract(5, 3)
print(sum, diff)  # 8 2
#```

### 13) Fonksiyonlar Predefined Parameters
#Fonksiyonlara varsayılan değerler atanabilir.

#**Örnek:**
#```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()  # Hello, Guest!
greet("Alice")  # Hello, Alice!
#```

### 14) Fonksiyon Update Parameters
#Fonksiyon parametreleri güncellenebilir ve değişken sayıda parametre alabilir.

#**Örnek:**
#```python
def update_parameters(*args, **kwargs):
    print(args)
    print(kwargs)

update_parameters(1, 2, 3, name="Alice", age=25)
#```

### 15) First Class Functions
#Fonksiyonlar birer değişken olarak ele alınabilir ve başka fonksiyonlara argüman olarak geçebilir.

#**Örnek:**
#```python
def square(x):
    return x * x

def apply_function(func, value):
    return func(value)

result = apply_function(square, 5)
print(result)  # 25
#```

#Bu kısa açıklamalar ve örnekler, Python'da veri yapıları ve fonksiyonlar hakkında temel bir anlayış sağlar. Her konuyu detaylandırarak Python programlama becerilerinizi geliştirebilirsiniz.