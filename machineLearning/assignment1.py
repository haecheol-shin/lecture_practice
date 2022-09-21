import matplotlib.pyplot as plt
import random
import math


# 두 점 사이 거리를 구하는 함수
def distance(x1, y1, x2, y2):
    result = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
    return result


x = []
y = []

for _ in range(100): # 점 100개를 랜덤으로 찍음
    x.append(random.random())
    y.append(random.random())


plt.scatter(x, y, s=100, c='k', alpha=0.7) # 처음 일반 점들은 검은 색으로 칠한다.
plt.scatter(x[0], y[0], s=100, c='r', marker='D') # 이 기준점과 가까우면 빨간 색으로 칠한다. (편의상 그룹1)
plt.scatter(x[99], y[99], s=100, c='b', marker='D') # 이 기준점과 가까우면 파란 색으로 칠한다. (편의상 그룹2)

plt.show()

dist1 = [] # 그룹1의 점 사이 거리
dist2 = [] # 그룹2의 점 사이 거리

group1x = [] # 그룹1의 x좌표
group1y = [] # 그룹1의 y좌표
group2x = [] # 그룹2의 x좌표
group2y = [] # 그룹2의 y좌표

for i in range(100):  # 각 점마다 기준점에서의 거리를 구한다.
    dist1.append(distance(x[0], y[0], x[i], y[i]))
    dist2.append(distance(x[99], y[99], x[i], y[i]))

for i in range(100):
    if dist1[i] < dist2[i]:
        plt.scatter(x[i], y[i], s=100, c='r')  # 그룹1에 소속되면 빨간 색으로 칠한다.
        group1x.append(x[i])
        group1y.append(y[i])
    else:
        plt.scatter(x[i], y[i], s=100, c='b')  # 그룹2에 소속되면 파란 색으로 칠한다.
        group2x.append(x[i])
        group2y.append(y[i])

plt.scatter(x[0], y[0], s=100, c='r', marker='D') # 그룹1 기준점 다시 표시
plt.scatter(x[99], y[99], s=100, c='b', marker='D') # 그룹2 기준점 다시 표시
plt.show()

# line 1~50 까지 초기 세팅 코드

x[0] = sum(group1x) / len(group1x) # 그룹1의 평균점 (x좌표)
y[0] = sum(group1y) / len(group1y) # 그룹1의 평균점 (y좌표)
x[99] = sum(group2x) / len(group2x) # 그룹2의 평균점 (x좌표)
y[99] = sum(group2y) / len(group2y) # 그룹2의 평균점 (y좌표)

dist1 = [] # 그룹1의 점 사이 거리
dist2 = [] # 그룹2의 점 사이 거리

group1x = [] # 그룹1의 x좌표
group1y = [] # 그룹1의 y좌표
group2x = [] # 그룹2의 x좌표
group2y = [] # 그룹2의 y좌표

for i in range(100):  # 각 점마다 기준점에서의 거리를 구한다.
    dist1.append(distance(x[0], y[0], x[i], y[i]))
    dist2.append(distance(x[99], y[99], x[i], y[i]))

for i in range(100):
    if dist1[i] < dist2[i]:
        plt.scatter(x[i], y[i], s=100, c='r')  # 그룹1에 소속되면 빨간 색으로 칠한다.
        group1x.append(x[i])
        group1y.append(y[i])
    else:
        plt.scatter(x[i], y[i], s=100, c='b')  # 그룹2에 소속되면 파란 색으로 칠한다.
        group2x.append(x[i])
        group2y.append(y[i])

plt.scatter(x[0], y[0], s=100, c='r', marker='D') # 그룹1 기준점 다시 표시
plt.scatter(x[99], y[99], s=100, c='b', marker='D') # 그룹2 기준점 다시 표시
plt.show()

# line 54~83 까지 기준점 바꾸고 다시 그룹화 하는 코드

x[0] = sum(group1x) / len(group1x) # 그룹1의 평균점 (x좌표)
y[0] = sum(group1y) / len(group1y) # 그룹1의 평균점 (y좌표)
x[99] = sum(group2x) / len(group2x) # 그룹2의 평균점 (x좌표)
y[99] = sum(group2y) / len(group2y) # 그룹2의 평균점 (y좌표)

dist1 = [] # 그룹1의 점 사이 거리
dist2 = [] # 그룹2의 점 사이 거리

group1x = [] # 그룹1의 x좌표
group1y = [] # 그룹1의 y좌표
group2x = [] # 그룹2의 x좌표
group2y = [] # 그룹2의 y좌표

for i in range(100):  # 각 점마다 기준점에서의 거리를 구한다.
    dist1.append(distance(x[0], y[0], x[i], y[i]))
    dist2.append(distance(x[99], y[99], x[i], y[i]))

for i in range(100):
    if dist1[i] < dist2[i]:
        plt.scatter(x[i], y[i], s=100, c='r')  # 그룹1에 소속되면 빨간 색으로 칠한다.
        group1x.append(x[i])
        group1y.append(y[i])
    else:
        plt.scatter(x[i], y[i], s=100, c='b')  # 그룹2에 소속되면 파란 색으로 칠한다.
        group2x.append(x[i])
        group2y.append(y[i])

