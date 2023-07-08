# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

len_names=len(names)
random_index=random.randint(0,len_names-1)
print(f"{names[random_index]} is going to buy the meal today!")
