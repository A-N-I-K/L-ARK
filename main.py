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
        delay()

        lines = resp.splitlines()

        for line in lines:

            if line != "" and line != " ":

                info = line.split(",")

                if len(info) == 2:

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
        delay()

        playerPosList = resp.split()

        playerPosX = playerPosList[0][2:]
        playerPosY = playerPosList[1][2:]
        playerPosZ = playerPosList[2][2:]

        if isFloat(playerPosX) and isFloat(playerPosY) and isFloat(playerPosZ):

            return [playerPosX, playerPosY, playerPosZ]

        else:

            return None
    except Exception as e:

        print(e)
        return None


# Can be made faster by incorporating into drawCanvas()
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


# Can be made faster by incorporating into drawCanvas()
def getAllPlayers(rcon):

    playerList = getPlayerList(rcon)
    playerList = updatePlayerPos(rcon, playerList)

    print(playerList)

    return playerList


def drawCanvas(rcon):

    pygame.init()

    screen = pygame.display.set_mode([1008, 1008])
    pygame.display.set_caption("L'ARK")
    bg = pygame.image.load("img/valguero_100x100.png")
    font = pygame.font.Font('freesansbold.ttf', 10)

    running = True

    while running:

        screen.fill((0, 0, 0))
        screen.blit(bg, (0, 0))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                running = False

        # == FAST DRAW == #

        playerList = getPlayerList(rcon)

        # == FAST DRAW == #

        # playerList = getAllPlayers(rcon)

        for player in playerList:

            # == FAST DRAW == #

            sid = player[2]
            playerPos = getPlayerPos(rcon, sid)

            if playerPos != None:

                print(player[1], playerPos)

                playerPosX = playerPos[0]
                playerPosY = playerPos[1]

                # == FAST DRAW == #

                # playerPosX = player[3][0]
                # playerPosY = player[3][1]

                playerLon = int(513 + (float(playerPosX) / 816))
                playerLat = int(506 + (float(playerPosY) / 816))

                pygame.draw.circle(screen, (255, 0, 0), (playerLon, playerLat), 5)

                # == NAME == #

                name = font.render(" " + player[1] + " [" + str(round(50 + (float(playerPosY) / 8160), 1)) + "," + str(round(50 + (float(playerPosX) / 8160), 1)) + "] ", True, (0, 255, 0), (0, 0, 128))
                nameBox = name.get_rect()
                nameBox.center = (playerLon, playerLat - 15)

                screen.blit(name, nameBox)

                # == NAME == #

        # pygame.draw.circle(screen, (0, 0, 255), (int(513 + (float(0) / 816)), int(506 + (float(0) / 816))), 5)

        pygame.display.flip()

        # time.sleep(1)

    # rcon.disconnect()
    pygame.quit()


def isFloat(num):

    try:

        float(num)
        return True
    except Exception:

        return False


def delay():

    time.sleep(0.1)


def main():

    ip = "192.168.0.196"
    pw = "quagganland"
    port = 32330

    rcon = mcrcon.MCRcon(ip, pw, port)

    # startCon(rcon)

    # if rcon != None:

    drawCanvas(rcon)

    endCon(rcon)


if __name__ == '__main__':

    main()
    pass
