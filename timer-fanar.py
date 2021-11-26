from time import sleep
from playsound import playsound

def start():
    long = int(input('how long > '))
    second = 1
    print('ready...\n')
    for wait in range(1,4):
        if wait == 3 :
            
            print(str(wait) + '\n')
            sleep(1)
            print('go\n')
        else:
            print(wait)
            sleep(1)
    for i in range (1 , long + 1 ):
        try:
            print(second , end = ' ')
            second += 1
            sleep(1)
        except KeyboardInterrupt:
            print('\nq for quite / enter for resume')
            status = input("Paused >")
            if status == 'q' :
                break
            else :
                continue
    playsound(r'F:\notification_sound\Windows_Xp__Turn_Off.mp3')
    
        
start()
