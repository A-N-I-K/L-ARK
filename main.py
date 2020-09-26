'''
Created on Sep 26, 2020

@author: Anik
'''

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


def listPlayers(rcon):

    try:
        resp = rcon.command("listplayers")
        print(resp)
    except Exception as e:
        print(e)


def main():

    ip = "192.168.0.196"
    pw = "quagganland"
    port = 32330

    rcon = mcrcon.MCRcon(ip, pw, port)

    startCon(rcon)

    if rcon != None:

        listPlayers(rcon)
        resp = rcon.command("getplayerpos 76561198034310022")
        print(resp)
        endCon(rcon)


if __name__ == '__main__':
    main()
    pass
