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


df = df.reset_index(drop=True)

df.loc[df["hackathon.status_salud_publica"] == "S", "hackathon.status_salud_publica"]= 1
df.loc[df["hackathon.status_salud_publica"] == "N", "hackathon.status_salud_publica"]= 0
df.loc[df["hackathon.estrato"] == "SIN CLASIFICACION", "hackathon.estrato"]= 0
df.loc[df["hackathon.estrato"] == "ABC1", "hackathon.estrato"]= 5
df.loc[df["hackathon.estrato"] == "C2", "hackathon.estrato"]= 4
df.loc[df["hackathon.estrato"] == "C3", "hackathon.estrato"]= 3
df.loc[df["hackathon.estrato"] == "D", "hackathon.estrato"]= 2
df.loc[df["hackathon.estrato"] == "E", "hackathon.estrato"]= 1

selectOpt = ["hackathon.status_salud_publica","hackathon.longitud","hackathon.latitud","hackathon.estrato"]

df = df.loc[:,selectOpt]

df.to_csv("archivo.csv")