'''
สวัสดี Riot ฉันมีคำถามเกี่ยวกับ Aram การเลือกแชมเปี้ยนเป็นแบบสุ่มทั้งหมดเหรอ?
จะแน่ใจได้อย่างไรว่าทั้งสองทีมจะไม่ได้แชมเปี้ยนเหมือนกันแม้จะมีคนสุ่มใหม่?

ตรรกะสำหรับการเลือกแชมเปี้ยนของ ARAM อยู่ในระบบที่เราเรียกว่า TeamBuilder เซิร์ฟเวอร์ TeamBuilder
จะรู้ว่าผู้เล่นทุกคนได้รับแชมเปี้ยนตัวไหน แชมเปี้ยนอะไรอยู่ในสล็อตตัวสำรอง ฯลฯ สำหรับทั้งสองทีม TeamBuilder
ป้องกันไม่ให้ผู้เล่นสุ่มแชมเปี้ยนที่คนอื่นสุ่มได้ไปแล้ว

UI การเลือกแชมเปี้ยนของไคลเอนต์ลีกจะมอบแชมเปี้ยนให้คุณอย่างที่ TeamBuilder ต้องการและเมื่อคุณคลิก "Reroll"
ไคลเอนต์จะบอก TeamBuilder ว่าคุณขอให้มีการสุ่มแชมเปี้ยนใหม่ TeamBuilder
จะกำหนดแชมเปี้ยนที่คุณสุ่มได้และส่งไปที่ไคลเอนต์เพื่อแสดงให้คุณเห็น

พูดง่าย ๆ ก็คือ กระบวนการเลือกแชมเปี้ยนทั้งหมดจะขึ้นตรงต่อเซิฟเวอร์ TeamBuilder เป็นผู้รับผิดชอบ
และทุก ๆ การสุ่มแชมเปี้ยน การกดสุ่มใหม่ การแลกเปลี่ยนแชมเปี้ยน
การเลือกแชมเปี้ยนจากสล็อตตัวสำรองและการล็อคอินจะเป็นระบบธุรกรรม
นั่นหมายความว่า เป็นไปไม่ได้ที่ผู้เล่นสองคนจะสุ่มได้แชมเปี้ยนซ้ำ TeamBuilder
จะดำเนินการสุ่มแชมเปี้ยนใหม่ทีละครั้งอย่างละเอียดถี่ถ้วน

ถ้าถามว่าการสุ่มนั้นเป็นการสุ่มโดยสิ้นเชิงหรือเปล่านั้น มันขึ้นอยู่กับว่าคุณหมายถึงการสุ่มแบบไหน
ทุก ๆครั้งที่คุณกดสุ่ม แชมเปี้ยนที่คุณได้รับจะถูกจั่วออกมาจากเซ็ตของแชมเปี้ยนที่คุณสามารถสุ่มออกมาได้
แต่เซ็ตที่หมายถึงนี้จะไม่มีการสุ่ม ในคำศัพท์เชิงเซ็ต-คณิตศาสตร์ เรากำหนด

+((A ∪ C ∪ O) R) D
+((A ∪ C ∪ O) - R) - D
โดย
A คือเซ็ตของแชมเปี้ยน 65 ตัวที่เล่นได้ตลอดเวลาใน ARAM
C เป็นแชมเปี้ยนที่เปิดให้เล่นฟรีประจำอาทิตย์
O คือเซ็ตของแชมเปี้ยนที่คุณมี
R คือเซ็ตแชมเปี้ยนที่ทั้ง 2 ทีมได้ทำการสุ่มได้ไปแล้วและ
D คือกลุ่มแชมเปี้ยนที่ไม่สามารถใช้การได้ (หวังว่าจะไม่มี)
พูดง่าย ๆ ว่า… คุณจะได้รับแชมเปี้ยนแบบสุ่มที่ไม่ได้มีอยู่แล้วในทีมหรือสล็อตตัวสำรอง

10 การสุ่มแรกก็ทำตามขั้นตอนนี้เช่นกัน ในช่วงเริ่มต้นของการเลือกแชมเปี้ยน TeamBuilder
จะทำสิ่งนี้เพียงครั้งเดียวสำหรับผู้เล่นแต่ละคนเพื่อตัดสินแชมเปี้ยนเริ่มต้นของทุกคน

โดยเฉพาะอย่างยิ่งแชมเปี้ยนที่ได้ปรากฏในเกมก่อนหน้านี้หรือแม้แต่การออกห้องเพื่อหลบหลีกการเลือกแชมเปี้ยนก็ไม่มีผลกับ
สิ่งนี้แต่อย่างใด นั่นหมายความว่ามีความเป็นไปได้ทั้งหมดที่จะได้แชมเปี้ยนตัวเดียวกันในเกมต่อมาหรือแชมเปี้ยนที่คุณชอบจริง ๆ
หรือจะเป็นแชมเปี้ยนที่คุณไม่ชอบเอาเสียเลยติดต่อกัน เมื่อสิ่งนั้นเกิดขึ้น มันจะทำให้รู้สึกได้ว่ามันไม่ได้สุ่ม
แม้ว่ามันจะเป็นแบบนั้นก็ตาม

ดังนั้นเมื่อเมาส์ของคุณลังเลวนไปวนมาบนปุ่มสุ่มใหม่ สิ่งที่ฉันพูดได้คือ “ โชคดีนะ!”

ตอบโดย - Riot Mojibake วิศวกรรมซอฟแวร์อาวุโส
'''
import random
class randomAram:
    """prototype how aram ramdom champaion"""

    def __init__(self,t1,t2):
        self.team_1 = t1
        self.team_2 = t2
        self.all_champion = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']
        self.free_champion_of_week = ['8','9','10']
        self.cannot_play_champion = []

        self.player_champioms_team_1 = [{'amoung' : ['1','3','5','7'] },
                                   {'amoung' : ['2','3','4','8'] },
                                   {'amoung' : ['3','4','5','6','7','8','9','10'] }]
        self.player_champioms_team_2 = [{'amoung' : ['1','2','5','8'] },
                                   {'amoung' : ['2','3','4','10'] },
                                   {'amoung' : ['3','6','7','8','9','10'] }]


    def test(self):
        print(self.team_1)

    def Union(self,lst1, lst2, lst3):
        final_list = list(set().union(lst1, lst2, lst3))
        return final_list

    def first_time_rand_champion(self,arr,player_champioms):
        temp = []
        temp = arr
        for i in range(len(player_champioms)):
            chamlist = player_champioms[i]['amoung']
            can_play = self.Union(self.all_champion, self.free_champion_of_week, chamlist)
            n = random.randint(0,len(can_play)-1)
            temp.append(can_play[n])
            del can_play[n]

        if len(temp) == len(set(temp)):
            # print('No duplicates found in list')
            # print(self.team_1)
            pass

    def prepare(self):
        for k in range(100):
            # print(k)
            arr_check = []
            self.team_1 = []
            self.team_2 = []
            self.first_time_rand_champion(self.team_1, self.player_champioms_team_1)
            self.first_time_rand_champion(self.team_2, self.player_champioms_team_2)
            # print(team_1,team_2)
            if  len(self.team_1) == 0 or len(self.team_2) == 0:
                print('something went wrong')
                self.prepare()
            else:
                for i in range(3):
                    arr_check.append(self.team_1[i])
                    arr_check.append(self.team_2[i])
                # print(arr_check)
                if len(arr_check) == len(set(arr_check)):
                    print('Done')
                    print('team 1:champaion',self.team_1)
                    print('team 2:champaion',self.team_2)
                    break
                else:
                    pass



    def reroll(self, own_champion,side):
        if side == 1:
            # print('---this is reroll---')
            can_play = self.Union(self.all_champion, self.free_champion_of_week, own_champion)
            for i in range(len(self.team_1)):
                can_play.remove(self.team_1[i])
            for j in range(len(self.team_2)):
                can_play.remove(self.team_2[j])
            n = random.randint(0,len(can_play)-1)
            self.team_1.append(can_play[n])
            print('new champ-->',can_play[n])
            # print(self.team_1)
        else:
            # print('---this is reroll---')
            can_play = self.Union(self.all_champion, self.free_champion_of_week, own_champion)
            for i in range(len(self.team_1)):
                can_play.remove(self.team_1[i])
            for j in range(len(self.team_2)):
                can_play.remove(self.team_2[j])
            n = random.randint(0,len(can_play)-1)
            self.team_2.append(can_play[n])
            print('new champ-->',can_play[n])
            # print(self.team_2)
    def show(self):
        print(self.team_1, self.team_2)

