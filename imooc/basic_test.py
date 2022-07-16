# https://www.imooc.com/learn/1261
CHAPTER_PREFIX = '=' * 50 + '> '
L = ['Alice', 'Bob', 'David', 'Elena', 66, True, 'False', 100]
print(CHAPTER_PREFIX + '按顺序访问list')
for item in L:
    print(item)

print(CHAPTER_PREFIX + '按索引访问list')
print(L[4])
sub_names = L[0:2]
print(sub_names)

print(CHAPTER_PREFIX + '倒序访问list')
print(L[-1])
print(L[-5])

print(CHAPTER_PREFIX + '向list添加新的元素')
# append()方法总是将元素添加到list的尾部
L.append('Candy')
print(L)
L.insert(2, 'Candy')
print(L)

print(CHAPTER_PREFIX + '从list删除元素')
del_name = L.pop()
print(del_name)
print(L)
third_name = L.pop(2)
print(third_name)
print(L)

print(CHAPTER_PREFIX + '替换list中的元素')
L[2] = 'John'
print(L)

print(CHAPTER_PREFIX + '二维list')
alice_scores = [100, 89, 92]
bob_scores = [70, 65, 81]
candy_scores = [88, 72, 77]
all_scores = [alice_scores, bob_scores, candy_scores]
print(all_scores)  # ==> [[100, 89, 92], [70, 65, 81], [88, 72, 77]]

T = ('Alice', 'Bob', 'Candy', 'David', 'Elena')
print(CHAPTER_PREFIX + '什么是tuple')
# 通过下标的方式访问元素
print(T[0])  # ==> Alice
print(T[4])  # ==> Elena
# 切片
print(T[1:3])  # ==> ('Bob', 'Candy')

print(CHAPTER_PREFIX + 'tuple -> list')
print(T)  # ==> ('Alice', 'Bob', 'Candy', 'David', 'Elena')
T2L = list(T)
print(T2L)  # ==> ['Alice', 'Bob', 'Candy', 'David', 'Elena']
print(CHAPTER_PREFIX + 'list -> tuple')
L2T = tuple(T2L)
print(L2T)

print(CHAPTER_PREFIX + '访问tuple元素的其他方法')
print(T.count('Alice'))  # ==> 1
print(T.index('Alice'))  # ==> 0

print(CHAPTER_PREFIX + '创建单个元素的tuple')
T = ()
print(T)  # ==> ()
T = (1)
print(T)  # ==> 1
T = (1,)
print(T)  # ==> (1, )

print(CHAPTER_PREFIX + '可变的tuple')
T = (1, 'CH', [3, 4])
L = T[2]
print(L)  # ==> [3, 4]
# 尝试替换L中的元素
L[1] = 40
print(L)  # ==> [3, 40]
print(T)  # ==> (1, 'CH', [3, 40])

d = {
    'Alice': 45,
    'Bob': 60,
    'Candy': 75,
    'David': 86,
    'Elena': 49
}
print(CHAPTER_PREFIX + '读取dict元素')
print(d)
print(d.get('Alice'))  # ==> 45
print(d.get('Dodo'))  # ==> None

print(CHAPTER_PREFIX + '添加dict元素')
d['Dodo'] = 88
print(d)
d['Dodo'] = [88, 90]
print(d)

print(CHAPTER_PREFIX + '更新dict元素')
d['Bob'] = 55
print(d)

print(CHAPTER_PREFIX + '删除dict元素')
dodo_score = d.pop('Dodo')
print(dodo_score)  # ==> [88, 90]
print(d)
name = 'Elena'
if name in d.keys():
    d.pop(name)
else:
    print('{} not in d'.format(name))
print(d)

print(CHAPTER_PREFIX + '遍历dict')
# 遍历d的key
for key in d:
    value = d[key]
    if value > 60:
        print(key, value)
# ==> Candy 75
# ==> David 86
for key, value in d.items():
    if value > 60:
        print(key, value)
# ==> Candy 75
# ==> David 86

print(CHAPTER_PREFIX + '获取dict的所有key')
for key in d.keys():
    print(key)
print(CHAPTER_PREFIX + '获取dict所有的value')
for key in d.values():
    print(key)
print(CHAPTER_PREFIX + '清除所有元素')
d.clear()
print(d)  # ==> {}

print(CHAPTER_PREFIX + '什么是set')
L = [1, 4, 3, 2, 5, 4, 2, 3, 1]
s = set(L)
print(s)  # ==> {1, 2, 3, 4, 5}

print(CHAPTER_PREFIX + '读取set元素')
names = ['Alice', 'Bob', 'Candy', 'David', 'Elena']
name_set = set(names)
print('Alice' in name_set)  # ==> True
print('Bobby' in name_set)  # ==> False

print(CHAPTER_PREFIX + '添加set元素')
name_set.add('Gina')
print(name_set)  # ==> set(['Gina', 'Alice', 'Candy', 'David', 'Elena', 'Bob'])
new_names = ['Hally', 'Isen', 'Jenny', 'Karl']
name_set.update(new_names)  # ==> set(['Jenny', 'Elena', 'Alice', 'Candy', 'David', 'Hally', 'Bob', 'Isen', 'Karl'])
print(name_set)

print(CHAPTER_PREFIX + '删除set元素')
name_set.remove('Jenny')
print(name_set)  # ==> set(['Elena', 'Alice', 'Candy', 'David', 'Hally', 'Bob', 'Isen', 'Karl'])

print(CHAPTER_PREFIX + '不会报错的删除方法discard()')
name_set.discard('Jenny')
print(name_set)  # ==> set(['Elena', 'Alice', 'Candy', 'David', 'Hally', 'Bob', 'Isen', 'Karl'])

print(CHAPTER_PREFIX + '清除所有元素的方法clear()')
name_set.clear()
print(name_set)  # ==> set([])

print(CHAPTER_PREFIX + '集合的子集和超集')
s1 = {1, 2, 3, 4, 5}
s2 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# 判断s1是否为s2的子集
print(s1.issubset(s2))  # ==> True
# 判断s2是否为s1的超集
print(s2.issuperset(s1))  # ==> True

print(CHAPTER_PREFIX + '判断集合是否重合')
print(s1.isdisjoint(s2))  # ==> False，因为有重复元素1、2、3、4、5

print(CHAPTER_PREFIX + '函数参数')
print(isinstance(100, int))  # ==> True
print(isinstance(100.0, int))  # ==> False
print(isinstance('3.1415926', str))  # ==> True

print(CHAPTER_PREFIX + '函数使用可变参数')


def func(*args):
    print('args length = {}, args = {}'.format(len(args), args))


func('a')  # ==> args length = 1, args = ('a',)
func('a', 'b')  # ==> args length = 2, args = ('a', 'b')
func('a', 'b', 'c')  # ==> args length = 3, args = ('a', 'b', 'c')

print(CHAPTER_PREFIX + '函数使用可变关键字参数')


def info(**kwargs):
    print('name: {}, gender: {}, age: {}'.format(kwargs.get('name'), kwargs.get('gender'), kwargs.get('age')))


info(name='Alice', gender='girl', age=16)


def func(param1, param2, param3=None, *args, **kwargs):
    print(param1)
    print(param2)
    print(param3)
    print(args)
    print(kwargs)


func(100, 200, 300, 400, 500, name='Alice', score=100)
# ==> 100
# ==> 200
# ==> 300
# ==> (400, 500)
# ==> {'name': 'Alice', 'score': 100}
