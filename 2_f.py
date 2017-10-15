from sklearn.ensemble import RandomForestClassifier #para implementar el random forest
import numpy as np
import pandas
from sklearn import cross_validation

data1 = pandas.read_csv('A.csv')
data2 = pandas.read_csv('B.csv')
data3 = pandas.read_csv('C.csv')
data4 = pandas.read_csv('D.csv')

datos = pandas.concat([data1, data2, data3, data4])

datos = datos.sample(frac = 1)
datos = datos.sample(frac = 1)
datos = datos.sample(frac = 1)

#print datos

#seleccionamos las caracteristicas
selectOpt = ["hackathon.tramo_salud_publico","hackathon.edad","hackathon.estrato","hackathon.ind_morosidad1","hackathon.ind_morosidad2","hackathon.cant_personas_fam","hackathon.cant_hijos_fam","hackathon.tot_mont","hackathon.cant_autos"]

datos = datos.loc[:,selectOpt]

datos = datos.reset_index(drop=True)

#datos.loc[datos["hackathon.status_salud_publica"] == "S", "hackathon.status_salud_publica"]= 1
#datos.loc[datos["hackathon.status_salud_publica"] == "N", "hackathon.status_salud_publica"]= 0
datos.loc[datos["hackathon.tramo_salud_publico"] == "A", "hackathon.tramo_salud_publico"]= 0
datos.loc[datos["hackathon.tramo_salud_publico"] == "B", "hackathon.tramo_salud_publico"]= 1
datos.loc[datos["hackathon.tramo_salud_publico"] == "C", "hackathon.tramo_salud_publico"]= 3
datos.loc[datos["hackathon.tramo_salud_publico"] == "D", "hackathon.tramo_salud_publico"]= 4

datos.loc[datos["hackathon.estrato"] == "SIN CLASIFICACION", "hackathon.estrato"]= 0
datos.loc[datos["hackathon.estrato"] == "ABC1", "hackathon.estrato"]= 5
datos.loc[datos["hackathon.estrato"] == "C2", "hackathon.estrato"]= 4
datos.loc[datos["hackathon.estrato"] == "C3", "hackathon.estrato"]= 3
datos.loc[datos["hackathon.estrato"] == "D", "hackathon.estrato"]= 2
datos.loc[datos["hackathon.estrato"] == "E", "hackathon.estrato"]= 1

#data.loc[:, 'hackathon.edad':] = (data.loc[:, 'hackathon.edad':] - data.loc[:, 'hackathon.edad':].mean()) / (data.loc[:, 'hackathon.edad':].std())
datos["hackathon.tramo_salud_publico"] = datos["hackathon.tramo_salud_publico"].astype('int')
datos["hackathon.edad"] = datos["hackathon.edad"].astype('int')
datos["hackathon.estrato"] = datos["hackathon.estrato"].astype('int')
#datos["hackathon.comuna"] = datos["hackathon.comuna"].astype('int')
datos["hackathon.ind_morosidad1"] = datos["hackathon.ind_morosidad1"].astype('int')
datos["hackathon.ind_morosidad2"] = datos["hackathon.ind_morosidad2"].astype('int')

print "random forest" 

model = RandomForestClassifier(n_estimators=500)

np.random.seed(123)
m_train    = np.random.rand(len(datos)) < 0.7
df_train = datos.iloc[m_train,]

df_train = df_train.reset_index(drop=True)

df_test  = datos.iloc[~m_train,]

df_test = df_test.reset_index(drop=True)

# MODELO
clf = model.fit(df_train.loc[:, 'hackathon.edad':], df_train["hackathon.tramo_salud_publico"])
#modelo = LogisticRegression(random_state=1)
#modelo.fit(df_train[headers], df_train["hackathon.status_salud_publica"])
probas = clf.predict(df_test.loc[:, 'hackathon.edad':])

print pandas.crosstab(df_test["hackathon.tramo_salud_publico"], probas, rownames=['Actual'], colnames=['Predicted'])
