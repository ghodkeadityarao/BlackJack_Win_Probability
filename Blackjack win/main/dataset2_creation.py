import random
import pandas as pd

data1 = []
for m in range(500):
    card_dic = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10}


    def getsum(card):
        sum = 0
        flag = 0
        if (card == 'A'):
            flag = 1
        sum = sum + card_dic[card]
        while (sum <= 17):
            card_pick = random.choice(list(card_dic.keys()))
            if ((sum == 17) and flag == 1):
                if (sum + card_dic[card_pick] > 21):
                    sum = sum + card_dic[card_pick] - 10
                else:
                    sum = sum + card_dic[card_pick]
                break
            elif ((sum == 17) and flag == 0):
                break

            if ((flag == 1) and (sum + card_dic[card_pick] + 10 <= 21 and sum + card_dic[card_pick] + 10 > 17)):
                sum = sum + card_dic[card_pick] + 10
            elif ((flag == 1) and (sum + card_dic[card_pick] + 10 > 21 or sum + card_dic[card_pick] + 10 < 17)):
                sum = sum + card_dic[card_pick]
            elif ((flag == 0) and card_pick == 'A'):
                if (sum + card_dic[card_pick] + 10 <= 21 and sum + card_dic[card_pick] + 10 > 17):
                    sum = sum + card_dic[card_pick] + 10
                    flag = 1
                else:
                    sum = sum + card_dic[card_pick]
                    flag = 1
            elif ((flag == 0) and card_pick != 'A'):
                sum = sum + card_dic[card_pick]

        return sum

    deal = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    play_sum = [12,13,14,15,16,17,18,19,20,21]
    map = {'A':0,'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7,'9':8,'10':9,'J':10,'Q':11,'K':12}
    li = [[0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0]]
    for i in play_sum:
        for j in deal:
            win = 0
            for k in range(5000):
                deal_sum = getsum(j)
                if(i >= deal_sum or deal_sum > 21):
                    win += 1
            win_prob = (win/5000)*100
            map_key = map[j]
            li[i-12][map_key]+=win_prob
    li_final = []
    for i in li:
        for y in i:
            li_final.append(y)
    data1.append(li_final)

df = pd.DataFrame(data1)
exl = df.to_csv("DataSet_2_raw.csv")
print(exl)

