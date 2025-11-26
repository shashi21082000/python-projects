import random

Computer = random.choice([1,-1,0])
My_Choice = input("Enter your choice: ")
My_Dict = {"stone":1,"paper":-1,"scissor":0}
My_Answer = My_Dict[My_Choice]

reverse_dict = {1:"stone",-1:"paper",0:"scissor"}

print(f"Computer chose {reverse_dict[Computer]} \n You chose {reverse_dict[My_Answer]}")

if Computer == My_Answer:
    print("It's a Draw")

else:
    if Computer == 1 and My_Answer == 0:
        print("You Lost")
    elif Computer == 1 and My_Answer == -1:
        print("You Won")
    elif Computer == -1 and My_Answer == 1:
        print("You Lost")
    elif Computer == -1 and My_Answer == 0:
        print("You Won")
    elif Computer == 0 and My_Answer == 1:
        print("You Won")
    elif Computer == 0 and My_Answer == -1:
        print("You Lost")
    else:
        print("Something Went Wrong")
    
