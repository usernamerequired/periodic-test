def originalPeriodAssignment(): #Gives the period of the atomic number
    global oper #Sets oper as a global variable so it can be used elsewhere
    if 1 <= oan <= 2:
        oper = int ("1")
    elif 3 <= oan <= 10:
        oper = int ("2")
    elif 11 <= oan <= 18:
        oper = int ("3")
    elif 19 <= oan <= 36:
        oper = int ("4")
    elif 37 <= oan <= 54:
        oper = int ("5")
    elif 55 <= oan <= 86:
        oper = int ("6")
    elif 87 <= oan <= 118:
        oper = int ("7")
    else :
        raise ValueError ("Atomic number does not fit!")
    print ("Period:", oper)

def newPeriodAssignment(): #Gives the period of the atomic number of the grounded equivilant to the charged version
    global per #Sets per as a global variable so it can be used elsewhere
    if 1 <= nan <= 2:
        per = int ("1")
    elif 3 <= nan <= 10:
        per = int ("2")
    elif 11 <= nan <= 18:
        per = int ("3")
    elif 19 <= nan <= 36:
        per = int ("4")
    elif 37 <= nan <= 54:
        per = int ("5")
    elif 55 <= nan <= 86:
        per = int ("6")
    elif 87 <= nan <= 118:
        per = int ("7")
    else :
        raise ValueError ("Ionic Charge is not valid!")
    lastPeriodElectrons()

def lastPeriodElectrons(): #Lists the number of electrons in the last period of the element's position
    global lpe #Sets lpe as a global variable so it can be used elsewhere
    if per == 1:
        lpe = nan
    elif per == 2:
        lpe = nan - 2
    elif per == 3:
        lpe = nan - 10
    elif per == 4:
        lpe = nan - 18
    elif per == 5:
        lpe = nan - 36
    elif per == 6:
        lpe = nan - 54
    elif per == 7:
        lpe = nan - 86
    else :
        raise RuntimeError ("Something went VERY wrong, the value for \'per\' does not fit!")

def sBlockElectrons():
    global sev
    if lpe == 1:
        sev = 1
    else :
        sev = 2

def pBlockElectrons():
    global pev
    if 1 <= lpe <= 2:
        pev = 0
    else :
        if 4 <= per <= 7:
            if 0 <= dev <= 10:
                pev = 0
            else :
                pev = dev - 10
        else :
            pev = lpe - 2


def dBlockElectrons():
    global dev
    if 1 <= lpe <= 2:
        dev = 0
    else :
        if 6 <= per <= 7:
            if 1 <= fev <= 14:
                dev = 0
            else :
                dev = fev - 14
        else :
            dev = lpe - 2

def fBlockElectrons():
    global fev
    if 1 <= lpe <= 2:
        fev = 0
    else :
        fev = lpe - 2

def fullConfiguration():
    if per == 1:
        sBlockElectrons()
        pBlockElectrons()
        print ("1s" + str(sev))
    elif per == 2:
        sBlockElectrons()
        pBlockElectrons()
        print ("1s2 2s" + str(sev) + " 2p" + str(pev) )
    elif per == 3:
        sBlockElectrons()
        pBlockElectrons()
        if pev == 0:
            print ("1s2 2s2 2p6 3s" + str(sev) )
        else :
            print ("1s2 2s2 2p6 3s2 3p" + str(pev) )
    elif per == 4:
        sBlockElectrons()
        dBlockElectrons()
        pBlockElectrons()
        if dev == 0:
            print ("1s2 2s2 2p6 3s2 3p6 4s" + str(sev) )
        elif pev == 0:
            print ("1s2 2s2 2p6 3s2 3p6 4s2 3d" + str(dev) )
        else :
            print ("1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p" + str(pev) )
    elif per == 5:
        sBlockElectrons()
        dBlockElectrons()
        pBlockElectrons()
        if dev == 0:
            print ("1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s" + str(sev) )
        elif pev == 0:
            print ("1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d" + str(dev) )
        else :
            print ("1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p" + str(pev) )
    elif per == 6:
        sBlockElectrons()
        fBlockElectrons()
        dBlockElectrons()
        pBlockElectrons()
        if fev == 0:
            print ("1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s" + str(sev) )
        elif dev == 0:
            print ("1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f" + str(fev) )
        elif pev == 0:
            print ("1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d" + str(dev) )
        else :
            print ("1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p" + str(pev) )
    elif per == 7:
        sBlockElectrons()
        fBlockElectrons()
        dBlockElectrons()
        pBlockElectrons()
        if fev == 0:
            print ("1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6p2 4f14 5d10 6p6 7s" + str(sev) )
        elif dev == 0:
            print ("1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6p2 4f14 5d10 6p6 7s2 5f" + str(fev) )
        elif pev == 0:
            print ("1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6p2 4f14 5d10 6p6 7s2 5f14 6d" + str(dev) )
        else :
            print ("1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6p2 4f14 5d10 6p6 7s2 5f14 6d10 7p" + str(pev) )

