import random
import numpy as np
import pandas as pd
data2 = []
for m in range(10):
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
    def hit(card1,card2):
        sum = 0
        sum = sum + card_dic[card1] + card_dic[card2]
        if(card1 != 'A' or card2 != 'A'):
            if (card1 == 'A' or card2 == 'A'):
                flag = 1
            else:
                flag = 0
            play_pick = random.choice(list(card_dic.keys()))
            if((flag == 1) and (sum + card_dic[play_pick] + 10 <=21)):
                sum = sum + card_dic[play_pick] + 10
            else:
                sum = sum + card_dic[play_pick]
            return sum
        else:
            return 12
    deck = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    map = {'A': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, '10': 9, 'J': 10, 'Q': 11, 'K': 12}
    arr = np.zeros((169, 13))
    for i in deck:
        for j in deck:
            for k in deck:
                c = 0
                for l in range(5000):
                    card_deal = getsum(k)
                    play_deal = hit(i,j)

                    if((play_deal >= card_deal) or (card_deal > 21)):
                        if(play_deal <= 21):

                            c+=1
                req = (((map[i]+1)*13) - (12 - map[j])-1)
                arr[req][map[k]]+=c/50
    li = []
    for x in arr:
        for y in x:
            li.append(y)
    data2.append(li)

df2 = pd.DataFrame(data2)
exl = df2.to_csv("DataSet_3_raw.csv")
print(exl)
