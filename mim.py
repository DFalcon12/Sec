from cryptography.fernet import Fernet
from Crypto.Util import number
import random   

g = 2
alice = random.getrandbits(256)
print(alice)
bob = random.getrandbits(256)
print(bob)
eve = random.getrandbits(256)
print(eve)
p = 2410312426921032588552076022197566074856950548502459942654116941958108831682612228890093858261341614673227141477904012196503648957050582631942730706805009223062734745341073406696246014589361659774041027169249453200378729434170325843778659198143763193776859869524088940195577346119843545301547043747207749969763750084308926339295559968882457872412993810129130294592999947926365264059284647209730384947211681434464714438488520940127459844288859336526896320919633919

A = pow(g,eve, p)
print(A)
E = pow(g, alice, p)
print(E)
B = pow(g, bob, p)
print(B)

s1 = pow(A, eve, p)
print(s1)
s2 = pow(E, alice, p)
print(s2)
s3 = pow(B, eve, p)
print(s3)
s4 = pow(E, bob, p)
print(s4)

if s1 != s3:
    print("Llaves incorrectas")


