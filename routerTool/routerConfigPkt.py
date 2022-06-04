import pyperclip
from routerScript import *

def cidrCalc(cidr):
    sub = [255,254,252,248,240,224,192,128]
    if cidr <= 8:
        subDiff = 8 - cidr
        subMask = f'{sub[subDiff]}.0.0.0'
    elif cidr > 8 and cidr <= 16:
        subDiff = 16 - cidr
        subMask = f'255.{sub[subDiff]}.0.0'
    elif cidr > 16 and cidr <= 24:
        subDiff = 24 - cidr
        subMask = f'255.255.{sub[subDiff]}.0'
    elif cidr > 24:
        subDiff = 32 - cidr
        subMask = f'255.255.255.{sub[subDiff]}'
    return subMask

def getInterface(Interface):
    if Interface == "g0":
        conn = "g0/0/0"
        return conn
    elif Interface == "g1":
        conn = "g0/0/1"
        return conn
    elif Interface == "s0":
        conn = "s0/1/0"
        return conn
    elif Interface == "s1":
        conn = "s0/1/1"
        return conn
    else:
        pass
    
def getIP():
    ipAdd = input("IP add for Router: (INT, IP, CIDR) ")
    secIP = ipAdd.split()
    Interface = secIP[0]
    finIP = secIP[1]
    cidr = int(secIP[2])

    subMask = cidrCalc(cidr)
    conn = getInterface(Interface)
    lastIP(conn,finIP,subMask)

def getDhcp():
    dhcpPool = input("DHCP config for Router: (SUBID, CIDR)")
    dhcpPool1 = dhcpPool.split()
    subID = dhcpPool1[0]
    cidr = int(dhcpPool1[1])

    subName = subID.split('.')
    name = '-'.join(subName) + '-' + str(cidr)
    fourthOct = int(subName[3]) + 1
    defRouter = subName[0] + '.' + subName[1] + '.' + subName[2] + '.' + str(fourthOct)
    subMask = cidrCalc(cidr)
    dhcpPoolParty(name,subID,subMask,defRouter)

def getVlan():
    ipAdd = input("IP add for Router: (INT, IP, CIDR, VLAN) ")
    secIP = ipAdd.split()
    Interface = secIP[0]
    finIP = secIP[1]
    cidr = int(secIP[2])
    vlan = secIP[3]

    subMask = cidrCalc(cidr)
    conn = getInterface(Interface)
    trunkPort(conn,finIP,subMask,vlan)

def switchConfig():
    gigOrfast = input("\nSWITCH CONFIG: \nwill you be affecting Gigabit or FastEthernet ports? (g or f)")
    if gigOrfast == "g":
        switchTrunk()
    if gigOrfast == "f":
        fastrange = input("What FastEthernet ports (fa0/[input]): ")
        switchVLAN = input("What VLAN is it for: ")
        switchFast(fastrange, switchVLAN)
    
def networkShell(getcommand):
    if getcommand == "ip":
        getIP()
        main()
    elif getcommand == "name":
        Router = input("Router name: ")
        rconfig(Router)
        main()
    elif getcommand == "clock":
        clockr8()
        main()
    elif getcommand == "ssh":
        sshconfig()
        main()
    elif getcommand == "eigrp":
        eigrp()
        main()
    elif getcommand == "trunk":
        Interface = input("On what connection: ")
        trunkin = getInterface(Interface)
        trunkOn(trunkin)
        main()
    elif getcommand == "vlan":
        getVlan()
        main()
    elif getcommand == "dhcp":
        getDhcp()
        main()
    elif getcommand == "switch":
        switchConfig()
        main()
    elif getcommand == "help":
        print("ip, name, clock, ssh, eigrp, trunk, vlan, dhcp, switch, bye")
        main()
    elif getcommand == "bye":
        print("GoodBye :)")
    else:
        print("\nERROR!!! Please enter a valid command")
        main()
        
def main():
    getcommand = input("What would you like to do: ")
    networkShell(getcommand)


main()
