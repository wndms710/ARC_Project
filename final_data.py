def add_parameters(filename):
    array_text = []
    text = ''

    with open(filename, 'r') as txt:
        lines = txt.readlines()

    cnt = 1

    for line in lines:
        strip_line = line.strip()

        if cnt == 1:
            t = strip_line.split(' ')

            array_text.append(t[6][5:-1])    # nSub
            array_text.append(t[3][5:-1])    # nARC
            array_text.append(t[2][7:-1])    # thARC


            for i in range(0, 3):
                text += array_text[i] + '\t'
        
        if cnt >= 4:
            t = strip_line.split('\t')
            text_sub = text + t[0] + '\t' + t[1]
                        
            file_name = 'C:\\Users\\User\\Desktop\\ARC_Project\\T_files_4\\T_data.txt'
            fw = open(file_name, 'a')
            fw.write(f'{text_sub}\n')
            fw.close()

            if cnt == 1004:
               cnt = 0

        cnt = cnt + 1

filename_array = []

for i in range(1, 919):
    filename_array.append(f'T_{str(i)}.txt')

for name in filename_array:
    name = 'C:\\Users\\User\\Desktop\\ARC_Project\\T_files_2\\' + name
    add_parameters(name)
    print(f'{name} Done!')


print('Finish!')
