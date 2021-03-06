# Hackathon: Desafío Big Data.

## Integrantes Equipo Vendetta.
- Ignacio Ibáñez Aliaga
- Matías Vargas Mora
- Joaquín Villagra Pacheco

### Planteamiento de los Problemas
### Problema 1.
El problema se busca solucionar a partir de un bosque de clasificación aleatorio: randomForest, cuyo método consiste en el ensamble
de árboles de decisión con bootstrapping, el cual genera n arboles que para efectos de clasificación un dato a clasificar es evaluado por los 
n arboles y aquel más votado (moda) es el seleccionado.
Debido a la cantidad de datos y en base a la literatura, se establece como 70% entrenamiento y 30% test.

Se debe entender que un modelo de clasificación no es fácil de perfeccionar.
Se efectua una implementación de regresión lógistica utilizada para comprobar reducción de caracteristicas.

Esta implementación está disponible en el archivo: 1_f.py

### Problema 2.
Este problema es solucionado con la misma técnica que el anterior, la diferencia radica a la hora de clasificar en donde la probabilidad 
encontrada logicamente debería corresponder a un nivel mayor de profundidad (probabilidad condicional).

Implementación disponible en: 2_f.py

### Problema 3.
El problema 3 optamos por pasar de él, producto de que los datos presentes en la BD entregada poseía el déficit de la pariedad de
datos entre dos años pertenecientes al mismo individuo. Esto quiere decir, el estado de una persona el año 2016 y la misma persona año 2017,
 situación dificil de identificar producto de la estructura de BD.
En el caso que se ubiese tenido la BD estructurada adecuadamente, como propuesta de solución se ocuparía la prueba de McNemar sobre aquellos
 individuos en las que se vieron modificadas variables como el estrato socio económico.
Si una persona es clasificada erronea por una variable significativa, esto indicaría su proporcion a migrar.

### Problema 4.
*Idea de solución*:
- Se extraen todos los individuos pertenecientes a la RM filtrando a partir del modelo de fuga obtenido en el problema 3 (Primera Capa de datos)
- Obtener la distribución de los centros de salud de todo tipo, ya sea privados o públicos.
- Aplicar función de intersección entre capas. 
- Función que recomiende considerando:
	- La próximidad de la persona al UAP.
	- La lejanía de la persona a algún Servicio de Salud (Público o Privado).
	- La probabilidad de que la persona se cambie.

# Prueba de concepto realizada
Se plantea una idea de concepto extrayendo de la data original todas las personas pertenecientes de la región metropolitana. Visualizando 
así una primera capa de datos, la cual se quería utilizar como base para las operaciones antes descritas. 

El tener una capa de centros medicos actuales permitiría efectuar procesamiento de capas georeferenciales 

## Caracteristicas utilizadas:
BD cargada en una tabla mediante linea de comando de HIVE disponibilizandolos en hadoop. (Imagen adjunta).
Uso de Spark para ejecutar código en python correspondiente a randomForest (python con numpy y pyspark).
Uso de los datos entregados de geolocalización en GoogleMaps para HeatMap con el uso de AngularJS 1.6.

## Resultados:

### Problema 1.
*Exactitud del modelo para clasificar a un individuo perteneciente a Fonasa*
![Prob(Individuo=>Fonasa)](https://github.com/JoaquinVillagra/Desafio_hackaton/tree/master/Imagenes/ExactitudDelModelo_desafio1.png)

A partir de modelo efectuado con RandomForest en Python, logrando una exactitud del 74% en la clasificación. (Código fuente Python: 1_f.py) 

### Problema 2.
*Probabilidad de dado que pertenece a Fonasa, sea del fondo A*
![Prob(A/esDeFonasa)](https://github.com/JoaquinVillagra/Desafio_hackaton/tree/master/Imagenes/TramoA.png)

*Probabilidad de dado que pertenece a Fonasa, sea del fondo B*
![Prob(B/esDeFonasa)](https://github.com/JoaquinVillagra/Desafio_hackaton/tree/master/Imagenes/TramoB.png)

*Probabilidad de dado que pertenece a Fonasa sea del fondo C*
![Prob(C/esDeFonasa)](https://github.com/JoaquinVillagra/Desafio_hackaton/tree/master/Imagenes/TramoC.png)

*Probabilidad de dado que pertenece a Fonasa sea del fondo D*
![Prob(D/esDeFonasa)](https://github.com/JoaquinVillagra/Desafio_hackaton/tree/master/Imagenes/TramoD.png)

A través de la implementación disponible en el archivo 2_f.py, se logra una exactitud de aproximadamente un 48% usando RandomForest para la clasificación de los tramos A,B,C,D del sistema FONASA. 

### Problema 3.
Se fundamento propuesta de solución

### Problema 4.
Se logra a partir de un proceso de Clustering(![ImgClusters](https://github.com/JoaquinVillagra/Desafio_hackaton/tree/master/Imagenes/clustering.png)), un mapa de calor(![Mapa de Calor](https://github.com/JoaquinVillagra/Desafio_hackaton/tree/master/Imagenes/mapa_calor.png)) en donde los pointer de color azul corresponden a los centroides de los tres grupos generados a partir de los datos. Los pointer de color verde corresponden a centros de salud buscados y posicionados manualmente para efectuar correctamente la prueba de concepto propuesta. 






