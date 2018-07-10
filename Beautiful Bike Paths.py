from operator import itemgetter

def max_florests(path_length, florests_intervals):
    n = len(florests_intervals)
    li1 = [[0] * 3 for i in range(n)]
    for i in range (0, n):
        li1[i][1] = florests_intervals[i][0]
        li1[i][2] = florests_intervals[i][1]
    for i in range (0, n):
        start = li1[i][1]
        end = li1[i][2]
        larger = False
        for j in range (0, n):
            if i != j:
                t_start = li1[j][1]
                t_end = li1[j][2]
                if start <= t_start and t_start < end:
                    li1[i][0] += 1
                elif start < t_end and t_end <= end:
                    li1[i][0] += 1
                elif t_start < start and end < t_end:
                    li1[i][0] += 1
                if start < t_start and t_end < end:
                    li1[j][0] += 1
                if start == t_start and t_end < end:
                    li1[j][0] += 1
                if end == t_end and start < t_start:
                    li1[j][0] += 1
                if t_start <= start and end <= t_end:
                    larger = True
        if larger == False:
            li1[i][0] += 1

    li1 = sorted(li1, key=itemgetter(0))
    li2 = [0]*path_length

    max_total = 0

    for j in range(0, len(li1)):
        li_item = li1[j]
        a = li_item[1]
        b = li_item[2]
        if b > n:
            b = n
        okay_add = True
        for i in range(a,b):
            if li2[i] == 3:
                okay_add = False
                i = b
        if okay_add:
            for i in range(a,b):
                li2[i] = li2[i] + 1
            max_total+=1
    print (max_total)

def group(lst, n):
    for i in range(0, len(lst)):
        lst[i] = int(lst[i])
    for i in range(0, len(lst), n):
        val = lst[i:i+n]
        if len(val) == n:
            yield tuple(val)

def main():
    f = open('input.txt')
    line = f.readline()
    path_length = int(line)
    line = f.readline()
    florests_intervals = (list(group(line.split(' '), 2)))
    max_florests(path_length, florests_intervals)

if __name__ == "__main__": main()
