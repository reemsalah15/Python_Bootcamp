# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

l_nm1=name1.lower()
l_nm2=name2.lower()

nm1_count_T=l_nm1.count('t')
nm1_count_R=l_nm1.count('r')
nm1_count_U=l_nm1.count('u')
nm1_count_E=l_nm1.count('e')

nm2_count_T=l_nm2.count('t')
nm2_count_R=l_nm2.count('r')
nm2_count_U=l_nm2.count('u')
nm2_count_E=l_nm2.count('e')

nm1_count_L=l_nm1.count('l')
nm1_count_O=l_nm1.count('o')
nm1_count_V=l_nm1.count('v')
nm1_count_E=l_nm1.count('e')

nm2_count_L=l_nm2.count('l')
nm2_count_O=l_nm2.count('o')
nm2_count_V=l_nm2.count('v')
nm2_count_E=l_nm2.count('e')

total_TRUE = nm1_count_T+nm1_count_R+nm1_count_U+nm1_count_E+nm2_count_T+nm2_count_R+nm2_count_U+nm2_count_E
total_LOVE = nm1_count_L+nm1_count_O+nm1_count_V+nm1_count_E+nm2_count_L+nm2_count_O+nm2_count_V+nm2_count_E

score=str(total_TRUE)+str(total_LOVE)
love_score=int(score)

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score > 40 and love_score < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")