t1 = []
t2 = []
player_1 = ['1','3','5','7']
player_2 = ['2','4','8','10']
get_champion = randomAram(t1, t2)
get_champion.prepare()
check = True
while check:
    choice = int(input("Enter number\n1. show team 1 champion\n2. show team 2 champion\n3.player1 reroll\n4.player2 reroll\n5.exit\n"))
    if choice == 1:
        get_champion.show()
    elif choice == 2:
        get_champion.show()
    elif choice == 3:
        get_champion.reroll(player_1, 1)
    elif choice == 4:
        get_champion.reroll(player_1, 2)
    else:
        check = False
        break

    #
    #














































# prototype
# def first_time_rand_champion():
#     can_play_p1 = Union(all_champion, free_champion_of_week, player_1_champiom)
#     can_play_p2 = Union(all_champion, free_champion_of_week, player_2_champiom)
#     for i in range(0,10):
#         n1 = random.randint(0,len(can_play_p1)-1)
#         n2 = random.randint(0,len(can_play_p2)-1)
#         if can_play_p1[n1] != can_play_p2[n2]:
#             print(can_play_p1[n1], can_play_p2[n2])
#             break
#         else:
#             continue





# arr = [{'a':['1','2','3']},
#        {'a':['1','2','3']}
# ]
#
#     print(arr[i][w][0])
