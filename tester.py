'''
Created on Sep 26, 2020

@author: Anik
'''

import unittest
import main
import mcrcon


class Test(unittest.TestCase):

    def test_startCon_1(self):

        rcon = mcrcon.MCRcon("", "", 0)

        try:
            main.startCon(rcon)
        except Exception:
            self.fail()

    def test_startCon_2(self):

        rcon = mcrcon.MCRcon("", "", 0)
        self.assertEquals(main.startCon(rcon), None)

    def test_endCon_1(self):

        rcon = mcrcon.MCRcon("", "", 0)

        try:
            main.endCon(rcon)
        except Exception:
            self.fail()

    def test_getPlayerList_1(self):

        rcon = mcrcon.MCRcon("", "", 0)

        try:
            main.getPlayerList(rcon)
        except Exception:
            self.fail()


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
