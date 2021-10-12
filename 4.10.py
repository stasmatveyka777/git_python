machine=[]
machine.append("bugati")
machine.append("lexus")
machine.append("mazda")
machine.append("tesla")
machine.append("bmw")
#machine.remove("bmw")
item="bugati"
machine.remove(item)
message=f'Остались машин:{machine}'
machine.sort()
machine.reverse()
#print(machine)
t=len(machine)
print(t)
