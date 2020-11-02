chat_new = []
def convert(filename):
	with open(filename,'r', encoding = 'utf-8') as i:
		person = None
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
		return chat_new

def write(filename, message):
	with open(filename,'w', encoding = 'utf-8') as o:
		for line in message:
			o.write(line)

new_message = convert('input.txt')
print(new_message)
write('output.txt',new_message)





