import pyperclip

## Scripts that will copy from routerConfig and we can paste into pktTracer

def lastIP(conn,finIP,subMask):
    confScript = f"""

conf t
int {conn}
ip add {finIP} {subMask}
no shut
end
wr mem
"""
    pyperclip.copy(confScript)

def rconfig(Router):
    confScript = f"""

conf t
hostname {Router}
ip domain-name ecpi.local
end
wr mem
"""
    pyperclip.copy(confScript)

def clockr8():
    confScript = f"""

conf t
int s0/1/0
clock rate 500000
end
wr mem
"""
    pyperclip.copy(confScript)
def sshconfig():
    confScript = f"""

conf t
username student password class
crypto key generate rsa
1024
ip ssh version 2
ip ssh time-out 50
ip ssh authentication-retries 4
line vty 0 4
transport input all
login local
logging synchronous
motd-banner
end
wr mem
"""
    pyperclip.copy(confScript)
    
def eigrp():
    confScript = f"""

conf t
router eigrp 100
network 10.0.0.0
network 11.0.0.0
network 172.16.0.0
end
wr mem
"""
    pyperclip.copy(confScript)
    
def trunkOn(trunkin):
    confScript = f"""

conf t
int {trunkin}
no ip add
no shut
end
wr mem
"""
    pyperclip.copy(confScript)
    
def trunkPort(conn,finIP,subMask,vlan):
    confScript = f"""

conf t
int {conn}.{vlan}
encapsulation dot1q {vlan}
ip add {finIP} {subMask}
end
wr mem
"""
    pyperclip.copy(confScript)

def dhcpPoolParty(name,subID,subMask,defRouter):
    confScript = f"""

conf t
ip dhcp pool mypool-{name}
network {subID} {subMask}
default-router {defRouter}
dns-server 11.1.1.10
end
wr mem
"""
    pyperclip.copy(confScript)

def switchFast(fastrange, switchVLAN):
    confScript = f"""

conf t
int ra fa0/{fastrange}
switchport mode access
switch access vlan {switchVLAN}
end
wr mem
"""
    pyperclip.copy(confScript)

def switchTrunk():
    confScript = f"""

conf t
int ra g0/1-2
switchport mode trunk
end
wr mem
"""
    pyperclip.copy(confScript)
