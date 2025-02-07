#!/media/linux/usr/bin/python3.13

def mygen():
    yield 20
    yield 40
    yield 60
    yield 80
    yield 100

def mygen2():
    for i in range(100):
        yield i

gen = mygen()
gen2 = mygen()

#print(next(gen))
#print(next(gen))
#print(next(gen))
#print(next(gen))
#print(next(gen))

#try:
#    print(next(gen))
#    print(next(gen))
#    print(next(gen))
#    print(next(gen))
#    print(next(gen))
#    print(next(gen))
#except StopIteration:
#    pass

#for item in gen:
#    print(item)