def nobleConfiguration():
    if per == 1:
        sBlockElectrons()
        pBlockElectrons()
        print ("1s" + str(sev))
    elif per == 2:
        sBlockElectrons()
        pBlockElectrons()
        print ("[He] 2s" + str(sev) + " 2p" + str(pev) )
    elif per == 3:
        sBlockElectrons()
        pBlockElectrons()
        if pev == 0:
            print ("[Ne] 3s" + str(sev) )
        else :
            print ("[Ne] 3s2 3p" + str(pev) )
    elif per == 4:
        sBlockElectrons()
        dBlockElectrons()
        pBlockElectrons()
        if dev == 0:
            print ("[Ar] 4s" + str(sev) )
        elif pev == 0:
            print ("[Ar] 4s2 3d" + str(dev) )
        else :
            print ("[Ar] 4s2 3d10 4p" + str(pev) )
    elif per == 5:
        sBlockElectrons()
        dBlockElectrons()
        pBlockElectrons()
        if dev == 0:
            print ("[Kr] 5s" + str(sev) )
        elif pev == 0:
            print ("[Kr] 5s2 4d" + str(dev) )
        else :
            print ("[Kr] 5s2 4d10 5p" + str(pev) )
    elif per == 6:
        sBlockElectrons()
        fBlockElectrons()
        dBlockElectrons()
        pBlockElectrons()
        if fev == 0:
            print ("[Xe] 6s" + str(sev) )
        elif dev == 0:
            print ("[Xe] 6s2 4f" + str(fev) )
        elif pev == 0:
            print ("[Xe] 6s2 4f14 5d" + str(dev) )
        else :
            print ("[Xe] 6s2 4f14 5d10 6p" + str(pev) )
    elif per == 7:
        sBlockElectrons()
        fBlockElectrons()
        dBlockElectrons()
        pBlockElectrons()
        if fev == 0:
            print ("[Rn] 7s" + str(sev) )
        elif dev == 0:
            print ("[Rn] 7s2 5f" + str(fev) )
        elif pev == 0:
            print ("[Rn] 7s2 5f14 6d" + str(dev) )
        else :
            print ("[Rn] 7s2 5f14 6d10 7p" + str(pev) )

def valenceElectrons():
    vee = sev + pev
    print ("Valence electrons: " + str(vee))

def main():
    global oan
    global nan
    oan = int ( input ("Input atomic number (0 to exit): ") )
    if oan == 0:
        cprint ("Goodbye! Hope this was useful!","green")
        time.sleep(1)
        raise SystemExit()
    ##ic = int ( input ("Input ionic charge: ") )
    ic = 0
    ct = int ( input ("Input configuration type, 0 for full, 1 for noble gas, 2 for both: ") )
    print ("--------------------")
    print ("Atomic number:", oan)
    originalPeriodAssignment()
    ##print ("Ionic charge:", ic)
    nan = oan - ic
    newPeriodAssignment()
    if ct == 0:
        print ("Full electron configuration:")
        fullConfiguration()
    elif ct == 1:
        print ("Noble gas configuration:")
        nobleConfiguration()
    elif ct == 2:
        print ("Full electron configuration:")
        fullConfiguration()
        print ("Noble gas configuration:")
        nobleConfiguration()
    else :
        raise ValueError("Improper configuration value!")
    valenceElectrons()
    print ("--------------------\n")

import sys
import traceback
import time
from colorama import init
from termcolor import colored, cprint

init()

while True:
    try :
        main()
    except ValueError :
        sys.exc_info()
        traceback.print_exc()
        cprint ("Warning: improper input, please try again.","yellow")
    except RuntimeError :
        sys.exc_info()
        traceback.print_exc()
        cprint ("Error: How did you break it this badly? Ending program!","red")
        time.sleep(2)
        raise SystemExit()
    except Exception :
        sys.exc_info()
        traceback.print_exc()
        cprint ("Warning: Something went wrong, restarting program!\n","yellow")
        time.sleep(1)
