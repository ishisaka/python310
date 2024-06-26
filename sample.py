# %%
import sys
print(f"Python version {sys.version}")

# %%
20 + 20 ** 2

# %%
x = 42
x: int = 42
print(x)
# %%
principal = 1000  # 初期金額
rate = 0.05  # 金利
num_years = 5  # 年数
year = 1
while year <= num_years:
    principal = principal * (1 + rate)
    print(f"{year:>3d}, {principal:0.2f}")
    year += 1

# %%
a = 0b11001001
mask = 0b11110000
x = (a & mask) >> 4  # x = 0b1100 (12)
print(x)
# %%
a = 10
b = 15
if a < b:
    print("Computer says Yes")
else:
    print("Computer says No")

if a < b:
    pass  # 何もしない
else:
    print("Computer says No")
# %%
suffix = ".txt"
if suffix == ".html":
    content = "text/html"
elif suffix == ".jpg":
    content = "image/jpeg"
elif suffix == ".png":
    content = "image/png"
else:
    raise RuntimeError(f"Unknown content type {suffix!r}")

# %%
x = 0
while (x := x + 1) < 10:  # 1, 2, 3, ..., 9
    print(x)
# %%
x = 0
while x < 10:
    if x == 5:
        break  # ループを中断する。最下部に移動する。
    print(x)
    x += 1
print("Done")
# %%
x = 0
while x < 10:
    x += 1
    if x == 5:
        continue  # print(x)をスキップ。ループの先頭へ戻る。
    print(x)
print("Done")
# %%
print("""Content-type: text/html

<h1> Hello World </h1>
Click <a href="https://www.python.org">here</a>.
""")
# %%
print(
    "Content-type: text/html\n"
    "\n"
    "<h1> Hello World </h1>\n"
    'Click <a href="https://www.python.org">here</a>\n'
)
# %%
s = "hello\nworld"
print(str(s))
print(repr(s))

# %%
x = 12.34567
print(format(x, "0.2f"))
print(x)

# %%
for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print(f"2 to the {n} power is {2**n}")
# %%
for n in range(1, 10):
    print(f"2 to the {n} power is {2**n}")
# %%
message = "Hello World"
# 文字列を1文字ずつ出力する
for c in message:
    print(c)

names = ["Dave", "Mark", "Ann", "Phil"]
# リストの要素を出力する
for name in names:
    print(name)

prices = {"GOOG": 490.10, "IBM": 91.50, "AAPL": 123.15}
# 辞書の要素を出力する
for key in prices:
    print(key, "=", prices[key])

# テキストファイルを1行ずつ出力する
with open("foo.txt") as file:
    for line in file:
        print(line, end="")
# %%
class Stack:
    def __init__(self):  # スタックの初期化
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def __repr__(self):
        return f"<{type(self).__name__} at 0x{id(self):x}, size={len(self)}>"

    def __len__(self):
        return len(self._items)

s = Stack()  # スタックを作る
s.push("Dave")  # スタックにプッシュ
s.push(42)
s.push([3, 4, 5])
x = s.pop()  # スタックをポップすると[3,4,5]が返される
y = s.pop()  # スタックをポップすると42が返される

print(s)  # <Stack at 0x7f8d1c7b4d30, size=1>
print(len(s))  # 1
print(x)  # [3, 4, 5]
print(y)  # 42

class MyStack(Stack):
    def swap(self):
        a = self.pop()
        b = self.pop()
        self.push(a)
        self.push(b)


s = MyStack()
s.push("Dave")
s.push(42)
s.swap()
print(s.pop())  # Dave
print(s.pop())  # 42
# %%
def factorial(n: int) -> int:
    """
    階乗を計算する。

    >>> factorial(6)
    120
    """
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(8))

# %%

async def greeting(name):
    print(f"Hello {name}")
import asyncio
asyncio.run(greeting("Guido"))
# greeting("Guido")

# %%
def countdown(n):
    print("Counting down from", n)
    while n > 0:
        yield n
        n -= 1

# 使用例
for x in countdown(10):
    print("T-minus", x)
# %%
