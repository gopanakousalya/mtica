coord=[(3,9),(2,4)]
print('first tuple:{0[0]},{0[1]},second tuple:{1[0]},{0[1]}'.format(*coord))
print('{:#<30}'.format('apple'))
print('{:*>30}'.format('apple'))
print('{:^30}'.format('apple'))
print('{:*^30}'.format('apple'))

print("int:{0:d};hex:{0:o};oct:{0:o};bin:{0:b}".format(42,55))
print("int:{1:d};hex:{1:o};oct:{1:o};bin:{1:b}".format(42,55))
print('{:,}'.format(1234567890))
points=19.0;total=22
print('correct answer:{:.2%}'.format(points/total))
print('correct answer:{:.2}'.format(points/total))
