def text_to_csv(filename):	
	f_in = open('//Users//jueun//Desktop//ARC_Project//'+filename+'.txt', 'r')
	f_out = open('//Users//jueun//Desktop//ARC_Project//'+filename+'.csv', 'w')
	for line in f_in:
		line_replace = line.replace('\t', ',')
		f_out.write(line_replace)
	f_in.close()
	f_out.close()


filename_array = ['n1', 'n2', 'n3', 'th1', 'th2', 'th3', 'nth1', 'nth2', 'nth3']

for name in filename_array:

	text_to_csv(name)
	print(f'{name} done')

print('Finish!')

