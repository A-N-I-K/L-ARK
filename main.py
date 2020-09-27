'''
Created on Sep 26, 2020

@author: Anik
'''

from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import time
import pygame
import mcrcon


def startCon(rcon):

    try:
        rcon.connect()
        return rcon
    except Exception as e:
        print(e)
        return None


def endCon(rcon):

    try:
        rcon.disconnect()
    except Exception as e:
        print(e)


def getPlayerList(rcon):

    playerList = []

    try:
        startCon(rcon)
        resp = rcon.command("listplayers")
        endCon(rcon)

        lines = resp.splitlines()

        for line in lines:

            if line != "" and line != " ":

                info = line.split(",")

                serial = info[0][0:info[0].find(".")].strip()
                name = info[0][info[0].find(".") + 1:].strip()
                sid = info[1].strip()

                playerList.append([serial, name, sid])
    except Exception as e:
        print(e)

    return playerList


def getPlayerPos(rcon, sid):

    try:
        startCon(rcon)
        resp = rcon.command("getplayerpos {}".format(sid))
        endCon(rcon)

        playerPosList = resp.split()

        playerPosX = playerPosList[0][2:]
        playerPosY = playerPosList[1][2:]
        playerPosZ = playerPosList[2][2:]

        return [playerPosX, playerPosY, playerPosZ]
    except Exception as e:
        print(e)
        return None


def updatePlayerPos(rcon, playerList):

    if len(playerList) > 0:

        for i in range(len(playerList)):

            playerPos = getPlayerPos(rcon, playerList[i][2])

            if playerPos != None and len(playerPos) == 3:

                if len(playerList[i]) == 3:

                    playerList[i].append(playerPos)

                else:

                    playerList[i][3] = playerPos

    return playerList


def drawCanvas():

    pygame.init()

    # screen = pygame.display.set_mode([1020, 1050], pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
    screen = pygame.display.set_mode([1008, 1008])
    tmpScreen = screen.copy()

    map = pygame.image.load("img/valguero_100x100.png")

    screen.fill((0, 0, 0))
    screen.blit(map, (0, 0))

    # Run until the user asks to quit
    running = True
    while running:

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the background with white

        # Draw a solid blue circle in the center
        pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

        # Flip the display
        pygame.display.flip()

    # Done! Time to quit.
    pygame.quit()


def main():

    ip = "192.168.0.196"
    pw = "quagganland"
    port = 32330

    rcon = mcrcon.MCRcon(ip, pw, port)

    # startCon(rcon)

    # if rcon != None:

    drawCanvas()

    while True:

        playerList = getPlayerList(rcon)
        onlinePlayerCount = len(playerList)

        playerList = updatePlayerPos(rcon, playerList)

        print(onlinePlayerCount, playerList)
        time.sleep(1)
    # endCon(rcon)


def test():

    ip = "192.168.0.196"
    pw = "quagganland"
    port = 32330

    rcon = mcrcon.MCRcon(ip, pw, port)

    startCon(rcon)
    print(rcon.command("getplayerpos 76561198034310022"))
    endCon(rcon)
    startCon(rcon)
    print(rcon.command("getplayerpos 76561198013307506"))
    endCon(rcon)


if __name__ == '__main__':

    main()
    pass
