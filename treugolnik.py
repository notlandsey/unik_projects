#Программа поиска площади треугольника

x = input().split()
sm = 0
for i in range(len(x)):
    for j in range(i+1, len(x)):
        for k in range(j+1, len(x)):
            a = x[i]
            b = x[j]
            c = x[k]
            if a+b > c and a+c > b and b+c > a:
                p = (a+b+c)/2
                s = (p*(p-a)*(p-b)*(p-c))**0.5
                if s > sm:
                    sm = s
print(sm)
