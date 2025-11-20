**Conclusiones**

_Desempeño del modelo:_

El modelo mostró un desempeño razonable. Al evaluar sobre los datos de entrenamiento, el modelo obtuvo un MAE de 27.095 dólares, lo que indica que en promedio, las predicciones se desvian del valor real en ese monto. Sobre los datos del test, el MAE fue de 28.389 dólares, muy cercano al de entrenamiento.

Esto nos muestra que el modelo mantiene su capacidad predictiva con datos nuevos, lo cual es una buena señal de generalización.

El MSE también fue similar entre entrenamiento y test, lo que significa que el comportamiento del modelo es esable y aprende de patrones generales del dataset. Entonces podriamos decir que el modelo presenta un desempeño coherente.


-------------------------------------------------------------------


_¿Las features extraidas del dataset fueron buenas predictoras?_

Las features seleccionadas representan caracteristicas tipicamente usadas en la predicion del precio de una vivienda: superficie, cantidad de habitaciones, tamaño del garaje, etc. Con estas variables el modelo logró errores relativamente bajos y una buena generalizacion entre entrenamiento y test, lo cual indica que las features sí aportaron información útil para el modelo.

Sin embargo, para que el modelo sea mejor se podrian incluir variables como:

*   Ubicación de la casa
*   Estado de mantenimiento
*   Calidad de construcción y materiales
*   Posee patio, pileta o terraza

Estas variables forman gran parte del valor de una propiedad y nos ayudaria a reducir el error del modelo.


-------------------------------------------------------------------


_La variable más influyente según los coeficientes del modelo_


La variable más influyente en el precio de la casa es el número de coches que caben en el garaje, ya que presenta el coeficiente positivo más alto: 18.584. Le sigue el número de baños, también con un impacto considerable: 12.975. Por otro lado, la variable con mayor influencia negativa es el número de cocinas, que posee un coeficiente de -51.582.




-------------------------------------------------------------------


  
_Comparativa de resultados de evaluación del modelo con los datos de Entrenamiento y de Test_

Al comparar los resultados de la evaluacion del modelo con los datos de entrenamiento y test podemos observar que los valores son muy similares:


*   MAE (entrenamiento) = 27.095
*   MAE (test) = 28.389

La diferencia entre ellos es pequeña, lo que significa que el modelo generaliza adecuadamente y no presenta sobreajuste. Se ajusta bien a los datos disponibles y logra capturar relaciones significativas entre las variables.


-------------------------------------------------------------------



_Otras conlcusiones_

Tambíen se calculó el coeficiente de determinación R^2, el de train fue de  0.71 y el de test de 0.70. Esto nos indica que el modelo explica alrededor del 70% de la variabilidad del precio de las viviendas. La diferencia entre ambos valores es mínima, por lo que el modelo generaliza bien y no presenta sobreajuste. 

