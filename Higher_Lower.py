import random
from Informathion import inform
import os
import pic
def clear_console():


    os.system('cls')


def born(a,b):
    int(a)
    int(b)


    if a>b:
        return 'b'
    else:
        return 'a'



def check_ab(a,b,t):


    while t!='a' and t!='b':


        t=input(f"please type {a} or {b}: ").lower()
    return t



def check_yn(y,n,t):


    while t!='y' and t!='n':


        t=input(f"please type {y} or {n}: ").lower()
    return t

def rand_num():
    return random.randint(0, len(inform)-1)
clear_console()


print("Welcome to the game Higher or Lower. \nThe rules are simple, two historians will appear before you and you have to say who was born before whom.\nGood luck\n")



def Higher_Lower():


    count=0
    a=rand_num()


    while True:


        print(pic.logo)
        b=rand_num()
        while a==b:
            b=rand_num()


        print(f"Compare A:\033[1m{inform[a]['name']}\033[m, {inform[a]['description']}\n")


        print(pic.vs)


        print(f"Compare B:\033[1m{inform[b]['name']}\033[m, {inform[b]['description']}\n")


        answer=str(input("Who was born first? type a or b: ")).lower()


        answer=check_ab('a', 'b', answer)

        real=born(inform[a]['born'],inform[b]['born'])
        if real==answer:


            count+=1


            print("Very good")
            a=b
            clear_console()
        else:


            print(f"You lose your score is: {count}")
            return count



max_score=Higher_Lower()


ask=str(input("Do you wanna play again? type y or n: ")).lower()


ask=check_yn('y', 'n', ask)
clear_console()


while ask=='y':


    s=Higher_Lower()


    if max_score<s:


        max_score=s


    ask=input("Do you wanna play again? type y or n: ").lower()


    ask=check_yn('y', 'n', ask)
    clear_console()



print(f"good game your best score is:{max_score} ")
