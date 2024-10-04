MainActivities = [["A","School",2], ["B","BotCode",2],["C","Eat",12], ["D","Anime",0.60],["E","Lift", 0.70]];

sum = 0;
txt = "$DaysActivities [C,B,A,E,D]"

x = list(txt.split()[1])

for i in x:
    if(i.isalpha()):
        print(i)
        for j in MainActivities:
            if i == j[0]:
                sum += j[2];
                
print("sum: {}".format(sum))