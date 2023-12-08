import numpy as np

def split_txt(filename):
    array_text = []
    array_for_cal = []
    text = ''
    
    with open(filename, 'r') as txt:
        lines = txt.readlines()

    cnt = 1
    file_name_num = 1
    for line in lines:
        strip_line = line.strip()

        if cnt == 1:
            t = strip_line.split(' ')

            array_text.append(t[6][5:-1])    # nSub
            array_text.append(t[3][5:-1])    # nARC
            array_text.append(t[2][7:-1])    # thARC
        
        if cnt >= 4:
            t = strip_line.split('\t')
            array_for_cal.append(float(t[1]))

        if cnt == 233:
            cnt = 0

        cnt = cnt + 1

    t_mean = np.mean(array_for_cal)
    t_SD = np.std(array_for_cal)

    array_text.append(str(t_mean))
    array_text.append(str(t_SD))

    for i in range(0, 5):
        text += array_text[i] + '\t'
        
    file_name = 'C:\\Users\\User\\Desktop\\ARC_Project\\T_files_3\\T_cal.txt'
    fw = open(file_name, 'a')
    fw.write(f'{text}\n')
    fw.close()


filename_array = []


for i in range(1, 919):
    filename_array.append(f'T_{str(i)}.txt')

for name in filename_array:
    name = 'C:\\Users\\User\\Desktop\\ARC_Project\\T_files_2\\' + name
    split_txt(name)

print('Finish!')
