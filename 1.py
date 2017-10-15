from pyspark.sql import HiveContext
from pyspark import SparkContext

from pyspark.ml.classification import RandomForestClassifie
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.ml.feature import IndexToString, StringIndexer, VectorIndexer
from pyspark.ml import Pipeline

import numpy as np

header = ["hackathon.profesion","hackathon.actividad","hackathon.est_civil","hackathon.sexo_desc","hackathon.tipo_nacionalidad","hackathon.edad", "hackathon.estrato","hackathon.ind_defuncion","hackathon.ind_interd","hackathon.n_direccion","hackathon.comuna","hackathon.ind_region_rm","hackathon.avaluo_bbrr","hackathon.cant_bbrr","hackathon.avaluo_auto","hackathon.cant_autos","hackathon.n_actividad","hackathon.n_rubros","hackathon.clean2","hackathon.tot_docs","hackathon.tot_mont","hackathon.ind_morosidad1","hackathon.ind_morosidad2","hackathon.ind_consultas_id","hackathon.status_salud_publica","hackathon.tramo_salud_publico","hackathon.cant_personas_fam","hackathon.can_vivos_fam","hackathon.cant_hijos_fam","hackathon.longitud","hackathon.latitud","hackathon.periodo"]

entrada = ["hackathon.edad","hackathon.estrato","hackathon.comuna",
          "hackathon.ind_morosidad1","hackathon.ind_morosidad2","hackathon.cant_hijos_fam"]

salida = "hackathon.status_salud_publica"

if not globals().has_key('sc'):
    sc = SparkContext()

sqlContext = HiveContext(sc)
items = sqlContext.sql("SELECT * FROM hackaton WHERE hackaton periodo = 2017")

data = items.collect()

(trainingData, testData) = data.randomSplit([0.7, 0.3])

#llabelIndexer = StringIndexer(inputCol=salida, outputCol="indexedLabel").fit(data)

#featureIndexer = VectorIndexer(inputCol=entradas, outputCol="indexedFeatures").fit(data)


#rf = RandomForestClassifier(labelCol=salida, featuresCol=entrada, numTrees=10)
#labelConverter = IndexToString(inputCol=salida, outputCol=entrada, labels=labelIndexer.labels)

#pipeline = Pipeline(stages=[labelIndexer, featureIndexer, rf, labelConverter])

# Train model.  This also runs the indexers.
#model = pipeline.fit(trainingData)

# Make predictions.
#predictions = model.transform(testData)

# Select example rows to display.
#predictions.select("predictedLabel", "label", "features").show(5)

# Select (prediction, true label) and compute test error
#evaluator = MulticlassClassificationEvaluator(
 #   labelCol="indexedLabel", predictionCol="prediction", metricName="accuracy")
#accuracy = evaluator.evaluate(predictions)
#print("Test Error = %g" % (1.0 - accuracy))

#rfModel = model.stages[2]
#print(rfModel)  # summary only