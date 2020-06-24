#!/usr/bin/python3
# todo: print only boys, sorted by height/weight ratio

fh = open('1.csv','r')
# note that we are NOT doing proper csv parsing - x,"a,b",y is not honored

#skip headers
fh.readline()

# init dict
ppl = {}

# parse 1.csv
for line in fh:
  (name,age,sex) = line.rstrip('\n').split(',')
  if (sex == 'M'):
    ppl[name] = None

# 2.csv
fh.close()
fh = open('2.csv','r')

#skip headers
fh.readline()

for line in fh:
  (name,height,weight) = line.rstrip('\n').split(',')
  if (name in ppl):
    ppl[name] = [int(height),int(weight)]

# just print sorted list
print(   sorted(ppl.keys(),key = lambda x: ppl[x][0]/ppl[x][1])   )

# print sorted list with value, reverse order
for human in sorted(ppl.keys(),key = lambda x: ppl[x][0]/ppl[x][1],reverse=True ):
  print(human,ppl[human][0],ppl[human][1],ppl[human][0]/ppl[human][1])
