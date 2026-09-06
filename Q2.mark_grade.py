subjects = int(input("Enter number of subjects: ")) 
total_mark = 0   
for i in range(subjects):  
       sub_mark = float(input(f"Enter marks for subject {i + 1}: "))
       total_mark = total_mark + sub_mark

percentage = total_mark / subjects 

if percentage >= 90:
    grade = "A+" 
elif percentage >= 80:   
    grade = "A"
elif percentage >= 70: 
    grade = "B" 
elif percentage >= 60: 
    grade = "C" 
elif percentage >= 40: 
    grade = "D" 
else:   
    grade = "F"  

print("Total Marks:", total_mark)
print("Percentage:", percentage)
print("Grade:", grade) 