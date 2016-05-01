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
		print command
		code_format_dict[ command[0] ] = command[1]
	code_format.close()

def parsing():
	coding = open("code.txt",'r')
	output_file = open("output.txt",'w')
	for line in coding:
		command=[]
		text = line.strip()
		code = text.split(" ")
		command.extend( opcode_dict[code[0]] )


		if len(code) == 1:
			print "no args"
			diff = 32-len(command)
			for z in xrange(0,diff):
				command.extend(str('0'))
			#print command
		else:
			args = code[1].split(",")
			formatter = code_format_dict[code[0]].split(",")
			print "format", formatter, "length", len(formatter)
			print "arguements",args, "length", len(args)
			if len(args) < len(formatter):
				diff = len(formatter) - len(args)
				for z in xrange(0,diff):
					command.extend(binary(num=0,length=7))
			for x in range(len(args)-1,-1,-1):
				#print args[x]
				command.extend(binary(num=int(args[x]),length=int(formatter[x]) ))
		print "command",command
			#print len(command)
		for y in xrange(0,len(command)):
			output_file.write(command[y])
			if ( (y+1) % 8 == 0) and (y>0):
				output_file.write("\n")


def binary(num, pre='', length=8, spacer=0):
    return '{0}{{:{1}>{2}}}'.format(pre, spacer, length).format(bin(num)[2:])

build_dict()
build_code_format_dict()
parsing()
