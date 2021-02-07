csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
friends_list = []
print(friends_list)
step1 = csv.split(',')
print(step1)
step2 = step1[4].split(':')
print(step2)
step3 = step2[1].split(';')
print(step3)

friends_list.append(step1[0])
friends_list.append(step1[1])
friends_list.append(step1[2])
friends_list.append(step1[3])
friends_list.append(step2[0])
friends_list.append(step3[0])
friends_list.append(step3[1])
print(friends_list)