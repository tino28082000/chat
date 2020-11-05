chat_new = []
new_message = []

def openfile(filename):
	with open(filename,'r', encoding = 'utf-8') as i:
		for line in i:
			chat_new.append(line)
	return chat_new


def convert(lines):
	person = None
	count_tino = 0
	count_jimmy = 0
	for line in lines:
		s = line.strip().split(' ')
		time = s[0]
		name = s[1]
		content = s[2:]
		if ':' not in time:
			new_message.append('今天是' + str(time))
		if name == 'Tino.L':
			for m in content:
				count_tino += len(m)
		elif name == 'Jimmy':
			for m in content:
				count_jimmy += len(m)
		if '星期' in name:
			new_message.append(str(name))
		else :
			new_message.append(str(name) + str(content))


	print(count_tino, count_jimmy)
	print(new_message)
	return new_message


def write(filename, message):
	with open(filename,'w', encoding = 'utf-8') as o:
		for line in message:
			o.write(str(line) + '\n')


def main(inputFileName,outputFileName): 
	chat_new = openfile(inputFileName)
	new_message = convert(chat_new)
	write(outputFileName,new_message)


main('[LINE]Jimmy.txt','linechat.txt')




