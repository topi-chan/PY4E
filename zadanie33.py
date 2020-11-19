#Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print
#an error. If the score is between 0.0 and 1.0, print a grade using the following table:
#Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
#If the user enters a value out of range, print a suitable error message and exit. For the test,
#enter a score of 0.85.

score = input("Enter Score: ")
scorex = float(score)
if scorex <= 0.0:
    print('Error!')
    quit()
elif scorex >= 1.0:
    print('Error!')
    quit()
elif scorex >= 0.9 and scorex < 1.0:
    print('A')
    quit()
elif scorex >= 0.8 and scorex < 0.9:
    print('B')
    quit()
elif scorex >= 0.7 and scorex < 0.8:
    print('C')
    quit()
elif scorex >= 0.6 and scorex < 0.7:
    print('D')
    quit()
else:
    print('F')
    quit()
