import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import pandas as pd


#loading the dfset
df1 = pd.read_csv("NO_C_2017.csv")
df2 = pd.read_csv("A.csv")
df3 = pd.read_csv("B.csv")
df4 = pd.read_csv("C.csv")
df5 = pd.read_csv("D.csv")

df = pd.concat([df1,df2,df3,df4,df5])

selectOpt = ["hackathon.status_salud_publica","hackathon.edad","hackathon.estrato","hackathon.ind_morosidad1","hackathon.ind_morosidad2","hackathon.cant_personas_fam","hackathon.cant_hijos_fam","hackathon.tot_mont","hackathon.cant_autos"]

df = df.loc[:,selectOpt]

df = df.reset_index(drop=True)

df.loc[df["hackathon.status_salud_publica"] == "S", "hackathon.status_salud_publica"]= 1
df.loc[df["hackathon.status_salud_publica"] == "N", "hackathon.status_salud_publica"]= 0
df.loc[df["hackathon.estrato"] == "SIN CLASIFICACION", "hackathon.estrato"]= 0
df.loc[df["hackathon.estrato"] == "ABC1", "hackathon.estrato"]= 5
df.loc[df["hackathon.estrato"] == "C2", "hackathon.estrato"]= 4
df.loc[df["hackathon.estrato"] == "C3", "hackathon.estrato"]= 3
df.loc[df["hackathon.estrato"] == "D", "hackathon.estrato"]= 2
df.loc[df["hackathon.estrato"] == "E", "hackathon.estrato"]= 1

#df.loc[:, 'hackathon.edad':] = (df.loc[:, 'hackathon.edad':] - df.loc[:, 'hackathon.edad':].mean()) / (df.loc[:, 'hackathon.edad':].std())
df["hackathon.status_salud_publica"] = df["hackathon.status_salud_publica"].astype('int')
df["hackathon.edad"] = df["hackathon.edad"].astype('int')
df["hackathon.estrato"] = df["hackathon.estrato"].astype('int')
#df["hackathon.comuna"] = df["hackathon.comuna"].astype('int')
df["hackathon.ind_morosidad1"] = df["hackathon.ind_morosidad1"].astype('int')
df["hackathon.ind_morosidad2"] = df["hackathon.ind_morosidad2"].astype('int')
#df["hackathon.cant_bbrr"] = df["hackathon.cant_bbrr"].astype('int')
#df["hackathon.avaluo_bbrr"] = df["hackathon.avaluo_bbrr"].astype('int')
df["hackathon.cant_hijos_fam"] = df["hackathon.cant_hijos_fam"].astype('int')
df["hackathon.cant_personas_fam"] = df["hackathon.cant_personas_fam"].astype('int')

clase_name = 'hackathon.status_salud_publica' # nombre de variable a predecir
headers = df.columns.values.tolist()
headers.remove(clase_name)

# TRAIN TEST
#---------------------------------------------------------------------------------------------
np.random.seed(123)
m_train    = np.random.rand(len(df)) < 0.7
df_train = df.iloc[m_train,]
df_test  = df.iloc[~m_train,]

# MODELO
modelo = LogisticRegression(random_state=1)
modelo.fit(df_train[headers], df_train["hackathon.status_salud_publica"])

# PREDICCION
#---------------------------------------------------------------------------------------------
prediccion = modelo.predict(df_test[headers])

# METRICAS
#---------------------------------------------------------------------------------------------
print(metrics.classification_report(y_true=df_test["hackathon.status_salud_publica"], y_pred=prediccion))
print(pd.crosstab(df_test["hackathon.status_salud_publica"], prediccion, rownames=['REAL'], colnames=['PREDICCION'])) 