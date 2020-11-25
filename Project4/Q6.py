import Testing

car_acc = []
for x in range(0, 41, 5):
    car_acc.append(Testing.testCarData([x])[1])

print('Car max = %d\nCar avg = %d\nCar stdv = %d' % (max(car_acc), Testing.average(car_acc), Testing.stDeviation(car_acc)))