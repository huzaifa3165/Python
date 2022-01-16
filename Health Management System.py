import datetime
def getdate():
    return datetime.datetime.now()
dates= str(getdate())
print("Hi, Welcome back to Health Management System\n")
print("Type 1, 2 or 3\n")
print("1. Customer diet/excercise log")
print("2. Check retrieve of customer diet/excercise")
print("3. Exit the program\n")
# while loop to not throw error if type 3+ number
while 1:
    # First Input
    in1=int(input())
    # If choose to log
    if in1 == 1:
        print("Please choose the customer\n")
        print("Type 1, 2 or 3\n")
        print("1. Huzaifa")
        print("2. Subhan")
        print("3. Abu huraira")
        while 1:
            # Choosing customer to log
            in2=int(input())
            # Huzaifa log
            if in2==1:
                # Choose Huzaifa log Excercise or Diet
                print("Please choose the One\n")
                print("Type 1 or 2\n")
                while 1:
                    print("1. Diet")
                    print("2. Excercise")
                    in3=int(input())
                    # Diet log Huzaifa
                    if in3==1:
                        print("Please enter the one you want to log")
                        in4=input()
                        with open("huzaifa_food.txt","a") as f:
                            
                            
                            f.write(str([dates])+ ": "+in4+"\n")
                        print("Submitted successfully")
                        print("1. To add other log")
                        print("2. To close the program")
                        in5=input()
                        if in5==1:
                            continue
                        elif in5==2:
                            break
                        else:
                            print("Enter 1 or 2 only")
                    
                    elif in3==2:
                        print("Please enter the one you want to log")
                        in4=input()
                        with open("huzaifa_excercise.txt","a") as f:
                            
                            
                            f.write(str([dates])+ ": "+in4+"\n")
                        print("Submitted successfully")
                        print("1. To add other log")
                        print("2. To close the program")
                        in5=input()
                        if in5==1:
                            continue
                        elif in5==2:
                            break
                        else:
                            print("Enter 1 or 2 only")
                    else:
                        print("Please re type the number from 1 to 3")
                        
            # Subhan log
            elif in2 ==2:
                # Choose Huzaifa log Excercise or Diet
                print("Please choose the One\n")
                print("Type 1 or 2\n")
                while 1:
                    print("1. Diet")
                    print("2. Excercise")
                    in3=int(input())
                    # Diet log Huzaifa
                    if in3==1:
                        print("Please enter the one you want to log")
                        in4=input()
                        with open("huzaifa_food.txt","a") as f:
                            
                            
                            f.write(str([dates])+ ": "+in4+"\n")
                        print("Submitted successfully")
                        print("1. To add other log")
                        print("2. To close the program")
                        in5=input()
                        if in5==1:
                            continue
                        elif in5==2:
                            break
                        else:
                            print("Enter 1 or 2 only")
                    
                    elif in3==2:
                        print("Please enter the one you want to log")
                        in4=input()
                        with open("huzaifa_excercise.txt","a") as f:
                            
                            
                            f.write(str([dates])+ ": "+in4+"\n")
                        print("Submitted successfully")
                        print("1. To add other log")
                        print("2. To close the program")
                        in5=input()
                        if in5==1:
                            continue
                        elif in5==2:
                            break
                        else:
                            print("Enter 1 or 2 only")
                    else:
                        print("Please re type the number from 1 to 3")
                
            # Abu huraira log
            elif in2 ==3:
                # Choose Huzaifa log Excercise or Diet
                print("Please choose the One\n")
                print("Type 1 or 2\n")
                while 1:
                    print("1. Diet")
                    print("2. Excercise")
                    in3=int(input())
                    # Diet log Huzaifa
                    if in3==1:
                        print("Please enter the one you want to log")
                        in4=input()
                        with open("huzaifa_food.txt","a") as f:
                            
                            
                            f.write(str([dates])+ ": "+in4+"\n")
                        print("Submitted successfully")
                        print("1. To add other log")
                        print("2. To close the program")
                        in5=input()
                        if in5==1:
                            continue
                        elif in5==2:
                            break
                        else:
                            print("Enter 1 or 2 only")
                    
                    elif in3==2:
                        print("Please enter the one you want to log")
                        in4=input()
                        with open("huzaifa_excercise.txt","a") as f:
                            
                            
                            f.write(str([dates])+ ": "+in4+"\n")
                        print("Submitted successfully")
                        print("1. To add other log")
                        print("2. To close the program")
                        in5=input()
                        if in5==1:
                            continue
                        elif in5==2:
                            break
                        else:
                            print("Enter 1 or 2 only")
                    else:
                        print("Please re type the number from 1 to 3")
        
            else:
                print("Please re type the number from 1 to 3")
        continue
    # If choose retrieve
    elif in1 ==2:
        print("Please choose the customer\n")
        print("Type 1, 2 or 3\n")
        print("1. Huzaifa")
        print("2. Subhan")
        print("3. Abu huraira")
        while 1:
            # Choosing customer to retrieve
            in2=int(input())
            # Huzaifa retrieve
            if in2==1:
                # Choose Excercise or Diet for Huzaifa retrieve
                print("Please choose the One\n")
                print("Type 1 or 2\n")
                while 1:
                    print("1. Diet")
                    print("2. Excercise")
                    in3=int(input())
                    # Diet retrieve Huzaifa
                    if in3==1:
                        with open("huzaifa_food.txt") as f:
                            print(f.read())
                        break
                    
                    elif in3==2:
                        with open("huzaifa_excercise.txt") as f:
                            print(f.read())
                        break
                    else:
                        print("Please re type the number from 1 to 3")
                        
            # Subhan retrieve
            elif in2 ==3:
                # Choose Excercise or Diet for Subhan retrieve
                print("Please choose the One\n")
                print("Type 1 or 2\n")
                while 1:
                    print("1. Diet")
                    print("2. Excercise")
                    in3=int(input())
                    # Diet retrieve Subhan
                    if in3==1:
                        with open("Subhan_food.txt") as f:
                            print(f.read())
                        break
                    
                    elif in3==2:
                        with open("Subhan_excercise.txt") as f:
                            print(f.read())
                        break
                    else:
                        print("Please re type the number from 1 to 3")
                
            # Abu huraira retrieve
            elif in2 ==3:
                # Choose Excercise or Diet for Abu huraira retrieve
                print("Please choose the One\n")
                print("Type 1 or 2\n")
                while 1:
                    print("1. Diet")
                    print("2. Excercise")
                    in3=int(input())
                    # Diet retrieve Abu huraira
                    if in3==1:
                        with open("Abu huraira_food.txt") as f:
                            print(f.read())
                        break
                    
                    elif in3==2:
                        with open("Abu huraira_excercise.txt") as f:
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
