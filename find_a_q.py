from gmpy2 import *

#隨機生成一個數rand
rand=mpz_rrandomb(random_state(),9)
print("random number ",end='')
print(rand)

#rand的下一個質數
q=next_prime(rand)
print("prime number ",end='')
print(q)
    
def find_a():

     for i in range(1,q): #i的j次方找原根
        for j in range(1,q):
            if powmod(i,j,q)==1 and j<q-1:
                break
            elif powmod(i,j,q)==1 and j==q-1:
                a=i
                return a
print(find_a())
