# Python 基礎まとめ

## 1. 変数、標準入力出力、コメント文

Python の基本となる変数の定義、標準入力出力、コメントの使い方について説明します。

### 1.1 変数の定義

Python の変数はデータを格納するためのもので、データ型を明示する必要はありません。動的型付け言語のため、値に応じて型が自動的に決定されます。

```python
x = 10
y = "Hello"
z = 3.14
print(type(x), type(y), type(z))  # <class 'int'> <class 'str'> <class 'float'>
```

### 1.2 標準入力と出力

```python
name = input("名前を入力してください: ")
print(f"こんにちは、{name}さん！")
```

標準入力（`input()`）でユーザーからの入力を取得し、標準出力（`print()`）で表示します。

### 1.3 コメントの記述

Python では `#` を使ってコメントを書きます。

```python
# これはコメントです
```

コメントはコードの可読性を向上させるために重要です。

## 2. 定数

Python には定数を明示的に定義する機能はありませんが、慣例として全て大文字で記述します。

```python
PI = 3.14159
```

## 3. 論理型、AND, OR

論理型（`True` / `False`）は条件分岐やループで頻繁に使用されます。

```python
x = True
y = False
print(x and y)  # False
print(x or y)   # True
print(not x)    # False
```

## 4. 数値型（整数型、浮動小数点数型）

Python では整数型（`int`）、浮動小数点数型（`float`）、複素数型（`complex`）が扱えます。

```python
x = 10
y = 3.14
print(x + y, x - y, x * y, x / y)  # 13.14 6.86 31.4 3.18
```

## 5. 進数（2 進数、8 進数、16 進数）

```python
binary = 0b1010  # 2進数
octal = 0o12  # 8進数
hexadecimal = 0xA  # 16進数
print(binary, octal, hexadecimal)
```

## 6. 複素数

Python は複素数をサポートしています。

```python
z = complex(2, 3)
print(z.real, z.imag)  # 実部と虚部
```

## 7. 文字列

文字列はシングルクォートまたはダブルクォートで囲みます。

```python
s = "Hello"
print(s.upper(), s.lower(), s.replace("H", "J"))  # HELLO hello Jello
```

## 8. リスト

リストは可変長のデータ構造で、異なる型の要素を格納できます。

```python
lst = [1, "apple", 3.14]
lst.append(4)  # 要素の追加
lst.remove("apple")  # 要素の削除
print(lst)
```

## 9. 辞書

辞書はキーと値のペアでデータを格納します。

```python
d = {"name": "Alice", "age": 25}
d["age"] = 26  # 値の更新
print(d["name"], d["age"])
```

## 10. タプル

タプルはリストと似ていますが、要素の変更ができない（イミュータブル）データ構造です。

```python
tuple_data = (1, "banana", 3.14)
print(tuple_data)
print(tuple_data[1])  # "banana"
# tuple_data[0] = 100  # エラー（タプルは変更不可）
```

## 11. セット

セットは重複を許さないデータ構造で、集合演算を行うことができます。

```python
set_data = {1, 2, 3, 3, 4}
print(set_data)  # {1, 2, 3, 4}
set_data.add(5)  # 要素の追加
set_data.remove(3)  # 要素の削除
print(set_data)
```

## 12. 条件分岐（if 文）

### 12.1 基本的な if 文

```python
x = 10
if x > 5:
    print("xは5より大きい")
elif x == 5:
    print("xは5")
else:
    print("xは5より小さい")
```

### 12.2 if all と if any

Python では `all()` 関数と `any()` 関数を使用して、リストやタプル内のすべてまたは一部の要素が特定の条件を満たしているかを判定できます。

```python
values = [True, True, False]
if all(values):
    print("すべての要素がTrueです")
else:
    print("少なくとも1つの要素がFalseです")

if any(values):
    print("少なくとも1つの要素がTrueです")
else:
    print("すべての要素がFalseです")
```

`all()` はリスト内のすべての要素が `True` の場合に `True` を返し、`any()` は少なくとも 1 つの要素が `True` の場合に `True` を返します。

## 13. ループ文（for, while）

```python
for i in range(5):
    print(i)

count = 0
while count < 5:
    print(count)
    count += 1
```

## 14. 関数

### 14.1 基本的な関数

関数はコードの再利用性を高めるために重要です。

```python
def greet(name):
    return f"Hello, {name}"
print(greet("Alice"))
```

### 14.2 可変長引数

Python では、関数に渡す引数の数を可変にすることができます。`*args` を使うと、複数の位置引数をタプルとして受け取れます。

```python
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4, 5))  # 15
```

また、`**kwargs` を使うと、複数のキーワード引数を辞書として受け取ることができます。

```python
def greet_all(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

greet_all(name="Alice", age=25, city="Tokyo")
```

### 14.3 複数の返り値

Python の関数は、複数の値をタプルとして返すことができます。

```python
def get_coordinates():
    x, y = 10, 20
    return x, y

x, y = get_coordinates()
print(f"X座標: {x}, Y座標: {y}")
```

## 15. グローバル変数

グローバル変数は関数外で定義され、関数内でも `global` キーワードを使うことで変更が可能です。

```python
x = 10

def update_x():
    global x
    x = 20

update_x()
print(x)  # 20
```

## 16. 関数内関数

関数の中に関数を定義することができます。

```python
def outer():
    def inner():
        print("Inner function")
    inner()

outer()
```

## 17.1 ジェネレータ関数

ジェネレータ関数は `yield` を使用して値を順次生成します。

```python
def my_generator():
    received = yield 1
    print(f"Received: {received}")
    received = yield 2
    print(f"Received: {received}")
    yield 3

gen = my_generator()
print(next(gen))  # 1
print(gen.send("Hello"))  # 2, Received: Hello
print(gen.send("World"))  # 3, Received: World
```

