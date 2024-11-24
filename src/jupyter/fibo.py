import scripts.script1 as script1


def fib(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    print(a)


def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


# 作为脚本运行
if __name__ == "__main__":
    script1.sayHello("fibo")
