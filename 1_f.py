from sklearn.ensemble import RandomForestClassifier #para implementar el random forest
import numpy as np
import pandas
from sklearn import cross_validation

data = pandas.read_csv('./NO_C_2017.csv')
data1 = pandas.read_csv('./A.csv')
data2 = pandas.read_csv('./B.csv')
data3 = pandas.read_csv('./C.csv')
data4 = pandas.read_csv('./D.csv')

datos = pandas.concat([data, data1, data2, data3, data4])

atos = datos.sample(frac = 1)
datos = datos.sample(frac = 1)
datos = datos.sample(frac = 1)

#print datos

#seleccionamos las caracteristicas
selectOpt = ["hackathon.status_salud_publica","hackathon.edad","hackathon.estrato","hackathon.ind_morosidad1","hackathon.ind_morosidad2","hackathon.cant_personas_fam","hackathon.cant_hijos_fam","hackathon.tot_mont","hackathon.cant_autos"]

datos = datos.loc[:,selectOpt]

datos = datos.reset_index(drop=True)

datos.loc[datos["hackathon.status_salud_publica"] == "S", "hackathon.status_salud_publica"]= 1
datos.loc[datos["hackathon.status_salud_publica"] == "N", "hackathon.status_salud_publica"]= 0
datos.loc[datos["hackathon.estrato"] == "SIN CLASIFICACION", "hackathon.estrato"]= 0
datos.loc[datos["hackathon.estrato"] == "ABC1", "hackathon.estrato"]= 5
datos.loc[datos["hackathon.estrato"] == "C2", "hackathon.estrato"]= 4
datos.loc[datos["hackathon.estrato"] == "C3", "hackathon.estrato"]= 3
datos.loc[datos["hackathon.estrato"] == "D", "hackathon.estrato"]= 2
datos.loc[datos["hackathon.estrato"] == "E", "hackathon.estrato"]= 1

#data.loc[:, 'hackathon.edad':] = (data.loc[:, 'hackathon.edad':] - data.loc[:, 'hackathon.edad':].mean()) / (data.loc[:, 'hackathon.edad':].std())
datos["hackathon.status_salud_publica"] = datos["hackathon.status_salud_publica"].astype('int')
datos["hackathon.edad"] = datos["hackathon.edad"].astype('int')
datos["hackathon.estrato"] = datos["hackathon.estrato"].astype('int')
#datos["hackathon.comuna"] = datos["hackathon.comuna"].astype('int')
datos["hackathon.ind_morosidad1"] = datos["hackathon.ind_morosidad1"].astype('int')
datos["hackathon.ind_morosidad2"] = datos["hackathon.ind_morosidad2"].astype('int')

model = RandomForestClassifier(n_estimators=700)

#Simple K-Fold cross validation. 10 folds.
cv = cross_validation.KFold(len(datos), n_folds=8)

vp = 0
vn = 0
fp = 0
fn = 0
it = 0
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
            
print "Exactitud: ",(vp+vn)/float(vp+vn+fp+fn)
print "%i | %i"%(vp,fp)
print "%i | %i"%(fn,vn)
