import numpy as numpy

dict1 = {
    (0, 0): 0,
    (0, 1): 0.5,
    (0, 2): 2.3
}
dict2 = {
    (1, 3): 34.23,
    (1, 0): 49.3,
    (1, 5): 13.43,
    (0, 0): 1.5
}
dict1.update(dict2)
print(dict1)
print(len(dict1))
dict3 = {}
if len(dict3) > 0:
    print("dict3 não está vazio")
else:
    print("dict3 vazio")
print(f"type {type(dict3)}")
print(f"tamanho {numpy.any(dict3) == True}")
print(dict3)
