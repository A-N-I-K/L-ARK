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

            if (line != "" and line != " "):

                info = line.split(",")

                serial = info[0][0:info[0].find(".")].strip()
                name = info[0][info[0].find(".") + 1:].strip()
                sid = info[1].strip()

                playerList.append([serial, name, sid])
    except Exception as e:
        print(e)

    return playerList


def main():

    ip = "192.168.0.196"
    pw = "quagganland"
    port = 32330

    rcon = mcrcon.MCRcon(ip, pw, port)

    startCon(rcon)

    if rcon != None:

        playerList = getPlayerList(rcon)
        # resp = rcon.command("getplayerpos 76561198034310022")
        print(playerList)
        endCon(rcon)


if __name__ == '__main__':

    main()
    pass
