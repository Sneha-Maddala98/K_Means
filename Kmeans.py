import argparse
import pandas as pd
import numpy as np

#python student.py --data Example.csv

def KMeans(df, c1, c2, c3):

change = 1
J = 0
curr_c1 = c1[-1][0], c1[-1][1]
curr_c2 = c2[-1][0], c2[-1][1]
curr_c3 = c3[-1][0], c3[-1][1]

while(change != 0):

change = 0

for row in range(len(df)):
point_label = ''
point = df['x'][row],df['y'][row]

dist1 = np.linalg.norm(np.array((point))-np.array((curr_c1)))
dist2 = np.linalg.norm(np.array((point))-np.array((curr_c2)))
dist3 = np.linalg.norm(np.array((point))-np.array((curr_c3)))

min_dist = min(dist1, dist2, dist3)

if min_dist == dist1:
point_label = 'A'

elif min_dist == dist2:
point_label = 'B'

else:
point_label = 'C'

J += min_dist**2

if point_label != df['label'][row]:
change = 1

df.at[row, 'label'] = point_label

print(J)
J = 0
c1, c2, c3 = new_centroids(df, c1, c2, c3)
curr_c1 = c1[-1][0], c1[-1][1]
curr_c2 = c2[-1][0], c2[-1][1]
curr_c3 = c3[-1][0], c3[-1][1]


print_centroids(c1,c2,c3)


def new_centroids(df, c1, c2, c3):

acount = 0
bcount = 0
ccount = 0
p1 = [0,0]
p2 = [0,0]
p3 = [0,0]

for row in range(len(df)):
point = df['x'][row],df['y'][row]

if df['label'][row] == 'A':
p1[0] = p1[0]+point[0]
p1[1] = p1[1]+point[1]
acount +=1

elif df['label'][row] == 'B':
p2[0] = p2[0]+point[0]
p2[1] = p2[1]+point[1]
bcount += 1

else:
p3[0] = p3[0]+point[0]
p3[1] = p3[1]+point[1]
ccount +=1

if acount == 0:
c1.append(c1[-1])
else:
c1.append([(p1[0]/acount),(p1[1]/acount)])

if bcount == 0:
c2.append(c2[-1])
else:
c2.append([(p2[0]/bcount),(p2[1]/bcount)])

if ccount == 0:
c3.append(c3[-1])
else:
c3.append([(p3[0]/ccount),(p3[1]/ccount)])


return c1, c2, c3



def print_centroids(c1,c2,c3):
for i in range(len(c1)):
print(c1[i][0],',',c1[i][1],'\t',c2[i][0],',',c2[i][1],'\t',c3[i][0],',',c3[i][1])


def main():
args = parser.parse_args()
data = args.data
k = 3

headers = ['label', 'x', 'y']
df= pd.read_csv(data,names = headers)
dataset = df[['x','y']]

c1 = [[0,5]]
c2 = [[0,4]]
c3 = [[0,3]]
J = 0

KMeans(df, c1, c2, c3)




if __name__ == '__main__':
parser = argparse.ArgumentParser()
parser.add_argument("--data",help="Location of Data File")
main()