plt.scatter(x[0], y[0], s=100, c='r', marker='D') # 그룹1 기준점 다시 표시
plt.scatter(x[99], y[99], s=100, c='b', marker='D') # 그룹2 기준점 다시 표시
plt.show()

x[0] = sum(group1x) / len(group1x) # 그룹1의 평균점 (x좌표)
y[0] = sum(group1y) / len(group1y) # 그룹1의 평균점 (y좌표)
x[99] = sum(group2x) / len(group2x) # 그룹2의 평균점 (x좌표)
y[99] = sum(group2y) / len(group2y) # 그룹2의 평균점 (y좌표)

dist1 = [] # 그룹1의 점 사이 거리
dist2 = [] # 그룹2의 점 사이 거리

group1x = [] # 그룹1의 x좌표
group1y = [] # 그룹1의 y좌표
group2x = [] # 그룹2의 x좌표
group2y = [] # 그룹2의 y좌표

for i in range(100):  # 각 점마다 기준점에서의 거리를 구한다.
    dist1.append(distance(x[0], y[0], x[i], y[i]))
    dist2.append(distance(x[99], y[99], x[i], y[i]))

for i in range(100):
    if dist1[i] < dist2[i]:
        plt.scatter(x[i], y[i], s=100, c='r')  # 그룹1에 소속되면 빨간 색으로 칠한다.
        group1x.append(x[i])
        group1y.append(y[i])
    else:
        plt.scatter(x[i], y[i], s=100, c='b')  # 그룹2에 소속되면 파란 색으로 칠한다.
        group2x.append(x[i])
        group2y.append(y[i])

plt.scatter(x[0], y[0], s=100, c='r', marker='D') # 그룹1 기준점 다시 표시
plt.scatter(x[99], y[99], s=100, c='b', marker='D') # 그룹2 기준점 다시 표시
plt.show()

x[0] = sum(group1x) / len(group1x) # 그룹1의 평균점 (x좌표)
y[0] = sum(group1y) / len(group1y) # 그룹1의 평균점 (y좌표)
x[99] = sum(group2x) / len(group2x) # 그룹2의 평균점 (x좌표)
y[99] = sum(group2y) / len(group2y) # 그룹2의 평균점 (y좌표)

dist1 = [] # 그룹1의 점 사이 거리
dist2 = [] # 그룹2의 점 사이 거리

group1x = [] # 그룹1의 x좌표
group1y = [] # 그룹1의 y좌표
group2x = [] # 그룹2의 x좌표
group2y = [] # 그룹2의 y좌표

for i in range(100):  # 각 점마다 기준점에서의 거리를 구한다.
    dist1.append(distance(x[0], y[0], x[i], y[i]))
    dist2.append(distance(x[99], y[99], x[i], y[i]))

for i in range(100):
    if dist1[i] < dist2[i]:
        plt.scatter(x[i], y[i], s=100, c='r')  # 그룹1에 소속되면 빨간 색으로 칠한다.
        group1x.append(x[i])
        group1y.append(y[i])
    else:
        plt.scatter(x[i], y[i], s=100, c='b')  # 그룹2에 소속되면 파란 색으로 칠한다.
        group2x.append(x[i])
        group2y.append(y[i])

plt.scatter(x[0], y[0], s=100, c='r', marker='D') # 그룹1 기준점 다시 표시
plt.scatter(x[99], y[99], s=100, c='b', marker='D') # 그룹2 기준점 다시 표시
plt.show()

x[0] = sum(group1x) / len(group1x) # 그룹1의 평균점 (x좌표)
y[0] = sum(group1y) / len(group1y) # 그룹1의 평균점 (y좌표)
x[99] = sum(group2x) / len(group2x) # 그룹2의 평균점 (x좌표)
y[99] = sum(group2y) / len(group2y) # 그룹2의 평균점 (y좌표)

dist1 = [] # 그룹1의 점 사이 거리
dist2 = [] # 그룹2의 점 사이 거리

group1x = [] # 그룹1의 x좌표
group1y = [] # 그룹1의 y좌표
group2x = [] # 그룹2의 x좌표
group2y = [] # 그룹2의 y좌표

for i in range(100):  # 각 점마다 기준점에서의 거리를 구한다.
    dist1.append(distance(x[0], y[0], x[i], y[i]))
    dist2.append(distance(x[99], y[99], x[i], y[i]))

for i in range(100):
    if dist1[i] < dist2[i]:
        plt.scatter(x[i], y[i], s=100, c='r')  # 그룹1에 소속되면 빨간 색으로 칠한다.
        group1x.append(x[i])
        group1y.append(y[i])
    else:
        plt.scatter(x[i], y[i], s=100, c='b')  # 그룹2에 소속되면 파란 색으로 칠한다.
        group2x.append(x[i])
        group2y.append(y[i])

