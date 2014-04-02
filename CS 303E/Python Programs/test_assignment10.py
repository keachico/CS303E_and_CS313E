def main():
    getWeightedsums('013162959x')
    getWeightedsums('0321537114')

def getWeightedsums(line):
    
    if line[-1] == 'x':
        sum1 = [0]*10
        sum1_total = 0
        for i in range(len(line)-1):
            sum1_total = int(line[i]) + sum1_total
            sum1[i] = sum1_total
            sum1[-1] = sum1[-2] + 10
        #print str(sum1)

        sum2 = [0] * 10
        sum2_total = 0
        for i in range(len(sum1)):
            sum2_total = int(sum1[i]) + sum2_total
            sum2[i] = sum2_total
        #print sum2

        if sum2[9] % 11 == 0:
            print 'valid'
        else:
            print 'invalid'

    elif line[-1] == 'X':
        sum1 = [0]*10
        sum1_total = 0
        for i in range(len(line)-1):
            sum1_total = int(line[i]) + sum1_total
            sum1[i] = sum1_total
            sum1[-1] = sum1[-2] + 10
        #print str(sum1)

        sum2 = [0] * 10
        sum2_total = 0
        for i in range(len(sum1)):
            sum2_total = int(sum1[i]) + sum2_total
            sum2[i] = sum2_total
        #print sum2

        if sum2[9] % 11 == 0:
            print 'valid'
        else:
            print 'invalid'

    else:
        sum1 = [0]*10
        sum1_total = 0
        for i in range(len(line)):
            sum1_total = int(line[i]) + sum1_total
            sum1[i] = sum1_total
        #print str(sum1)

        sum2 = [0] * 10
        sum2_total = 0
        for i in range(len(sum1)):
            sum2_total = int(sum1[i]) + sum2_total
            sum2[i] = sum2_total
        #print sum2

        if sum2[9] % 11 == 0:
            print 'valid'
        else:
            print 'invalid'   

main()