### 17.2 send() メソッド

`send()` を使用すると、ジェネレータに値を送信しながら次の `yield` まで進めることができます。

```python
def my_generator():
    received = yield 1
    print(f"Received: {received}")
    received = yield 2
    print(f"Received: {received}")
    yield 3

gen = my_generator()
print(next(gen))  # 1
print(gen.send("Hello"))  # 2, Received: Hello
print(gen.send("World"))  # 3, Received: World
```

### 17.3 throw() メソッド

`throw()` を使うと、ジェネレータの実行中に例外を発生させることができます。

```python
def controlled_generator():
    try:
        yield 1
        yield 2
        yield 3
    except Exception as e:
        print(f"Exception caught: {e}")
    finally:
        print("Generator closing")

gen = controlled_generator()
print(next(gen))  # 1
print(next(gen))  # 2
gen.throw(ValueError("An error occurred"))  # Exception caught: An error occurred
```

### 17.4 close() メソッド

`close()` を使用すると、ジェネレータを明示的に終了させることができます。

```python
def my_generator():
    try:
        yield 1
        yield 2
    finally:
        print("Generator is closing")

gen = my_generator()
print(next(gen))  # 1
gen.close()  # Generator is closing
```

## 18. サブジェネレータ関数

ジェネレータの中で別のジェネレータを呼び出すことができます。

```python
def sub_generator():
    yield from range(3)

def controlled_generator():
    try:
        yield 1
        yield 2
        yield 3
    except Exception as e:
        print(f"Exception caught: {e}")
    finally:
        print("Generator closing")

gen = controlled_generator()
print(next(gen))  # 1
print(next(gen))  # 2
gen.throw(ValueError("An error occurred"))  # Exception caught: An error occurred
gen.close()  # Generator closing
```

## 19. 高階関数

高階関数は、関数を引数として受け取ったり、関数を返すことができます。

```python
def apply(func, value):
    return func(value)

print(apply(lambda x: x * 2, 5))  # 10
```

## 20. lambda 式

匿名関数を作成できます。

```python
square = lambda x: x ** 2
print(square(4))  # 16
```

## 21. 再帰

関数が自分自身を呼び出すことができます。

```python
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120
```

## 22. リスト内包表記

リストを簡潔に生成できます。

```python
squares = [x ** 2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]
```

## 23. デコレーター関数

関数の動作を拡張するために使用されます。

```python
def decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@decorator
def say_hello():
    print("Hello")

say_hello()
```

## 24. map 関数

`map()` 関数は、リストやタプルなどのイテラブルなデータに対して関数を適用し、新しいイテラブルを作成します。

```python
def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
print(squared_numbers)  # [1, 4, 9, 16, 25]
```

ラムダ関数と組み合わせることもできます。

```python
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # [1, 4, 9, 16, 25]
```

## 25. クラスとオブジェクト

Python のオブジェクト指向プログラミングの基本です。

### 25.1 クラス定義

クラスは `class` キーワードを使って定義します。

```python
class Person:
    pass
```

### 25.2 クラス変数とインスタンス変数

クラス変数はクラス全体で共有される変数で、インスタンス変数は各インスタンスごとに異なる値を持ちます。

```python
class Person:
    species = "Human"  # クラス変数

    def __init__(self, name, age):
        self.name = name  # インスタンス変数
        self.age = age  # インスタンス変数
```

### 25.3 コンストラクタ

コンストラクタ（`__init__` メソッド）は、インスタンスが生成される際に自動的に呼ばれます。

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

### 25.4 デストラクタ

デストラクタ（`__del__` メソッド）は、インスタンスが削除されるときに呼ばれます。

```python
class Person:
    def __init__(self, name):
        self.name = name
        print(f"{self.name}が作成されました")

    def __del__(self):
        print(f"{self.name}が削除されました")
```

### 25.5 インスタンスメソッド

インスタンスメソッドは、インスタンスごとに動作するメソッドで、`self` を通じてインスタンス変数にアクセスできます。

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, my name is {self.name}"
```

### 25.6 クラスメソッド

クラスメソッドは `@classmethod` デコレーターを付けて定義し、`cls` を引数に取ります。

```python
class Person:
    species = "Human"

    @classmethod
    def get_species(cls):
        return cls.species
```

### 25.7 スタティックメソッド

スタティックメソッドは `@staticmethod` デコレーターを付けて定義し、インスタンス変数やクラス変数にアクセスしません。

```python
class Utility:
    @staticmethod
    def add(x, y):
        return x + y
```

## 26. クラスの継承

クラスの機能を別のクラスに引き継ぐことができます。

```python
class Animal:
    def speak(self):
        return "Animal sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

dog = Dog()
print(dog.speak())  # Woof!
```

## 27. メタクラス

クラスの振る舞いを制御できます。

```python
class Meta(type):
    def __new__(cls, name, bases, dct):
        dct["greet"] = lambda self: "Hello from Meta"
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass

obj = MyClass()
print(obj.greet())  # Hello from Meta
```

## 28. ファイル入出力

```python
with open("test.txt", "w") as f:
    f.write("Hello, World!")
with open("test.txt", "r") as f:
    print(f.read())
```

## 29. with 構文

リソース管理を簡潔に記述できます。

```python
with open("test.txt", "r") as f:
    content = f.read()
print(content)
```

## 30. パッケージ管理

Python では `import` 文を使用して外部モジュールをインポートできます。

```python
import math
print(math.sqrt(16))  # 4.0
```

また、特定の関数やクラスだけをインポートすることもできます。

```python
from math import sqrt
print(sqrt(16))  # 4.0
```

エイリアス（別名）を付けることも可能です。

```python
import numpy as np
print(np.array([1, 2, 3]))
```
