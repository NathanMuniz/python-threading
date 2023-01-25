# python-threading
learning to manage threading in python.

## Exemplo 1

[ex1](exemplos/ex1.py)

Uma forma de ver com clareza como o uso de Threads pode ser útil é contabilizando o tempo que seu código executa ************************sem threads************************ e **************com threads**************. 

Para isso, iremos usar o método ****************************perf_counter**************************** que retorna o tempo de execução do código até o moment em que ele foi chamado. Sendo assim, marcamos um ************inicio,************  o momento em que queremos **********parar********** de marcar, e a diferença entre eles será o tempo final.
