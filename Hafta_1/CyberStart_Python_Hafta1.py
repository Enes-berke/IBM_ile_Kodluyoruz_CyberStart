# Temel Veri Tipleri Python'da temel veri tipleri arasında int (tamsayı), float (ondalıklı sayı), str (string), ve bool (mantıksal veri tipi) bulunur.

x = 10          # int
y = 3.14        # float
z = "Hello"     # str
a = True        # bool

​


# Değişken Atama Python'da değişkenler dinamik olarak atanır, yani veri tipini belirtmek gerekmez. Atama operatörü = kullanılır.
x = 5
y = "Python"
​


# Operatörler ve İfadeler (Operators - Expressions) Python'da aritmetik operatörler (+, -, *, /), karşılaştırma operatörleri (==, !=, <, >, <=, >=) ve mantıksal operatörler (and, or, not) sıkça kullanılır.
a = 10
b = 5
c = a + b  # c = 15
d = (a > b)  # d = True
​


#String Veri Tipi - String Operatörleri - İndeksleme - Dönüştürme (Casting) Stringler karakter dizileridir ve + operatörü ile birleştirilebilir. İndeksleme ile karakterlere erişilebilir. Casting, veri tiplerini dönüştürmek için kullanılır.
s = "Hello, "
t = "World!"
u = s + t  # u = "Hello, World!"
first_char = s[0]  # first_char = 'H'
num_str = str(123)  # num_str = '123'
​


#Sayısal Verilerde Karşılaştırma Sayısal veriler karşılaştırma operatörleri ile karşılaştırılabilir.
a = 10
b = 5
result = (a > b)  # result = True
​


#String Karşılaştırma Stringler alfabetik sıralama ve uzunluklarına göre karşılaştırılabilir.
str1 = "apple"
str2 = "banana"
result = (str1 < str2)  # result = True, çünkü 'a' < 'b'
​


#Mantıksal Operatörler (Logical Operators) and, or, not mantıksal ifadeleri birleştirmek için kullanılır.
a = True
b = False
result = a and b  # result = False
result = a or b  # result = True
result = not a  # result = False
​


#Short-Circuit Mantıksal operatörlerde short-circuit, gereksiz işlemleri önlemek için kullanılır.
a = True
b = False
result = a or (b and a)  # result = True, çünkü 'a' True olduğunda diğer ifadeyi kontrol etmeye gerek kalmaz.
​


#Else - If - Elif Koşullu ifadeler ile belirli kod blokları çalıştırılabilir.
x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")
​
# x is greater than 5


#Ternary Conditionals (Üçlü Koşullu İfadeler) Kısa if-else ifadeleri için kullanılır.
x = 10
result = "x is greater than 5" if x > 5 else "x is not greater than 5"
​


# Döngüler (Loops) Python'da for ve while döngüleri ile tekrar eden işlemler yapılabilir.

# for loop
for i in range(5):
    print(i)
​

# while loop
count = 0
while count < 5:
    print(count)
    count += 1
# 0
# 1
# 2
# 3
# 4
# 0
# 1
# 2
# 3
# 4


#While Döngüsü Belirli bir koşul sağlandığı sürece çalışır.
count = 0
while count < 5:
    print(count)
    count += 1
​
# 0
# 1
# 2
# 3
# 4


#13) For Döngüsü
#Belirli bir dizideki her bir eleman için çalışır.
for i in range(5):
    print(i)
# ​
# 0
# 1
# 2
# 3
# 4


#Continue - Break Döngülerde belirli durumlarda döngüyü atlamak veya sonlandırmak için kullanılır.

for i in range(5):
    if i == 2:
        continue  # 2 atlanacak
    if i == 4:
        break  # Döngü 4'te sona erecek
    print(i)
​
# 0
# 1
# 3