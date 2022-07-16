# https://www.imooc.com/code/22157
import math
import sys
import tools
from functools import reduce

CHAPTER_PREFIX = '=' * 50 + '> '


class Person(object):
    country = 'Asia'
    __location = 'Asia'

    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def get_info(self):
        return 'name = {}, age = {}, location = {}'.format(self.name, self.age, self.__location)

    @classmethod
    def set_location(cls, location):
        cls.__location = location

    @classmethod
    def get_location(cls):
        return cls.__location

    def who(self):
        return 'I am a Person, my name is %s' % self.name

    def __len__(self):
        return len(self.name)

    def __call__(self, friend):
        print('My name is {}...'.format(self.name))
        print('My friend is {}...'.format(friend))


print(CHAPTER_PREFIX + '实例属性的初始化')
person = Person('Xiao Hong', 'girl', 14)
print(person.name)
print(person.sex)
print(person.age)

print(CHAPTER_PREFIX + '类属性')
print(person.country)  # ==> Asia
print(Person.country)  # ==> Asia

print(CHAPTER_PREFIX + '定义实例方法')
print(person.get_info())

print(CHAPTER_PREFIX + '定义类方法')
print(Person.get_location())  # ==> Asia
Person.set_location('Africa')
print(Person.get_location())  # ==> Africa


class Student(Person):
    def __init__(self, name, sex, age, score):
        super(Student, self).__init__(name, sex, age)
        self.score = score

    def who(self):
        return 'I am a Student, my name is %s' % self.name


print(CHAPTER_PREFIX + '继承类')
student = Student('Alice', 'girl', 18, 100)
print(student.name)  # ==> Alice
print(student.sex)  # ==> girl
print(student.score)  # ==> 100
print(student.get_info())

print(CHAPTER_PREFIX + '判断类型')
print(isinstance(person, Person))
print(isinstance(person, Student))
print(isinstance(student, Person))
print(isinstance(student, Student))
s = 'this is a string.'
n = 10
print(isinstance(s, int))  # ==> False
print(isinstance(n, str))  # ==> False

print(CHAPTER_PREFIX + '多态')
print(person.who())
print(student.who())

print(CHAPTER_PREFIX + '获取对象信息')
print(type(n))  # ==> <class 'int'>
print(type(s))  # ==> <class 'str'>
print(type(person))  # ==> <class '__main__.Person'>
print(type(student))  # ==> <class '__main__.Student'>
print(dir(n))
print(dir(s))
print(dir(person))
print(getattr(person, 'name'))
setattr(person, 'name', 'Adam')
print(getattr(person, 'name'))
print(getattr(student, 'age', 20))

print(CHAPTER_PREFIX + '类的__str__ 和 __repr__方法')
num = 12
print(str(num))  # ==> '12'
test_dict = {1: 1, 2: 2}
print(str(test_dict))  # ==> '{1: 1, 2: 2}'
print(test_dict)  # ==> '{1: 1, 2: 2}'
L = [1, 2, 3, 4, 5]
print(str(L))  # ==> '[1, 2, 3, 4, 5]'
print(L)  # ==> '[1, 2, 3, 4, 5]'
print(str(person))

print(CHAPTER_PREFIX + '类的__len__方法')
print(len(person))

