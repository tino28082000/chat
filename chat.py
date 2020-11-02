chat_new = []
person = None

with open('input.txt','r', encoding = 'utf-8') as i:
	for line in i:
		if '你傳送的時間：' in line:
			person = 'Tino:'
			continue
		elif '傳送的時間：' in line:
			continue
		elif '前' in line:
			continue
		elif '媽的老頭 1.75w' in line:
			person = '俊凱:'
			continue
		if person:
			chat_new.append(person + line)
print(chat_new)

with open('output.txt','w', encoding = 'utf-8') as o:
	for line in chat_new:
		o.write(line)



