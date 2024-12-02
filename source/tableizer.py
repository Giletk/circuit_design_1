with open(r"C:\Learning\ЭлТех\CircuitDesign_lab_0\source\input.txt", "r") as f:
    lines = f.readlines()

# for i in range(len(lines)):
#     line = str(i + 1) + " & " + " & ".join(lines[i].split()) + " \\\\ "
#     print(line)

# print("\n\n\n")
# for i in range(len(lines)):
#     line = str(i + 1) + " & " + " & ".join([str(round(int(x) / 625, 3)) if i == 1 else str(int(x)) for i, x in enumerate(lines[i].split())]) + " \\\\ "
#     print(line)

ans = [[i] for i in range(1, 18)]
flag = 0
for n, i in enumerate(lines):
    i = i.strip()
    match i:
        case 'xxxx':
            flag = 1
            continue
        case 'yyyy':
            flag = 2
            continue  
    
    match flag:
        case 0:
            ans[n] += [i]
        case 1:
            ans[n - 18] += [i]
        case 2:
            ans[n - 18*2-1] += [i]
for line in ans:
    print(*line, sep=' & ', end=' \\\\\n')