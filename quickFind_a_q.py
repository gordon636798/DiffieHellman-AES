from gmpy2 import *
import gmpy2
#隨機生成一個數rand，並顯示出
rand=mpz_rrandomb(random_state(),256)
print("random number ",end='')
print(rand)

#找rand的下一個質數q，並顯示出
q=next_prime(rand)
print("prime number ",end='')
print(q)
    
def find_a():

     for i in range(2,q): #從2到q-1之間找原根
        for j in range(2,f_div(q-1,2)+1): #從2~(q-1)/2之間找出q-1的質因數
            
            #如果j是q-1的質因數且找到i的(q-1)/j次方mod q=1，代表這個i不是原根
            if f_mod(q-1,j)==0 and is_prime(j) and powmod(i ,f_div(q-1,j), q)==1:
                break
            
            #如果2~(q-1)/2之間沒有找到上述的話，代表這個i是原根
            elif j==f_div(q-1,2):
                return i
           
print(find_a())
