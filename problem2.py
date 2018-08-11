#Algorithm derived from Sieve of Atkin wiki page http://en.wikipedia.org/wiki/Sieve_of_Atkin. 
# The 10000th prime number is 104729

import math

#uses Sieve of Atkin algorithm to find all prime numbers up to a specific integer. 
def findPrimesUpTo(limit):
    
    #create a results list, filled with 2, 3, and 5
    primesList = [2,3,5]

    #create a sieve list with entry for each positive integer; all entries of this list should initially be marked non prime (False)
    sieveList=[False]*(limit+1)
    
    #Put in candidate primes: integers which have an odd number of representations by certain quadratic forms.
    for x in range(1, int(math.sqrt(limit))+1):
        for y in range(1, int(math.sqrt(limit))+1):
            
            #for each entry number n where n=4x^2+y^2 with modulo-sixty remainder r, if r is 1, 13, 17, 29, 37, 41, 49, 53... (also works out to n%12==1 or n%12==5), flip the boolean in sieveList[n]
            n = 4*x**2 + y**2
            if n<=limit and (n%12==1 or n%12==5): 
                sieveList[n] = not sieveList[n]

            #for each entry number n where n=3x^2+y^2 with modulo-sixty remainder r, if r is 7, 19, 31, or 43...(also works out to n%12==7), flip the boolean in sieveList[n]
            n = 3*x**2+y**2
            if n<= limit and n%12==7: 
                sieveList[n] = not sieveList[n]

            #for each entry number n where n=4x^2+y^2 with modulo-sixty remainder r, if r is 11, 23, 47, or 59... (also works out to n%12==11), flip the boolean in sieveList[n]
            n = 3*x**2 - y**2
            if x>y and n<=limit and n%12==11: 
                sieveList[n] = not sieveList[n]
    
    #eliminate composites by sieving, only for those occurrences on the wheel
    for x in range(5,int(math.sqrt(limit))):
        if sieveList[x]:
            #square the next prime number and mark all multiples of that square as non prime. omit multiples of its square; this is sufficient because square-free composites can't get on this list
            for y in range(x**2,limit+1,x**2):
                sieveList[y] = False
    
    #iterate through the sieveList and each time a True boolean is detected, add index to primeslist
    for i in range(7,limit):
        if sieveList[i]: 
            primesList.append(i)
    return primesList


limit = 1000000
primes = findPrimesUpTo(limit)
l = len(primes)
if(l > 10000):
    print(primes[9999])
else: 
    print("not yet... increase limit")

#TEST
####################################
# print(findPrimesUpTo(60)) #[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]
# print(len(findPrimesUpTo(60))) #17