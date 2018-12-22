#encoding utf-8
import random
import answerC
import C
def main():
    match = True
    count = 0
    while(match):
        n = random.randrange(2,20,2)
        Q = []
        for i in range(n):
            Q.append(random.randint(1,9))
        print("count:",count,"n:",n,"Q:",Q)
        myans = C.main(n,Q)
        trueans = answerC.main(n,Q)
        # print("わいの答え:",myans)
        # print("正しい答え:",trueans)
        count += 1
        if myans != trueans:
            match = False

    print(Q)
    print("わいの答え:",myans)
    print("正しい答え:",trueans)

if __name__ =="__main__":
    main()
