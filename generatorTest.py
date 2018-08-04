#yield 装入数据，产出generator object,使用next释放
def fun3():
    for i in  range(1,5):
        yield i


if __name__ == '__main__':
    gob = fun3()
    print(gob)
    print(next(gob))
    print(next(gob))
    print(next(gob))
    print(next(gob))

    print(next(gob))