print(CHAPTER_PREFIX + '类的数学运算')
num = 5
print(num.__truediv__(3))
print(num.__floordiv__(3))  # 向下取整 ==> 1
print(5 / 3)
print(5 // 3)

print(CHAPTER_PREFIX + '类的__call__方法')
f = abs
print(f)
print(f.__name__)
print(f(-123))
person('Alice')

print(CHAPTER_PREFIX + '导入模块')
print(math.pi)
print(math.pow(2, 3))  # 函数：次方

print(CHAPTER_PREFIX + '模块导入的路径')
print(sys.path)
tools.say_hello()  # 调用模块里面的say_hello()函数
tools.say_goodbye()  # 调用模块里面的say_goodbye()函数

print(CHAPTER_PREFIX + '把字符串写入文件')
f = open('test.txt', 'w')
f.write('Hello World\n')
f.close()
lines = ['Hello World\n', 'Hello Python\n', 'Hello Imooc\n']
f = open('test.txt', 'w')
f.writelines(lines)
f.close()

print(CHAPTER_PREFIX + '往文件追加内容')
f = open('test.txt', 'a+')
content = f.readlines()
print(content)  # ==> []
f.seek(0)  # 文件游标移动到了文件的首部
content = f.readlines()
print(content)  # ==> ['Hello World\n', 'Hello Python\n', 'Hello Imooc\n']
f.close()

print(CHAPTER_PREFIX + '正确关闭文件')
with open('test.txt', 'r') as f:
    content = f.readlines()
    for line in content:
        print(line)


def add(x, y, func):
    return func(x) + func(y)


print(CHAPTER_PREFIX + '把函数作为参数')
print(add(-5, 9, abs))

print(CHAPTER_PREFIX + 'map()函数')


def square(x):
    return x * x


square_list = []
for item in map(square, [1, 2, 3, 4, 5, 6, 7, 8, 9]):
    square_list.append(item)
print(square_list)

print(CHAPTER_PREFIX + 'reduce()函数')


def reduce_func(x, y):
    return x + y


print(reduce(reduce_func, [1, 3, 5, 7, 9]))  # ==> 25
print(reduce(reduce_func, [1, 3, 5, 7, 9], 100))  # ==> 125

print(CHAPTER_PREFIX + 'filter()函数')


def is_odd(x):
    return x % 2 == 0


for item in filter(is_odd, [1, 6, 7, 9, 12, 17]):
    print(item)


def is_not_empty(filter_str):
    return filter_str and len(filter_str.strip()) > 0


for item in filter(is_not_empty, ['test', None, '', 'str', '  ', 'END']):
    print(item)

print(CHAPTER_PREFIX + '自定义排序函数')
print(sorted([36, 5, 12, 9, 21]))
score = [('Alice', 72), ('Candy', 90), ('Bob', 62)]
print(sorted(score))


def sorted_score(item_score):
    return item_score[1]  # ==> 按成绩排序，成绩是第二个字段


print(sorted(score, key=sorted_score, reverse=True))

print(CHAPTER_PREFIX + '返回函数')


def call_func():
    def sub_func():  # 定义子函数
        print('call sub_func.')

    sub_func()


call_func()


def calc_sum(list_):
    def lazy_sum():
        return sum(list_)

    return lazy_sum


calc_sum_func = calc_sum([1, 2, 3, 4])
print(calc_sum_func())

print(CHAPTER_PREFIX + '匿名函数')
result = [item for item in map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])]
print(result)  # ==> [1, 4, 9, 16, 25, 36, 49, 64, 81]
print(reduce(lambda x, y: x + y, [1, 3, 5, 7, 9]))

print(CHAPTER_PREFIX + '编写无参数的decorator')


def log(log_func):
    def fn(x):
        print('call ' + log_func.__name__ + '()...')
        return log_func(x)

    return fn


@log
def factorial(factorial_n):
    return reduce(lambda x, y: x * y, range(1, factorial_n + 1))


print(factorial(10))

print(CHAPTER_PREFIX + '编写有参数的decorator')


def log(prefix):
    def log_decorator(log_func):
        def wrapper(*args, **kw):
            print('[{}] {}()...'.format(prefix, log_func.__name__))
            return log_func(*args, **kw)

        return wrapper

    return log_decorator


@log('DEBUG')
def test():
    pass


test()

print(CHAPTER_PREFIX + '偏函数')
print(int('12345', base=8))
print(int('12345', 16))


def int2(x, base=2):
    return int(x, base)


print(int2('1000000'))
