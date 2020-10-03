# Written By: Andrew Bailey
# CS 264

import random
import pygame
from pygame.locals import *

pygame.init()

# display the map
displayWidth = 1000
displayHight = 800

screen = pygame.display.set_mode((displayWidth, displayHight))

# load in the images to display
background = pygame.image.load('map.jpg')
enemyTriangle = pygame.image.load('enemy.png')

ratio = displayHight/background.get_height()

background = pygame.transform.scale(background, (int(background.get_width() * ratio), int(background.get_height() * ratio)))
enemyTriangle = pygame.transform.scale(enemyTriangle, (15, 15))


loop = True

# This loop keeps the map up while the call for fire is being made
while loop:
    screen.blit(background, (0,0))

    screen.blit(enemyTriangle, (250, 350))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            loop = False
            #pygame.quit()
            #sys.exit()


# mock situation report to give needed information
enemyType = ['Armour', 'Infantry', 'Bunker']
enemyActivity = []
print ("The enemy has been identified as", random.choice(enemyType), "operating nearby Wallace Hollow")
print("\nCall for indirect Fire before engaging with Enemy Forces.")



# declared variables to run the loop and check answers
splash = "Splash Out"
shot = "Shot Out"
destroyed = "n"

# main loop to call for fire until the correct location and direction is put in
while destroyed == "n":

    callFire = input("Enter call here:\n")
    print(callFire)

    #input grid 
    grid = input("Enter Grid Coordinates (round to nearest 100m): ") #correct grid is WT06503320
    direction = int(input("Enter Direction (in degrees): ")) # correct direction is 300-310 degrees

    print("Target is located at ", grid, direction, "degrees from your location \nOut")
    #input Direction

    description = input("\nDescribe Target: ")
    print(description, "\nOut")
    print("\nShot Over")

    # checking for correct radio etiquette 
    checkShot = input("Respond correctly: ")
    if checkShot == shot:
        print("Splash Over")
        checkSplash = input("Respond correctly: ")
        if checkSplash == splash:
            print ("Nice Job!")
        else:
            print ("Incorrect")
    else:
        print("Incorrect")
        
    # checking if the target was destroyed or not
    if grid != "WT06503320":
        print("Your grid was incorrect, the enemy was not destroyed")
    
    if direction > 310 or direction < 300:
        print("The direction was incorrect, the enemy was not destroyed")

    # the user is prompted to call for fire again if the first time missed
    destroyed = input("Was the enemy destroyed? (y/n): ")
    