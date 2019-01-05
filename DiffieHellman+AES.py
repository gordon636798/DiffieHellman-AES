# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 16:12:53 2018

@author: gordon
"""

from gmpy2 import *
from Crypto.Cipher import AES
import hashlib
a=mpz(11) #原根
q=mpz(1040699159) #質數


class user:
# 使用者都共用a、q ， 選擇任意小於q的數當X當私鑰並求出準備給對方的Y
# 其中Y=(a^X)mod q
    def __init__(self,name,a,q):
        self.name = name
        self.a = a
        self.q = q
        self.__X = mpz_random(random_state(),q)
        self.Y = powmod(self.a,self.__X,self.q)
        self.__key = {} #DiffieHellman為1對1的通訊故需要紀錄與多個使用者的common key
        
#接收到對方的Y後開始計算雙方的common key，key = (Yb^X)mod q ; Yb為對方的Y  
    def commonKey(self, _user, Yb):
        key = powmod(self.Y,self.__X,self.q)
        key = int(key).to_bytes(len(key)//4+1,byteorder='big') #由數字進行編碼
        key = hashlib.sha256(key) #為保證AES的KEY長度固定所以塞進SHA256
        key = key.digest()
        print(self.name+' : \n'+ key.hex())
        self.__key[_user.name] = key #放進key storage

#AES 加密
    def AES_encrypt(self, _user, data):
        data = data.encode('utf-8')  #編碼將字串轉bytes
        padding = 16 - len(data) % 16 #AES為block ciper，須將明文鋪滿為128 bits
        if padding == 0 :   #缺3個bytes 就補3個 /x03 
            padding = 16
        P = bytes([padding])
        data += padding*(P)
        cryptor = AES.new(self.__key[_user.name],AES.MODE_CBC , 16*'\x00') #選擇block的模式和設定IV
        cip = cryptor.encrypt(data)
        print('cipher : \n'+ cip.hex())
        return [cip , self.name]  #回傳秘文和加密者的名

#AES 解密    
    def AES_decrypt(self, cip):
        data,name = cip[0],cip[1] #解析分出密文和加密者
        cryptor = AES.new(self.__key[name], AES.MODE_CBC,16*'\x00') #使用與加密者的common key
        plain = cryptor.decrypt(data)
        plain = plain[:(16-plain[-1])] #解密時將當初的padding給去掉 
        plain = plain.decode('utf-8')
        print('plain from ' +name+' : \n'+ plain)
        return plain
           
Alice = user('Alice', a , q) #建立Alice
Bob = user('Bob', a , q) #建立Bob

Alice.commonKey(Bob,Bob.Y) #收到彼此的Y之後算K = Y^X
Bob.commonKey(Alice,Alice.Y)        

cip = Alice.AES_encrypt(Bob,'白癡喔') #Alice對Bob送出 "你白癡喔" 並進行加密
plain = Bob.AES_decrypt(cip) #Bob從Alice收到密文進行解密