plt.scatter(x[0], y[0], s=100, c='r', marker='D') # 그룹1 기준점 다시 표시
plt.scatter(x[99], y[99], s=100, c='b', marker='D') # 그룹2 기준점 다시 표시
plt.show()

x[0] = sum(group1x) / len(group1x) # 그룹1의 평균점 (x좌표)
y[0] = sum(group1y) / len(group1y) # 그룹1의 평균점 (y좌표)
x[99] = sum(group2x) / len(group2x) # 그룹2의 평균점 (x좌표)
y[99] = sum(group2y) / len(group2y) # 그룹2의 평균점 (y좌표)

dist1 = [] # 그룹1의 점 사이 거리
dist2 = [] # 그룹2의 점 사이 거리

group1x = [] # 그룹1의 x좌표
group1y = [] # 그룹1의 y좌표
group2x = [] # 그룹2의 x좌표
group2y = [] # 그룹2의 y좌표

for i in range(100):  # 각 점마다 기준점에서의 거리를 구한다.
    dist1.append(distance(x[0], y[0], x[i], y[i]))
    dist2.append(distance(x[99], y[99], x[i], y[i]))

for i in range(100):
    if dist1[i] < dist2[i]:
        plt.scatter(x[i], y[i], s=100, c='r')  # 그룹1에 소속되면 빨간 색으로 칠한다.
        group1x.append(x[i])
        group1y.append(y[i])
    else:
        plt.scatter(x[i], y[i], s=100, c='b')  # 그룹2에 소속되면 파란 색으로 칠한다.
        group2x.append(x[i])
        group2y.append(y[i])

plt.scatter(x[0], y[0], s=100, c='r', marker='D') # 그룹1 기준점 다시 표시
plt.scatter(x[99], y[99], s=100, c='b', marker='D') # 그룹2 기준점 다시 표시
plt.show()

x[0] = sum(group1x) / len(group1x) # 그룹1의 평균점 (x좌표)
y[0] = sum(group1y) / len(group1y) # 그룹1의 평균점 (y좌표)
x[99] = sum(group2x) / len(group2x) # 그룹2의 평균점 (x좌표)
y[99] = sum(group2y) / len(group2y) # 그룹2의 평균점 (y좌표)

dist1 = [] # 그룹1의 점 사이 거리
dist2 = [] # 그룹2의 점 사이 거리

group1x = [] # 그룹1의 x좌표
group1y = [] # 그룹1의 y좌표
group2x = [] # 그룹2의 x좌표
group2y = [] # 그룹2의 y좌표

for i in range(100):  # 각 점마다 기준점에서의 거리를 구한다.
    dist1.append(distance(x[0], y[0], x[i], y[i]))
    dist2.append(distance(x[99], y[99], x[i], y[i]))

for i in range(100):
    if dist1[i] < dist2[i]:
        plt.scatter(x[i], y[i], s=100, c='r')  # 그룹1에 소속되면 빨간 색으로 칠한다.
        group1x.append(x[i])
        group1y.append(y[i])
    else:
        plt.scatter(x[i], y[i], s=100, c='b')  # 그룹2에 소속되면 파란 색으로 칠한다.
        group2x.append(x[i])
        group2y.append(y[i])

plt.scatter(x[0], y[0], s=100, c='r', marker='D') # 그룹1 기준점 다시 표시
plt.scatter(x[99], y[99], s=100, c='b', marker='D') # 그룹2 기준점 다시 표시
plt.show()

x[0] = sum(group1x) / len(group1x) # 그룹1의 평균점 (x좌표)
y[0] = sum(group1y) / len(group1y) # 그룹1의 평균점 (y좌표)
x[99] = sum(group2x) / len(group2x) # 그룹2의 평균점 (x좌표)
y[99] = sum(group2y) / len(group2y) # 그룹2의 평균점 (y좌표)

dist1 = [] # 그룹1의 점 사이 거리
dist2 = [] # 그룹2의 점 사이 거리

group1x = [] # 그룹1의 x좌표
group1y = [] # 그룹1의 y좌표
group2x = [] # 그룹2의 x좌표
group2y = [] # 그룹2의 y좌표

for i in range(100):  # 각 점마다 기준점에서의 거리를 구한다.
    dist1.append(distance(x[0], y[0], x[i], y[i]))
    dist2.append(distance(x[99], y[99], x[i], y[i]))

for i in range(100):
    if dist1[i] < dist2[i]:
        plt.scatter(x[i], y[i], s=100, c='r')  # 그룹1에 소속되면 빨간 색으로 칠한다.
        group1x.append(x[i])
        group1y.append(y[i])
    else:
        plt.scatter(x[i], y[i], s=100, c='b')  # 그룹2에 소속되면 파란 색으로 칠한다.
        group2x.append(x[i])
        group2y.append(y[i])

plt.scatter(x[0], y[0], s=100, c='r', marker='D') # 그룹1 기준점 다시 표시
plt.scatter(x[99], y[99], s=100, c='b', marker='D') # 그룹2 기준점 다시 표시
plt.show()