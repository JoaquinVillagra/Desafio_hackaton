
data <- read.table("archivo.csv", header = TRUE, sep = ",", na.strings = "NA")

dataGeo<-na.omit(data)

error = dataGeo$hackathon.longitud == " "
dataGeo = dataGeo[!error,]

dataGeo = dataGeo[2:5]

dataGeo<-scale(dataGeo)
#Cargi biblioteca
library("cluster")
library("mclust") #cargar biblioteca
dataGeo$hackathon.longitud<-as.double(dataGeo$hackathon.latitud)
dataGeo$hackathon.latitud<-as.double(dataGeo$hackathon.latitud)

##Este proceso se repitio para k = i para todo i perteneciente a [2:18]
# K-Means Cluster Analysis
fit <- kmeans(dataGeo, 3) # cluster solution
# get cluster means 
aggregate(dataGeo,by=list(fit$cluster),FUN=mean)
# append cluster assignment
dataGeo<- data.frame(dataGeo, fit$cluster)
clusplot(dataGeo, fit$cluster, color=TRUE, shade=TRUE, lines=0, main="Cluster", xlab="Componente 1", ylab="Componente 2")


