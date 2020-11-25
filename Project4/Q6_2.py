import Testing

pen_acc = []
for x in range(0, 41, 5):
    pen_acc.append(Testing.testPenData([x])[1])

print('pen max = %d\npen avg = %d\npen stdv = %d' % (max(pen_acc), Testing.average(pen_acc), Testing.stDeviation(pen_acc)))