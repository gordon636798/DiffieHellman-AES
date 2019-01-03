# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 16:12:53 2018

@author: gordon
"""

from gmpy2 import *
from Crypto.Cipher import AES
import hashlib
a=mpz(3)
q=mpz(353)

class user:
    def __init__(self,name,a,q):
        self.name = name
        self.a = a
        self.q = q
        self.__X = mpz_random(random_state(),q)
        self.Y = powmod(self.a,self.__X,self.q)
        self.__key = {}
    
    def commonKey(self, _user, Yb):
        key = powmod(self.Y,self.__X,self.q)
        key = int(key).to_bytes(len(key)//4+1,byteorder='big')
        key = hashlib.sha256(key)
        key = key.digest()
        print(self.name+' : \n'+ key.hex())
        self.__key[_user.name] = key
    def AES_encrypt(self, _user, data):
        data = data.encode('utf-8')
        padding = 16 - len(data) % 16
        if padding == 0 :
            padding = 16
        P = bytes([padding])
        data += padding*(P)
        cryptor = AES.new(self.__key[_user.name],AES.MODE_CBC , 16*'\x00')
        cip = cryptor.encrypt(data)
        print('cipher : \n'+ cip.hex())
        return [cip , self.name] 
    
    def AES_decrypt(self, cip):
        data,name = cip[0],cip[1]
        cryptor = AES.new(self.__key[name], AES.MODE_CBC,16*'\x00')
        plain = cryptor.decrypt(data)
        plain = plain[:(16-plain[-1])]
        plain = plain.decode('utf-8')
        print('plain from ' +name+' : \n'+ plain)
        return plain
           
Alice = user('Alice', a , q)
Bob = user('Bob', a , q)

Alice.commonKey(Bob,Bob.Y)
Bob.commonKey(Alice,Alice.Y)        

cip = Alice.AES_encrypt(Bob,'白癡喔')
plain = Bob.AES_decrypt(cip)





