
data <- read.table("cienmil.csv", header = TRUE, sep = ",", na.strings = "NA")

header = c("hackathon.profesion","hackathon.actividad","hackathon.est_civil","hackathon.sexo_desc","hackathon.tipo_nacionalidad","hackathon.edad", "hackathon.estrato","hackathon.ind_defuncion","hackathon.ind_interd","hackathon.n_direccion","hackathon.comuna","hackathon.ind_region_rm","hackathon.avaluo_bbrr","hackathon.cant_bbrr","hackathon.avaluo_auto","hackathon.cant_autos","hackathon.n_actividad","hackathon.n_rubros","hackathon.clean2","hackathon.tot_docs","hackathon.tot_mont","hackathon.ind_morosidad1","hackathon.ind_morosidad2","hackathon.ind_consultas_id","hackathon.status_salud_publica","hackathon.tramo_salud_publico","hackathon.cant_personas_fam","hackathon.cant_vivos_fam","hackathon.cant_hijos_fam","hackathon.longitud","hackathon.latitud","hackathon.periodo")


for(i in 1:(length(header))){
  suma = sum(data[,header[i]] != " ")
  print(paste("header: ",header[i]," suma: ",suma))
}

# [1] "header:  hackathon.profesion  suma:  3796"
# [1] "header:  hackathon.actividad  suma:  67210"
# [1] "header:  hackathon.est_civil  suma:  96595"
# [1] "header:  hackathon.sexo_desc  suma:  100000"
# [1] "header:  hackathon.tipo_nacionalidad  suma:  97796"
# [1] "header:  hackathon.edad  suma:  100000"
# [1] "header:  hackathon.estrato  suma:  100000"
# [1] "header:  hackathon.ind_defuncion  suma:  100000"
# [1] "header:  hackathon.ind_interd  suma:  35529"
# [1] "header:  hackathon.n_direccion  suma:  100000"
# [1] "header:  hackathon.comuna  suma:  100000"
# [1] "header:  hackathon.ind_region_rm  suma:  100000"
# [1] "header:  hackathon.avaluo_bbrr  suma:  100000"
# [1] "header:  hackathon.cant_bbrr  suma:  100000"
# [1] "header:  hackathon.avaluo_auto  suma:  100000"
# [1] "header:  hackathon.cant_autos  suma:  100000"
# [1] "header:  hackathon.n_actividad  suma:  100000"
# [1] "header:  hackathon.n_rubros  suma:  100000"
# [1] "header:  hackathon.clean2  suma:  100000"
# [1] "header:  hackathon.tot_docs  suma:  100000"
# [1] "header:  hackathon.tot_mont  suma:  100000"
# [1] "header:  hackathon.ind_morosidad1  suma:  100000"
# [1] "header:  hackathon.ind_morosidad2  suma:  100000"
# [1] "header:  hackathon.ind_consultas_id  suma:  100000"
# [1] "header:  hackathon.status_salud_publica  suma:  100000"
# [1] "header:  hackathon.tramo_salud_publico  suma:  100000"
# [1] "header:  hackathon.cant_personas_fam  suma:  100000"
# [1] "header:  hackathon.cant_vivos_fam  suma:  100000"
# [1] "header:  hackathon.cant_hijos_fam  suma:  100000"
# [1] "header:  hackathon.longitud  suma:  85586"
# [1] "header:  hackathon.latitud  suma:  85586"
# [1] "header:  hackathon.periodo  suma:  100000"

#cantidad de gente que pertenece y cantidad que no pertenece
pertenece = sum(data[,"status_salud_publica"] == "S")
print(paste("pertenece: ",pertenece))
print(paste("No pertenece: ",1000000-pertenece))