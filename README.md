Comenzamos con la tarea 1
Incluimos otros programas que usaremos y una carpeta llamada capturas

Agregamos otro código basado en el básico modificando el optimizador y agregamos una captura de pantalla de prueba ajena al código.

En el código temp.py hicimos la primera corrida del código base para probarlo sin cambiar nada, agregando la captura de pantalla de compilación 1.

Observamos que en la prueba 1, con 100 neuronas, la red entrena mucho más lento y baja significativamente su eficiencia a menos del 70%.

En la prueba 2, asignamos la tasa de aprendizaje a 0.001, y la red al final aumenta al 95% de eficiencia, un 1% mas que el código base.

En la prueba 3, asignamos una tasa de aprendizaje de 50, y la red al final se mantiene en 94%, la misma eficiencia que el código original.

Me encuentro atorado en implementar correctamente el optimizador RMSPROP.

Resolviendo el punto anterior, se introdujeron ciertas variables epsilon, delta y "g" para introducir el modelo matemático del optimizador RMSPROP

Corremos la red con RMS con 100 neuronas pero es muy lento el entrenamiento. Comienza con una eficiencia muy baja (debajo del 40%) y en 30 épocas no alcanza al final el 70% de efectividad.

Corremos la red con RMS con 30 neuronas y con una tasa de aprendizaje de 0.001 y vimos que la red mejoró su eficiencia que en caso pasado pero no mejora su eficiencia que en el código original. Se mantiene igual.

Introducimos un código donde implementamos la capa cross entropy eliminando un renglón en la Línea 124. 

Implementando cross entropy al código network 5 que tambien tiene el optimizador rms, vemos que al correr el programa la eficiencia al final de la ultima epoca se mantiene igual, 94%. 
Vemos que la eficiencia del código con cross entropy y con rms es la misma prácticamente que la del código original. Podemos concluir que se pudo aumentar la eficiencia en la prueba 2, unicamente cambiando el valor de la tasa a 0.001 con 30 neuronas.