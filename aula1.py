a = 10  # int
b = "palavra"  # string
bb = b"bytearray"  # byte
c = 3.4  # float
d = True  # bool
e = False  # bool
f = None  # null

l = [1, 2]    # list() - ordem garantida - add/del
l[0]
t = (1, 2)    # tuple() - ordem garantida - imutavel
t[1]
o = {'a': 1, 'b': 2}  # dict() - chave/valor - O(1) - sem ordem
o['a']

s = {1, 2}    # set() - chave - 0(1) - sem ordem

complexo = [
    (1, 2, 3),
    {'a': [2, 3, 4]},
    ({2: 3},)
]

achou = complexo[1]['a'][2] == 4
