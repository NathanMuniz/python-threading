# python-threading
learning to manage threading in python.

## Exemplo 1 [ [ex1](exemplos/ex1.py) ]

Uma forma de ver com clareza como o uso de Threads pode ser útil é contabilizando o tempo que seu código executa ************************sem threads************************ e **************com threads**************. 

Para isso, iremos usar o método ****************************perf_counter**************************** que retorna o tempo de execução do código até o momento em que ele foi chamado. Sendo assim, marcamos um ************início,************ o momento em que queremos **********parar********** de marcar, e a diferença entre eles será o tempo final. 

```python
from time import perf_counter

inicio = perf_counter()

## code 

pausa = perf_counter()

final = pausa - inicio
```

Então criamos um função que faça algo, para simular um processo a ser executado. É importante que essa função leve um certo tempo para terminar, por isso usaremos o método sleep para que nossa função leve um certo tempo para encerrar. 

Queremos executar essa função 10 vezes, e ver quanto tempo nosso código leva para fazer isso.

```python
from time import perf_counter, sleep

inicio = perf_counter()

def dormindo_por_seg(segundos):
    print(f'Dormindo por {segundos}segs')
    sleep(segundos)
    print('Terminou')
    

for c in range(0, 10):
    dormindo_por_seg(1)

pausa = perf_counter()

temp_final = pausa - inicio 

print(f'Seu código levou {temp_final} para executar')
```

Após a execução, vemos que nosso código levou 10 segundos para ser executado. Isso acontece porque ele é executado de forma síncrona, ou seja, um função só é executada após uma outra função terminar. 

Contudo, esse tempo que nossas funções estão “dormindo” se torna um desperdício, outras coisas poderiam estar ocorrendo enquanto elas dormem. Aqui é onde entra a programação assíncrona. 

Executaremos nossa função em **threads** separadas. Criamos um **lista** onde teremos todas essa thredas. Então criamos, startamos e adicionamos cada thread lista de threads. Após isso, iremos usar **join** para cada thread em nossa **lista de threads,** isso fará com que as **threads** sejam encerradas, assim que a ultima encerrar.

```python
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
```

Após a execução, vemos que diferente do caso anterior, nosso código levou apenas 1s para terminar. Isso acontece porque a primeira thread é executada, porém ela tem um tempo de 1s de espera, e nesse tempo as outras threads são executadas. 

Nosso código agora está assíncrona, pois ele não é executado de forma sequencial, o retorno da primeira função ocorreu após todas as outras funções serem iniciadas.
