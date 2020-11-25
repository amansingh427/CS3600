import Testing

car_accuracy = []
for x in range(5):
    car_accuracy.append(Testing.testCarData()[1])
pen_accuracy = []
for x in range(5):
    pen_accuracy.append(Testing.testPenData()[1])


print('Car accuracy max = %d\nCar accuracy avg = %d\nCar accuracy stdev = %d', max(car_accuracy), Testing.average(car_accuracy), Testing.stDeviation(car_accuracy))
print('Pen accuracy max = %d\nCar accuracy avg = %d\nPen accuracy stdev = %d', max(pen_accuracy), Testing.average(pen_accuracy), Testing.stDeviation(pen_accuracy))

