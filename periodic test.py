
def periodAssignment(): #Gives the period of the atomic number
    global per #Sets per as a global variable so it can be used elsewhere 
    if 1 <= oan <= 2:
        per = int ("1")
    elif 3 <= oan <= 10:
        per = int ("2")
    elif 11 <= oan <= 18:
        per = int ("3")
    elif 19 <= oan <= 36:
        per = int ("4")
    elif 37 <= oan <= 54:
        per = int ("5")
    elif 55 <= oan <= 86:
        per = int ("6")
    elif 87 <= oan <= 118:
        per = int ("7")
    else :
        raise ValueError ("Atomic number does not fit!") #Ends program if atomic number is not an integer between 1 and 118
    print ("Period:", per)
    lastPeriodElectrons()

def lastPeriodElectrons(): #Lists the number of electrons in the last period of the element's position
    global lpe #Sets lpe as a global variable so it can be used elsewhere
    if per == 1:
        lpe = oan
    elif per == 2:
        lpe = oan - 2
    elif per == 3:
        lpe = oan - 10
    elif per == 4:
        lpe = oan - 18
    elif per == 5:
        lpe = oan - 36
    elif per == 6:
        lpe = oan - 54
    elif per == 7:
        lpe = oan - 86
    else :
        raise RuntimeError ("Something went very wrong, the value for \'per\' does not fit!") #Ends program if value of per is not equal to an integer between 1 and 7

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
            if 1 <= dev <= 10:
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

def main():
    global oan
    oan = int ( input ("Input atomic number (0 to exit): ") )
    if oan == 0:
        raise SystemExit()
    ct = int ( input ("Input configuration type, 0 for full, 1 for noble gas, 2 for both: ") )
    print ("--------------------")
    print ("Atomic number:", oan)
    periodAssignment()
    ##ic = int ( input ("Input ionic charge: ") )
    ##print ("Ionic charge:", ic)
    ##nan = oan + ic
    ##print ("Atomic number and charge:", nan)
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
        print ("Error: improper value")
    print ("--------------------")



while True:
    main()
