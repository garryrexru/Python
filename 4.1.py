NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload"
var1 = NAT.replace('Fast', 'Gigabit')
print(var1)