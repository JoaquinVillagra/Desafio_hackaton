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

show_databases <- dbGetQuery(conn, "SELECT * FROM hackathon LIMIT 1")


print(show_databases$hackathon.tipo_nacionalidad) 
print(show_databases)
