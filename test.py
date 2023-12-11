def tap_to_space(filename):
    fr = open(filename, 'r')
    lines = fr.readlines()
    fr.close()

    fw = open(filename, 'w')
    for line in lines:
        fw.write(line.replace('\t', ' '))
    fw.close()

tap_to_space('C:\\Users\\User\\Desktop\\ARC_Project\\T_data_final(1209)-3.txt')
