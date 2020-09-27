'''
Created on Sep 26, 2020

@author: Anik
'''

import os
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
        resp = rcon.command("listplayers")
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
        resp = rcon.command("getplayerpos {}".format(sid))
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


def main():

    ip = "192.168.0.196"
    pw = "quagganland"
    port = 32330

    rcon = mcrcon.MCRcon(ip, pw, port)

    startCon(rcon)

    if rcon != None:

        playerList = getPlayerList(rcon)
        onlinePlayerCount = len(playerList)

        playerList = updatePlayerPos(rcon, playerList)

        # playerPos =
        # resp = rcon.command("getplayerpos 76561198034310022")
        print(onlinePlayerCount, playerList)
        endCon(rcon)


if __name__ == '__main__':

    main()
    pass
