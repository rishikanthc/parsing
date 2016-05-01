opcode_dict = {}
code_format_dict = {}

def build_dict():
	file = open("opcode.txt",'r')
	for line in file:
		text=line.strip()
		code = text.split(":")
		opcode_dict[code[0]]=code[1]
	file.close()

def build_code_format_dict():
	code_format = open("code-format.txt",'r')
	for line in code_format:
		text = line.strip()
		command = text.split(" ")
		code_format_dict[ command[0] ] = command[1]
	code_format.close()


def parsing():
	coding = open("code.txt",'r')
	command=[]
	a=7
	for line in coding:
		text = line.strip()
		code = text.split(" ")
		command.extend( opcode_dict[code[0]] )
		args = code[1].split(",")
		command.extend(args[0])
		#command.extend(bin(int(code[1])))

		#command.extend(format(int(int(args[0]) & 0xff ), '07b'))
		command.extend(binary(num=int(args[0]),length=a))
		#command.extend("{0:b}".format(int(args[0]) & 0xff ))
		print command

def binary(num, pre='', length=8, spacer=0):
    return '{0}{{:{1}>{2}}}'.format(pre, spacer, length).format(bin(num)[2:])

build_dict()
build_code_format_dict()
parsing()
print opcode_dict
print code_format_dict