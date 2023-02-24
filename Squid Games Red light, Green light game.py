#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
choices = ["Run", "Freeze", "Hide"]
computer = random.choice(choices)
player = False
cpu_score = 0
player_score = 0
while True:
    player = input("Run, Freeze or  Hide?").capitalize()

    #Conditions of Red light, Green light
    if player == computer:
        print("Advance!")
    elif player == "Run":
        if computer == "Freeze":
            print("You lose! Laser kills you")
            cpu_score+=1
        else:
            print("You win! You reached safety")
            player_score+=1
    elif player == "Freeze":
        if computer == "Hide":
            print("You lose! Laser kills you")
            cpu_score+=1
        else:
            print("You win! You reached safety")
            player_score+=1
    elif player == "Hide":
        if computer == "Run":
            print("You lose... Laser kills you")
            cpu_score+=1
        else:
            print("You win! You reached safety")
            player_score+=1
    elif player=='End':
        print("Final Scores:")
        print(f"CPU:{cpu_score}")
        print(f"Plaer:{player_score}")
        break


# In[ ]:




