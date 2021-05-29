start = int(input())
end = int(input())

nBissextos = 0
for ano in range(start, end + 1):
    if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
        print(ano)
        nBissextos += 1

print('bissextos:', nBissextos)
