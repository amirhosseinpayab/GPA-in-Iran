number = int(input("\nNumber of lessons : "))
total = 0
credit = 0
print("Tip : Score from 0 to 20")
for i in range(number):
  score = float(input(f"\nScore of lesson {i+1} : "))
  number_credit = float(input(f"Credit of lesson {i+1} : "))
  total += score * number_credit  
  credit += number_credit
term_rate = total / credit
gpa = ( term_rate * 4 ) / 20
print("\nYour term rate is %.2f "%term_rate)
if term_rate >= 16:
  print("Grade : A")
  print('Gpa : %.2f \n'%gpa)
elif term_rate>= 14 and term_rate<= 15.99:
  print("Grade : B")
  print('Gpa : %.2f \n'%gpa)
elif term_rate>= 12 and term_rate<= 13.99:
  print("Grade : C")
  print('Gpa : %.2f \n'%gpa)
elif term_rate>= 10 and term_rate <= 11.99:
  print("Grade : D")
  print('Gpa : %.2f \n'%gpa)
elif term_rate<10:
  print("Grade : F")
  print('Gpa : %.2f \n'%gpa)


  
