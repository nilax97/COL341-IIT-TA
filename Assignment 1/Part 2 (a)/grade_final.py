def grade(num):
    '''formats a number to create a VPL grade'''
    print('Grade :=>> ' + str(num))

f = open("counter.txt", "r+");
value = f.readlines();
sum = 0.0;
for x in value:
    sum = sum + float(x);
grade(sum/3.0);