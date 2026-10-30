score = 0

q1 = str(input("\nQ1: What is the capital of china?\nA. Beijing\nB. Ouagadougou\nC. Colombo\nD. Delhi\nEnter your answer: ")) # takes the input
if q1 == 'A': # takes the answer
    print("Correct")
    score = score + 1
else:
    print("Incorrect") # set because i have no fucking clue how this would work if i set the score to 0

q2 = str(input("\nQ2: What shape has 4 sides?\nA. Triangle\nB. Square\nC. Dodecahedron\nD. Oval\nEnter your answer: "))
if q2 == 'B':
    print("Correct")
    score = score + 1
else:
    print("Incorrect")

q3 = str(input("\nQ3: What is the derivative of f(x)=56/7?\nA. 8\nB. 14\nC. 0\nD. Infinity\nEnter your answer: "))
if q3 == 'B':
    print("Correct, +1 score")
    score = score + 1
else:
    print("Incorrect")


q4 = str(input("\nQ4: What is the equation of the equation of the universe?\nA. Kys\nB. f=ma\nC. (ȧa)2=8πG3kc2a2+Λc23open paren the fraction with numerator a dot and denominator a end-fraction close paren squared equals the fraction with numerator 8 pi cap G and denominator 3 end-fraction rho minus the fraction with numerator k c squared and denominator a squared end-fraction plus the fraction with numerator cap lambda c squared and denominator 3 end-fraction𝑎̇2=8𝜋𝐺3𝜌−𝑘𝑐2𝑎2+Λ𝑐23\nD. Infinity\nEnter your answer: "))
if q4 == 'A':
    print("Correct")
    score = score + 1
else:
    print("Incorrect")

q5 = str(input("\nQ5: Are you a robot?\nA. Yes\nB. Yes\nC. Yes\nD. Yes\nEnter your answer:  "))
if q5 == 'A':
    print("Correct, -1 score")
    score = score - 1
elif q5 == 'B':
    print("Correct, -1 score")
    score = score - 1
elif q5 == 'C':
    print("Correct, -1 score")
    score = score - 1
elif q5 == 'D':
    print("Correct, -1 score")
    score = score - 1
else:
    print("Error 404: Could not compute result")
    score = score - 9_223_372_036_854_775_808

print("Congratulations! You finished the test")
print("Your final score is ", score,"/5")
