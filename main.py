def datetime():
    import datetime
    return datetime.datetime.now
date= str(datetime())
print("Hi, Welcome back to Health Management System\n")
print("Type 1, 2 or 3\n")
print("1. Lock customer diet/excercise")
print("2. Check history of customer diet/excercise")
print("3. Exit the program\n")
# while loop to not throw error if type 3+ number
while 1:
    # First Input
    in1=int(input())
    # If choose to Lock
    if in1 == 1:
        print("Please choose the customer\n")
        print("Type 1, 2 or 3\n")
        print("1. Huzaifa")
        print("2. Harry")
        print("3. Larry")
        while 1:
            # Choosing customer to lock
            in2=int(input())
            # Huzaifa lock
            if in2==1:
                # Choose Huzaifa Lock Excercise or Diet
                print("Please choose the One\n")
                print("Type 1 or 2\n")
                while 1:
                    print("1. Diet")
                    print("2. Excercise")
                    in3=int(input())
                    # Diet lock Huzaifa
                    if in3==1:
                        print("Please enter the one you want to lock")
                        in4=input()
                        with open("huzaifa_food.txt","r+") as f:
                            f.write(date)
                            f.write(in4)
                            f.write("\n")
                        break
                    
                    elif in3==2:
                        print("Please enter the one you want to lock")
                        in4=input()
                        with open("huzaifa_excercise.txt","r+") as f:
                            f.write(date)
                            f.write(in4)
                            f.write("\n")
                        break
                    else:
                        print("Please re type the number from 1 to 3")
                        
            # Harry lock
            elif in2 ==2:
                # Choose Huzaifa Lock Excercise or Diet
                print("Please choose the One\n")
                print("Type 1 or 2\n")
                while 1:
                    print("1. Diet")
                    print("2. Excercise")
                    in3=int(input())
                    # Diet lock Huzaifa
                    if in3==1:
                        print("Please enter the one you want to lock")
                        in4=input()
                        with open("huzaifa_food.txt","r+") as f:
                            f.write(date)
                            f.write(in4)
                            f.write("\n")
                        break
                    
                    elif in3==2:
                        print("Please enter the one you want to lock")
                        in4=input()
                        with open("huzaifa_excercise.txt","r+") as f:
                            f.write(date)
                            f.write(in4)
                            f.write("\n")
                        break
                    else:
                        print("Please re type the number from 1 to 3")
                
            # Larry lock
            elif in2 ==3:
                # Choose Huzaifa Lock Excercise or Diet
                print("Please choose the One\n")
                print("Type 1 or 2\n")
                while 1:
                    print("1. Diet")
                    print("2. Excercise")
                    in3=int(input())
                    # Diet lock Huzaifa
                    if in3==1:
                        print("Please enter the one you want to lock")
                        in4=input()
                        with open("huzaifa_food.txt","r+") as f:
                            f.write(date)
                            f.write(in4)
                            f.write("\n")
                        break
                    
                    elif in3==2:
                        print("Please enter the one you want to lock")
                        in4=input()
                        with open("huzaifa_excercise.txt","r+") as f:
                            f.write(date)
                            f.write(in4)
                            f.write("\n")
                        break
                    else:
                        print("Please re type the number from 1 to 3")
        
            else:
                print("Please re type the number from 1 to 3")
        continue
    # If choose history
    elif in1 ==2:
        print("Please choose the customer\n")
        print("Type 1, 2 or 3\n")
        print("1. Huzaifa")
        print("2. Harry")
        print("3. Larry")
        while 1:
            # Choosing customer to lock
            in2=int(input())
            # Huzaifa lock
            if in2==1:
                # Choose Excercise or Diet for Huzaifa history
                print("Please choose the One\n")
                print("Type 1 or 2\n")
                while 1:
                    print("1. Diet")
                    print("2. Excercise")
                    in3=int(input())
                    # Diet history Huzaifa
                    if in3==1:
                        with open("huzaifa_food.txt","r") as f:
                            print(f.read())
                        break
                    
                    elif in3==2:
                        with open("huzaifa_excercise.txt","r") as f:
                            print(f.read())
                        break
                    else:
                        print("Please re type the number from 1 to 3")
                        
            # Harry lock
            elif in2 ==3:
                # Choose Excercise or Diet for harry history
                print("Please choose the One\n")
                print("Type 1 or 2\n")
                while 1:
                    print("1. Diet")
                    print("2. Excercise")
                    in3=int(input())
                    # Diet History harry
                    if in3==1:
                        with open("harry_food.txt","r") as f:
                            print(f.read())
                        break
                    
                    elif in3==2:
                        with open("harry_excercise.txt","r") as f:
                            print(f.read())
                        break
                    else:
                        print("Please re type the number from 1 to 3")
                
            # Larry lock
            elif in2 ==3:
                # Choose Excercise or Diet for larry history
                print("Please choose the One\n")
                print("Type 1 or 2\n")
                while 1:
                    print("1. Diet")
                    print("2. Excercise")
                    in3=int(input())
                    # Diet History Larry
                    if in3==1:
                        with open("larry_food.txt","r") as f:
                            print(f.read())
                        break
                    
                    elif in3==2:
                        with open("larry_excercise.txt","r") as f:
                            print(f.read())
                        break
                    else:
                        print("Please re type the number from 1 to 3")
        
            else:
                print("Please re type the number from 1 to 3")
        continue
    # For wrong number choosing
    elif in1==3:
        break
    else:
        print("Please re type the number from 1 to 3")
        continue
