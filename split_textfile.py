
def split_txt(filename):
    with open(filename, 'r') as txt:
        lines = txt.readlines()

    cnt = 1
    file_name_num = 1
    for line in lines:
        strip_line = line.strip()
        file_name = 'C:\\Users\\User\\Desktop\\ARC_Project\\T_files_2\\T_' + str(file_name_num) + '.txt'

        fw = open( file_name, 'a')

        if ((cnt in range(4, 24)) == False) and (cnt < 254)==True:
            fw.write(f'{strip_line}\n')
            fw.close()
            
        if cnt == 1004:
            file_name_num = file_name_num +1
            cnt = 0

        cnt = cnt + 1
        

split_txt('T.txt')
