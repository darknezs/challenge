'''
โปรแกรมจัดการแข่งแบบทัวนาเมนต์
รับค่าเป็นไฟล์
ข้อจำกัด : จำนวนผู้เข้าแข่งขันต้องเป็นจำนวน 2^n
'''

import random

round = 1

def tournament(candidate):
    global round
    get_in = []
    remain = []
    size = len(candidate)
    list = random.sample(range(size), size)
    if round == 1:              #random candidate place at firstround
        for i in range(0, size):
            remain.append(candidate[list[i]])
    elif round > 1:
        remain = candidate
    print('Round', round, remain)

    for i in range(0, int(len(remain)),2):
        print('who would win?')
        print('1.'+remain[i])
        print('2.' + remain[i+1])
        choose = input('you choose --> ')
        print('-------------------------------')
        if choose == '1':
            get_in.append(remain[i])
        if choose == '2':
            get_in.append(remain[i+1])
    round = round + 1

    if len(get_in) > 1:
        tournament(get_in)
    if len(get_in) == 1:
        print('winner is ', get_in[0])

raw_candidate_arr = []
with open("name.txt", "r") as listFile:
    for line in listFile:
        word = line.strip()
        raw_candidate_arr.append(word)

tournament(raw_candidate_arr)
