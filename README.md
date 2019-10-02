# DiffieHellman-AES

DiffieHellman-AES
實作DiffieHellman部分 AES利用library實現
將兩者結合

Alice = user('Alice', a , q) #建立Alice
Bob = user('Bob', a , q) #建立Bob

Alice.commonKey(Bob,Bob.Y) #收到彼此的Y之後算K = Y^X
Bob.commonKey(Alice,Alice.Y)        

cip = Alice.AES_encrypt(Bob,data) #Alice對Bob送出 "你白癡喔" 並進行加密
plain = Bob.AES_decrypt(cip) #Bob從Alice收到密文進行解密
