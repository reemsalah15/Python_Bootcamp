#Write your code below this line 👇

def prime_checker(number):
    flag = 0
    if number == 1:
            flag = 1
    for n in range(2,number): 
        
        if number % n == 0 :
            flag = 1
    if flag == 1:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")

               
  

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
