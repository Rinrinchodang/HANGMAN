import random
print("lets play hangman")
def hangman():
    f=open("hangman1.txt","r")
    list=f.read()
    f.close()
    word=random.choice(list)
    tries=6
    str=""
    v=set('abcdefghijklmnopqrstuvwxyz')
    while len(word)>0:
        # guess=input("please guess a letter or a word")
        # if len(guess)==1:
        #     print("you already guessed the letters")
        # elif guess not in word:
        #     print(guess,"is not in word")2
        #     tries-=1
        # else:
        #     print(guess,"is the word")

        word_var=""
        for letter in word:
            if letter in str:
                word_var=word_var+letter
            else:
                word_var=word_var+"_"
        if word_var==word:
            print(word_var)
            print("congrats!,you won")
            break
        print("guess the word",word_var)
        guess=input("enter the word:")
        if guess in v:
            str=str+guess
        else:
            print("enter valid words")
            guess=input()
        if guess not in word:
            if tries==6:
                print("  __")
                print("       |")
                print("       |")
                print("       |")
                print(" =======")
            if tries==5:
                print("o___")
                print("     |")
                print("     |")
                print(" =====")
            if tries==4:
                print(" o__")
                print(" |   |")
                print("     |")
                print(" =====")
            if tries==3:
                print("3 time is left ")
                print(" o___")
                print("/|    |")
                print("      |")
                print(" ======")
            if tries==2:
                print("2 time is left choose right")
                print(" o___")
                print("/|\   |")
                print("      |")
                print(" =======")
            if tries==1:
                print("only one trun is left):!!")
                print(" o___")
                print("/|\   |")
                print("/     |")
                print(" =======")
            if tries==0:
                print("ooppssss sorry you loss")
                print(" o___")
                print("/|\    |")
                print("/ \    |")
                print(" =======")
                break
            tries=tries-1
name=input("enter your name__(:")
print("WELCOME To Hangman Game ",name)
hangman()
        
