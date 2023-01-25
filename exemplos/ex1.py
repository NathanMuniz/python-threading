from time import perf_counter, sleep
import threading


inicio = perf_counter()


def dormindo_por_seg(segundos):
    print(f'Dormindo por {segundos}segs')
    sleep(segundos)
    print('Terminou')
    

threads = []

for c in range(0, 10):
    t = threading.Thread(target=dormindo_por_seg, args=[1])
    t.start()
    threads.append(t)


for t in threads:
    t.join()



pausa = perf_counter()

temp_final = pausa - inicio 

print(f'Seu código levou {temp_final} para executar;')
