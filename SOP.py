CYAN = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
WARNING = '\033[93m'

info = [[1, 12, 10, 20, 1, 1], [2, 10, 1, 12, 0, 0], [3, 11, 2, 21, 1, 0],
        [4, 12, 0, 22, 1, 0]]

print(CYAN + '== FIFO ==' + RESET)

time = info[0][1]
frame_1 = 0

for i in range(len(info)):
    j = info[i][1]
    if j < time:
        time = j
        frame_1 = info[i][0]
    i = i + 1

print('Frame =>', frame_1)
print('Tempo de carga =>', time)

print(' ')

print(GREEN + '== LFU ==' + RESET)

qtd = info[0][1]
frame_2 = 0

for q in range(len(info)):
    u = info[q][2]
    if u < qtd:
        qtd = u
        frame_2 = info[q][0]
    q = q + 1

print('Frame =>', frame_2)
print('Quantidade de referências =>', qtd)

print(' ')

print(WARNING + '== LRU ==' + RESET)

last_ref = info[0][1]
frame_3 = 0

for h in range(len(info)):
    o = info[h][3]
    if o > last_ref:
        last_ref = o
        frame_3 = info[h][0]
    h = h + 1

print('Frame =>', frame_3)
print('Tempo da última referência =>', last_ref)

print(' ')

print(CYAN + '== NRU ==' + RESET)

frame_4 = 0

for a in range(len(info)):
    br = info[a][4]
    bm = info[a][5]
    if br == bm:
        if br == 0:
            if bm == 0:
                frame_4 = info[a][0]
            a = a + 1

print('BR =>', br)
print('BM =>', bm)
print('Frame =>', frame_4)
