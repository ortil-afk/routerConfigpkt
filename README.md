# routerConfigpkt
Tool used to configure routers and switches in pkt tracer, by modifying and copying repetitive commands.

## How routerConfig.py works 

RouterConfig.py is set up to automate scripts that will be sent into Packet Tracer to configure Routers and Switches. It works in the same way as a shell, but will prevent mistakes from being sent to packet tracer to prevent typos, and faster configuration of routers since the commands are the same. These are the following commands that can be input into the scipt: 

- ip 
- name 
- clock 
- ssh 
- eigrp 
- trunk 
- vlan 
- dhcp 
- switch 
- help 
- bye  

All commands must be in lowercase and the commands will be explained in how they work and what they do. Also, all Routers and Switches must be in enabled mode in order for this to work. All arguments from the command are seperated by spaces, and have no other method in order to separate these values when entering them. 

 
## Installation
***DISCLAIMER!!! YOU MUST HAVE PYPERCLIP.PY INSTALLED FOR THIS SCRIPT TO WORK*** 

To install pyperclip.py: 

Go into command prompt 

Enter “pip install pyperclip” or “pip3 install pyperclip” and let the command prompt install pyperclip. 

```bash
pip install pyperclip
```

## COMMANDS: 

ip: 

The ip command will enter the ip address of whatever router and interface we are gonna configure. There are 3 arguments that are entered (INT, IP, CIDR). Here is an example: 
```bash
Ex. -->  g0 10.44.1.1 24 
```
The INT argument takes either “g0, g1, s0, s1” and converts this to “g0/0/0, g0/0/1, s0/1/0, s0/1/1” 

The IP argument just takes the IP address that will be entered for that interface 

The CIDR command takes the cidr, and translates that to a subnet mask for you. 

name: 

The name command takes the name that will be put for the Router/Switch. Here is an example: 
```bash
Ex. --> R1 
```
The above example will name the router “R1”, configure the domain name to be “ecpi.local”, and set the enable password to “cisco” 

 

clock: 

This command will change the s0/1/0 clock rate to 500000 

ssh: 

This command will enable ssh, and the default password is “class” 

Eigrp: 

This command will enable eigrp. Currently the eigrp is configured for 10.0.0.0, 11.0.0.0, and 172.16.0.0. if you wish to add another one to the default script, the command is in routerScript.py. 

trunk: 

This will turn on the trunk port ON THE ROUTER, and is a necessary step before entering the vlan command. Trunk as for one input and that would be the interface. Here is an example: 
```bash
Ex. --> g0 
```
The above example will allow g0/0/0 to be set up as a trunk port. 

 

vlan: 

This command will enable vlan configuration on the router, A TRUNK PORT MUST BE ENABLED FIRST (this can be done with the trunk command). Vlan takes 4 arguments (INT, IP, CIDR, VLAN ). Here is an example: 
```bash
Ex. --> g0 10.44.1.1 24 10 
```
The INT argument takes either “g0, g1, s0, s1” and converts this to “g0/0/0, g0/0/1, s0/1/0, s0/1/1” 

The IP argument just takes the IP address that will be entered for that interface 

The CIDR argument takes the cidr, and translates that to a subnet mask for you. 

The VLAN argument takes the VLAN we want to set. So in this example we are stating this is VLAN 10 

dhcp: 

The dhcp command takes two arguments subID and CIDR, and will configure a dhcp pool for that network. Here is an example. 
```bash
Ex. --> 10.44.1.0 24 
```
The subID argument takes the subnet ID of the network we want to create 

The CIDR will subnet the network for that cidr.  

Another note, is that the pool will be saved as “mypool-10-44-1-0-24” for the above example, in the event that you need to go back to configure the dhcp pool.  

The DNS server is also saved as “11.1.1.10” since that is the default DNS server for our assignments, if you wish it to be something else, either go into the dhcp pool after the command or alter the routerScript.py file.  

THE DHCP COMMAND WILL NOT PERFORM EXCLUDED ADDRESSES OR IP HELPER ADDRESS 

You will have to enter excluded addresses for dhcp manually, and configure ip helper address on other routers that do not have the dhcp pool. 

switch: 

This command is split into two posibilities, and will ask for Gigabit port (g) or FastEthernet port (f) 

If you choose “g” this will configure the switch to set up trunking on the gigabit ports. 

If you choose “f” this will go into vlan configuration for the switch, and the only two parameters it will ask for is the range of the ports, and the vlan assigned. Here is an example: 
```bash
Ex. --> what fast ethernet ports: 1-11 
```
What vlan is it for: 10 

The above will set the switch to allow vlan 10 work on FastEthernet ports 1-11. 

help: 

This command will show all available commands 

bye: 

This command will end the program 
