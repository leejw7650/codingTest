score = input()

score = list(map(int,score))

if sum(score[0:(len(score)//2)]) == sum(score[-(len(score)//2):]) :
    print("LUCKY")

else :
    print("READY")