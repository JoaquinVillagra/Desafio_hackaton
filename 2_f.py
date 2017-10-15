
from sklearn.ensemble import RandomForestClassifier #para implementar el random forest
import numpy as np
import pandas
from sklearn import cross_validation

#son leidos los archivos
data1 = pandas.read_csv('A.csv')
data2 = pandas.read_csv('B.csv')
data3 = pandas.read_csv('C.csv')
data4 = pandas.read_csv('D.csv')

#son unidos
datos = pandas.concat([data1, data2, data3, data4])

#se mesclan
datos = datos.sample(frac = 1)
datos = datos.sample(frac = 1)
datos = datos.sample(frac = 1)

#seleccionamos las caracteristicas
selectOpt = ["hackathon.tramo_salud_publico","hackathon.edad","hackathon.estrato","hackathon.ind_morosidad1","hackathon.ind_morosidad2","hackathon.cant_personas_fam","hackathon.cant_hijos_fam","hackathon.tot_mont","hackathon.cant_autos"]

datos = datos.loc[:,selectOpt]

datos = datos.reset_index(drop=True)

#se cambia el valor de las clases a numericos
datos.loc[datos["hackathon.tramo_salud_publico"] == "A", "hackathon.tramo_salud_publico"]= 0
datos.loc[datos["hackathon.tramo_salud_publico"] == "B", "hackathon.tramo_salud_publico"]= 1
datos.loc[datos["hackathon.tramo_salud_publico"] == "C", "hackathon.tramo_salud_publico"]= 2
datos.loc[datos["hackathon.tramo_salud_publico"] == "D", "hackathon.tramo_salud_publico"]= 3

#se puede ver la clasificacion
datos.loc[datos["hackathon.estrato"] == "SIN CLASIFICACION", "hackathon.estrato"]= 0
datos.loc[datos["hackathon.estrato"] == "ABC1", "hackathon.estrato"]= 5
datos.loc[datos["hackathon.estrato"] == "C2", "hackathon.estrato"]= 4
datos.loc[datos["hackathon.estrato"] == "C3", "hackathon.estrato"]= 3
datos.loc[datos["hackathon.estrato"] == "D", "hackathon.estrato"]= 2
datos.loc[datos["hackathon.estrato"] == "E", "hackathon.estrato"]= 1

#las columnas son transformadas a enteros
datos["hackathon.tramo_salud_publico"] = datos["hackathon.tramo_salud_publico"].astype('int')
datos["hackathon.edad"] = datos["hackathon.edad"].astype('int')
datos["hackathon.estrato"] = datos["hackathon.estrato"].astype('int')
datos["hackathon.ind_morosidad1"] = datos["hackathon.ind_morosidad1"].astype('int')
datos["hackathon.ind_morosidad2"] = datos["hackathon.ind_morosidad2"].astype('int')

print "Inicio del Random Forest"

model = RandomForestClassifier(n_estimators=500)
#se realiza validacion cruzada
cv = cross_validation.KFold(len(datos), n_folds=5)


print "Se inicia Random Forest"

suma_respuesta = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

it = 0

#se inicia la validacion cruzada
for traincv, testcv in cv:
    
    clf = model.fit(datos.loc[traincv].loc[:, 'hackathon.edad':].values, datos.loc[traincv]['hackathon.tramo_salud_publico'].values)
    
    probas = clf.predict(datos.loc[testcv].loc[:, 'hackathon.edad':])

    respuesta = pandas.crosstab(datos.loc[testcv]["hackathon.tramo_salud_publico"], probas, rownames=['Actual'], colnames=['Predicted'])
    
    suma_respuesta[0]+=respuesta[0][0]
    suma_respuesta[1]+=respuesta[1][0]
    suma_respuesta[2]+=respuesta[2][0]
    suma_respuesta[3]+=respuesta[3][0]
    suma_respuesta[4]+=respuesta[0][1]
    suma_respuesta[5]+=respuesta[1][1]
    suma_respuesta[6]+=respuesta[2][1]
    suma_respuesta[7]+=respuesta[3][1]
    suma_respuesta[8]+=respuesta[0][2]
    suma_respuesta[9]+=respuesta[1][2]
    suma_respuesta[10]+=respuesta[2][2]
    suma_respuesta[11]+=respuesta[3][2]
    suma_respuesta[12]+=respuesta[0][3]
    suma_respuesta[13]+=respuesta[1][3]
    suma_respuesta[14]+=respuesta[2][3]
    suma_respuesta[15]+=respuesta[3][3]
    
    print "iteracion: %i"%(it)
    it+=1

#son mostrados los resultados
print "Exactitud: ",(suma_respuesta[0]+suma_respuesta[5]+suma_respuesta[10]+suma_respuesta[15])/float(len(datos))
print "%i | %i | %i | %i"%(suma_respuesta[0],suma_respuesta[1],suma_respuesta[2],suma_respuesta[3])
print "%i | %i | %i | %i"%(suma_respuesta[4],suma_respuesta[5],suma_respuesta[6],suma_respuesta[7])
print "%i | %i | %i | %i"%(suma_respuesta[8],suma_respuesta[9],suma_respuesta[10],suma_respuesta[11])
print "%i | %i | %i | %i"%(suma_respuesta[12],suma_respuesta[13],suma_respuesta[14],suma_respuesta[15])
