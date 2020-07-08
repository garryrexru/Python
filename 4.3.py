config = 'switchport trunk allowed vlan 1,3,10,20,30,100'
var1 = config.split()
var2 = var1[-1].split(',')
print(var2)