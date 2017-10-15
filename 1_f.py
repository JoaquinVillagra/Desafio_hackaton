from sklearn.ensemble import RandomForestClassifier #para implementar el random forest
import numpy as np
import pandas
from sklearn import cross_validation


#se lee la base de datos
data = pandas.read_csv('./data_prueba/NO_C_2017.csv')
data1 = pandas.read_csv('./data_prueba/A.csv')
data2 = pandas.read_csv('./data_prueba/B.csv')
data3 = pandas.read_csv('./data_prueba/C.csv')
data4 = pandas.read_csv('./data_prueba/D.csv')

#son unidad
datos = pandas.concat([data, data1, data2, data3, data4])

#la base de datos es mesclada
datos = datos.sample(frac = 1)
datos = datos.sample(frac = 1)
datos = datos.sample(frac = 1)

#seleccionamos las caracteristicas con mayor importancia
selectOpt = ["hackathon.status_salud_publica","hackathon.edad","hackathon.estrato","hackathon.ind_morosidad1","hackathon.ind_morosidad2","hackathon.cant_personas_fam","hackathon.cant_hijos_fam","hackathon.tot_mont","hackathon.cant_autos"]

#se seleccionan las caracteristicas desde el dataframe
datos = datos.loc[:,selectOpt]
datos = datos.reset_index(drop=True)

#son pasados los estados a una variable binaria
datos.loc[datos["hackathon.status_salud_publica"] == "S", "hackathon.status_salud_publica"]= 1
datos.loc[datos["hackathon.status_salud_publica"] == "N", "hackathon.status_salud_publica"]= 0

3son discretizados los estratos sociales
datos.loc[datos["hackathon.estrato"] == "SIN CLASIFICACION", "hackathon.estrato"]= 0
datos.loc[datos["hackathon.estrato"] == "ABC1", "hackathon.estrato"]= 5
datos.loc[datos["hackathon.estrato"] == "C2", "hackathon.estrato"]= 4
datos.loc[datos["hackathon.estrato"] == "C3", "hackathon.estrato"]= 3
datos.loc[datos["hackathon.estrato"] == "D", "hackathon.estrato"]= 2
datos.loc[datos["hackathon.estrato"] == "E", "hackathon.estrato"]= 1

#se indica que son columnas enteras
datos["hackathon.status_salud_publica"] = datos["hackathon.status_salud_publica"].astype('int')
datos["hackathon.edad"] = datos["hackathon.edad"].astype('int')
datos["hackathon.estrato"] = datos["hackathon.estrato"].astype('int')
datos["hackathon.ind_morosidad1"] = datos["hackathon.ind_morosidad1"].astype('int')
datos["hackathon.ind_morosidad2"] = datos["hackathon.ind_morosidad2"].astype('int')

#se crea un modelo de random forest
model = RandomForestClassifier(n_estimators=700)
#se realiza validacion cruzada
cv = cross_validation.KFold(len(datos), n_folds=8)


print "Se inicia Random Forest"

vp = 0
vn = 0
fp = 0
fn = 0
it = 0

#se inicia la validacion cruzada
for traincv, testcv in cv:
    
    probas = model.fit(datos.loc[traincv].loc[:, 'hackathon.edad':].values, datos.loc[traincv]['hackathon.status_salud_publica'].values).predict(datos.loc[testcv].loc[:, 'hackathon.edad':].values)
    
    print "iteracion: %i"%(it)
    for i in range(len(testcv)):
        if(datos.loc[testcv[i]]['hackathon.status_salud_publica'] == 0 and probas[i] == datos.loc[testcv[i]]['hackathon.status_salud_publica']):
            vp+=1
        elif(datos.loc[testcv[i]]['hackathon.status_salud_publica'] == 0 and probas[i] != datos.loc[testcv[i]]['hackathon.status_salud_publica']):
            fp+=1
        elif(datos.loc[testcv[i]]['hackathon.status_salud_publica'] == 1 and probas[i] == datos.loc[testcv[i]]['hackathon.status_salud_publica']):
            vn+=1
        elif(datos.loc[testcv[i]]['hackathon.status_salud_publica'] == 1 and probas[i] != datos.loc[testcv[i]]['hackathon.status_salud_publica']):
            fn+=1
    it+=1

#son mostrados los resultados
print "Exactitud: ",(vp+vn)/float(vp+vn+fp+fn)
print "%i | %i"%(vp,fp)
print "%i | %i"%(fn,vn)
