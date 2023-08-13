x = "Welcome!! to Quiz Club"
print(x.center(75))
user = input("What is your name? : ")
print("Hello!!", user)
print("Can I start the game?")
while True:
    start = input("Press Y/N : ")
    if start == "Y":
        print("Ok! The game will Start...")
        break
    elif start == "N":
        break
    else:
        print("Invalid Input!!!!")
        print("Please run the code again")
print("Here is your first question")
score = 0
x = ('Which planet is known as the "Red Planet"?','A) Earth','B) Mars','C) Jupiter','D) Venus')
for i in x:
    print(i)
first_ans = input("Ans: ")    
if first_ans=="Mars":
    print("Correct ans!! ")  
    score +=1
else:
    print("Wrong ans!!")
y = ('What is the largest mammal in the world?','A) Elephant','B) Blue Whale','C) Giraffe','D) Polar Bear')
for f in y:
    print(f)
second_ans = input("Ans: ")
if second_ans== 'Blue Whale':
    print("Correct Ans!!")
    score +=1
else:
    print("Wrong Ans!!!")
z =('Which famous scientist developed the theory of relativity?','A) Isaac Newton','B) Galileo Galilei','C) Albert Einstein','D) Nikola Tesla')  
for m in z:
    print(m)
third_ans = input("Ans: ")
if third_ans=="Albert Einstein":
    print("Correct ans!!")
    score +=1
else:
    print("Wrong ans!!")
h = ('What is the capital city of France?','A) London','B) Berlin','C) Rome','D) Paris')
for t in h:
    print(t)
fourth_ans = input("Ans: ")  
if fourth_ans=='Paris':
    print("Correct ans!!")
    score +=1
else:
    print("Wrong ans!!!")
j = ('Which famous artist painted the Mona Lisa?','A) Vincent van Gogh','B) Pablo Picasso','C) Leonardo da Vinci','D) Michelangelo')  
for o in j:
    print(o)
fifth_ans = input("Ans: ")
if fifth_ans=="Leonardo da Vinci":
    print("Correct ans!!!")
    score +=1
else:
    print("Wrong ans!!!")
print("Your Total score is ",score)                                                    