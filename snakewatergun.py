import random
swglist=["snake","water","gun"]
comput=random.choice(swglist)
y=0
x=0
w=10
print("Welcome to the Huzaifa Game Zone")
print(f"You have total {w} chance")
while 1:
    inp=input("Choose snake, water or gun (Type s/w/g)\n")
    if w==0:
        break
    else:
        if inp=="s" and comput=="snake":
            print(f"Both tie as computer choosed {comput} \n")
            w=w-1
            print(f"{w} chances left")
            print(f"You won {y} times")
            print(f"Computer won {x} times\n")
            continue
        elif inp=="w" and comput=="water":
            print(f"Both tie as computer choosed {comput} \n")
            w=w-1
            print(f"{w} chances left")
            print(f"You won {y} times")
            print(f"Computer won {x} times\n")
            continue
        elif inp=="g" and comput=="gun":
            print(f"Both tie as computer choosed {comput} \n")
            w=w-1
            print(f"{w} chances left")
            print(f"You won {y} times")
            print(f"Computer won {x} times\n")
            continue
        elif inp=="s" and comput=="water":
            print(f"You win as computer choosed {comput} \n")
            w=w-1
            y=y+1
            print(f"{w} chances left")
            print(f"You won {y} times")
            print(f"Computer won {x} times\n")
            continue
        elif inp=="w" and comput=="gun":
            print(f"You win as computer choosed {comput} \n")
            w=w-1
            y=y+1
            print(f"{w} chances left")
            print(f"You won {y} times")
            print(f"Computer won {x} times\n")
            continue
        elif inp=="g" and comput=="snake":
            print(f"You win as computer choosed {comput} \n")
            w=w-1
            y=y+1
            print(f"{w} chances left")
            print(f"You won {y} times")
            print(f"Computer won {x} times\n")
            continue
        elif inp=="s" and comput=="gun":
            print(f"You Lose as computer choosed {comput} \n")
            w=w-1
            x=x+1
            print(f"{w} chances left")
            print(f"You won {y} times")
            print(f"Computer won {x} times\n")
            continue
        elif inp=="w" and comput=="snake":
            print(f"You Lose as computer choosed {comput} \n")
            w=w-1
            x=x+1
            print(f"{w} chances left")
            print(f"You won {y} times")
            print(f"Computer won {x} times\n")
            continue
        elif inp=="g" and comput=="water":
            print(f"You Lose as computer choosed {comput} \n")
            w=w-1
            x=x+1
            print(f"{w} chances left")
            print(f"You won {y} times")
            print(f"Computer won {x} times\n")
            continue
        else:
            print("Please choose from s/w/g only")
            continue