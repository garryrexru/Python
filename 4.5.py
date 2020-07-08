from sys import argv
vlans1 = input('Введите первый набор vlans ')
vlans2 = input('Введите второй набор vlans ')
command1 = 'switchport trunk allowed vlan {}'.format(vlans1) #1,2,3,5,8'
command2 = 'switchport trunk allowed vlan {}'.format(vlans2)#1,3,8,9'

var1 = command1.split()
var2 = var1[-1].split(',')
var3 = command2.split()
var4 = var3[-1].split(',')
var5 = sorted(list(set(var2) & set(var4)))
print(var5)
