# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
sum = 0
num = 0

for student_height in student_heights: 
    sum += student_height
    num += 1
    
average=round(sum/num)
print(average)



