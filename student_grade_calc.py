def calculate_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >=70:
        return "C"
    elif percentage >=60:
        return "D"
    else:
        return "F"

name=input("\nEnter  Student Name : ")
marks=[]
for i in range(5):
    mark=float(input(f"\nEnter Marks For  Subject {i + 1}:"))
    marks.append(mark)
total=sum(marks)
percentage=total/5
grade =calculate_grade(percentage)
if percentage >= 40:
    result="Pass"
else:
    result="Fail"
print("\n==========Student Result==========")
print(f"Name: {name}")
print(f"Marks:{marks}")
print(f"Total: {total}/500")
print(f"percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
print(f"Result: {result}")





