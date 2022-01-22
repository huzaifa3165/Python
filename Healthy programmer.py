#<----------Import Section----------->
from pygame import mixer
import time
#<----------Define Section----------->
def time_to_min(hour, minute):
    return hour*60+minute
def that_time():
    return time.asctime(time.localtime(time.time()))
def player(file,stopper):
        mixer.init()
        # Loading the song
        mixer.music.load(file)

        # Setting the volume
        mixer.music.set_volume(100)

        # Start playing the song
        mixer.music.play()
        a=input()
        while True:
            if a == stopper:
                mixer.music.stop()
                with open("log detail.txt","a") as f:
                    f.write(f"{file}\b\b\b at {that_time()}\n")
                break

#<----------Variables Section----------->
timenow = time.localtime()

t9 = time_to_min(9, 0)
t9_3 = time_to_min(9, 30)
t10 = time_to_min(10, 0)
t10_3 = time_to_min(10, 30)
t11 = time_to_min(11, 0)
t11_3 = time_to_min(11, 30)
t12 = time_to_min(12, 0)
t12_3 = time_to_min(12, 30)
t13 = time_to_min(13, 0)
t13_3 = time_to_min(13, 30)
t14 = time_to_min(14, 0)
t14_3 = time_to_min(14, 30)
t15 = time_to_min(15, 0)
t15_3 = time_to_min(15, 30)
t16 = time_to_min(16, 0)
t16_3 = time_to_min(16, 30)
t17 = time_to_min(17, 0)
tc = time_to_min(timenow.tm_hour, timenow.tm_min)

#<----------Logic Section----------->
if __name__ == "__main__":
    print("Welcome to the healthy programmer software\n")
    print("s -- start program")
    print("l -- view log")
    print("any key -- close program\n")
    firstin=input()
    if firstin=="s":
        while 1:
                if tc==t9:
                    print("Drink some water and type done")
                    player("water.mp3","done")
                    print("Do exercise and type done")
                    player("physical.mp3","done")
                    print("Give rest to eyes and type done")
                    player("eyes.mp3","done")
                if tc==t9_3:
                    print("Do exercise and type done")
                    player("physical.mp3","done")
                    print("Give rest to eyes and type done")
                    player("eyes.mp3","done")
                if tc==t10:
                    print("Drink some water and type done")
                    player("water.mp3","done")
                    print("Do exercise and type done")
                    player("physical.mp3","done")
                    print("Give rest to eyes and type done")
                    player("eyes.mp3","done")
                if tc==t10_3:
                    print("Do exercise and type done")
                    player("physical.mp3","done")
                    print("Give rest to eyes and type done")
                    player("eyes.mp3","done")
                if tc==t11:
                    print("Drink some water and type done")
                    player("water.mp3","done")
                    print("Do exercise and type done")
                    player("physical.mp3","done")
                    print("Give rest to eyes and type done")
                    player("eyes.mp3","done")
                if tc==t11_3:
                    print("Do exercise and type done")
                    player("physical.mp3","done")
                    print("Give rest to eyes and type done")
                    player("eyes.mp3","done")
                if tc==t12:
                    print("Drink some water and type done")
                    player("water.mp3","done")
                    print("Do exercise and type done")
                    player("physical.mp3","done")
                    print("Give rest to eyes and type done")
                    player("eyes.mp3","done")
                if tc==t12_3:
                    print("Do exercise and type done")
                    player("physical.mp3","done")
                    print("Give rest to eyes and type done")
                    player("eyes.mp3","done")
                if tc==t13:
                    print("Drink some water and type done")
                    player("water.mp3","done")
                    print("Do exercise and type done")
                    player("physical.mp3","done")
                    print("Give rest to eyes and type done")
                    player("eyes.mp3","done")
                if tc==t13_3:
                    print("Do exercise and type done")
                    player("physical.mp3","done")
                    print("Give rest to eyes and type done")
                    player("eyes.mp3","done")
                if tc==t14:
                    print("Drink some water and type done")
                    player("water.mp3","done")
                    print("Do exercise and type done")
                    player("physical.mp3","done")
                    print("Give rest to eyes and type done")
                    player("eyes.mp3","done")
                if tc==t14_3:
                    print("Do exercise and type done")
                    player("physical.mp3","done")
                    print("Give rest to eyes and type done")
                    player("eyes.mp3","done")
                if tc==t15:
                    print("Drink some water and type done")
                    player("water.mp3","done")
                    print("Do exercise and type done")
                    player("physical.mp3","done")
                    print("Give rest to eyes and type done")
                    player("eyes.mp3","done")
                if tc==t15_3:
                    print("Do exercise and type done")
                    player("physical.mp3","done")
                    print("Give rest to eyes and type done")
                    player("eyes.mp3","done")
                if tc==t16:
                    print("Drink some water and type done")
                    player("water.mp3","done")
                    print("Do exercise and type done")
                    player("physical.mp3","done")
                    print("Give rest to eyes and type done")
                    player("eyes.mp3","done")
                if tc==t16_3:
                    print("Do exercise and type done")
                    player("physical.mp3","done")
                    print("Give rest to eyes and type done")
                    player("eyes.mp3","done")
                if tc==t17:
                    print("Drink some water and type done")
                    player("water.mp3","done")
                    print("Do exercise and type done")
                    player("physical.mp3","done")
                    print("Give rest to eyes and type done")
                    player("eyes.mp3","done")
    elif firstin=="l":
        with open("log detail.txt") as f:
            f.read()
