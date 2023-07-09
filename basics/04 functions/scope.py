
number = 12

def test1():
    print(number) # 12

test1() # 12

def test2():
    number = 100
    print(number)
    if True:
        print(number) # 100
        if True:
            number = 50
            print(number) # 50
    print(number) # 50



test2() # 100
print(number) # 12

print("\n test3")
def test3():
    global number
    number = 5
    print("test3", number) # 5
    if True:
        number = 6
        print("test3", number) # 6

test3()
print("global number after test3(): ", number) # 6

print("\n test4")
number = 10
def test4(number):
    print("test4 param:", number)
    number = 20
    print("test4 after change:", number)

test4(33)
print("global number after test4():",number)


print("\ntest5")

number = 10
def foo():
    print("foo number:", number) # 10

def bar():
    number = 9
    print("bar() number:", number) # 9
    foo()

bar()
print("global number after foo() bar():", number)

print("\n check1 & check2")
number = 10

def chceck1():
    number = 12
    print("chceck1() number:", number) # 12
    def chceck2():
        print("chceck2() number:", number) # 12
    chceck2()

chceck1()
print("global number after chceck1():", number)



print("\nif test")

if True:
    data = 100 # utworzy zmienną globalną

print(data) # 100

if False:
    nextData = 15

# print(nextData) BŁĄD


