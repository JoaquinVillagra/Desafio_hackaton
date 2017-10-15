options( java.parameters = "-Xmx8g" )
library(rJava)
library(RJDBC)

cp = c("/usr/lib/hive/lib/hive-jdbc.jar",
       "/usr/lib/hadoop/client/hadoop-common.jar")
.jinit(classpath=cp)

drv <- JDBC("org.apache.hive.jdbc.HiveDriver",
            "/usr/lib/hive/lib/hive-jdbc-standalone.jar",
            identifier.quote="`")

conn <- dbConnect(drv, "jdbc:hive2://localhost:10000/default", "cloudera", "cloudera")

bc_data <- dbGetQuery(conn, "SELECT * FROM hackathon LIMIT 1")

bc_data <- read.table("recortado.csv", header = TRUE, sep = ",")

header = c("PROFESION","ACTIVIDAD","EST_CIVIL","SEXO_DESC","TIPO_NACIONALIDAD","EDAD","ESTRATO","IND_DEFUNCION","IND_INTERD","N_DIRECCION","COMUNA","IND_REGION_RM","AVALUO_BBRR","CANT_BBRR","AVALUO_AUTO","CANT_AUTOS","N_ACTIVIDAD","N_RUBROS","CLEAN2","TOT_DOCS","TOT_MONT","IND_MOROSIDAD1","IND_MOROSIDAD2","IND_CONSULTAS_ID","STATUS_SALUD_PUBLICO","TRAMO_SALUD_PUBLICO","CANT_PERSONAS_FAM","CANT_VIVOS_FAM","CANT_HIJOS_FAM","DIRE_LON","DIRE_LAT","PERIODO")

# Test de correlación entre dos variables de iris
for( i in 1:length(header)){
  test <- cor.test(bc_data[header],bc_data[""], method="spearman")
  print(test)
}
#print(test)
#require(randomForest)

#set.seed(21)
#modelo = randomForest(c~ ., data=bc_data, ntree = 500, importance=TRUE, proximity=TRUE, ntry=6)

#print(modelo$importance)

