from time import perf_counter, sleep


inicio = perf_counter()


def dormindo_por_seg(segundos):
    print(f'Dormindo por {segundos}segs')
    sleep(segundos)
    print('Terminou')
    

for c in range(0, 9):
    dormindo_por_seg(1)


pausa = perf_counter()

final = inicio - pausa

