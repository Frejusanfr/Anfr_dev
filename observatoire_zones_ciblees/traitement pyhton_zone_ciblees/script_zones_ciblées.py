import pandas as pd
import csv
import numpy
import math
from datetime import datetime
file_4G_France=pd.read_csv('observatoire.csv',sep=';', encoding='latin-1')
file_4G_France["emr_dt_service"] = pd.to_datetime(file_4G_France["emr_dt_service"], infer_datetime_format=True)
date = pd.to_datetime(input('Entrer la date au format dd/mm/yyyy  '),format='%d/%m/%Y')
file_4G_France = file_4G_France.loc[(file_4G_France.emr_dt_service < date)]
file_4G_France = file_4G_France[file_4G_France['en_service'] == "En service"]
file_4G_France.sort_values(by = ["emr_dt_service"], inplace = True)
file_4G_France=file_4G_France.drop_duplicates(subset=['adm_lb_nom', 'sup_id', 'emr_lb_systeme'])
file_7=file_4G_France[file_4G_France['sta_nm_dpt'] == "02B" ]
file_8= file_4G_France[file_4G_France['sta_nm_dpt'] == "02A"]
file_4G_France = file_4G_France[file_4G_France['sta_nm_dpt'] != "02B"]
file_4G_France = file_4G_France[file_4G_France['sta_nm_dpt'] != "02A"]
file_4G_France=file_4G_France[file_4G_France['sta_nm_dpt'].astype('int64') <= 95]
file_4G_France = pd.concat([file_7,file_8,file_4G_France], ignore_index=True)
def transform(data):
    buffer = data.split(',')
    obj = dict()
    obj["coordonnee_y"] = buffer[0]
    obj["coordonnee_x"] = buffer[1]
    return obj
resultat = list(map(lambda x: transform(x),  list(file_4G_France["coordonnees"])))
Y = list(map(lambda x: x["coordonnee_y"], resultat))
X = list(map(lambda x: x["coordonnee_x"], resultat))
dt = file_4G_France.copy()
dt.insert(21, 'coordonnee_X', X)
dt.insert(22, 'coordonnee_Y', Y)
dt = dt.drop('coordonnees', axis=1)
val = 1
#for ind, row in dt.iterrows():
#    dt.loc[ind,"id"]=val
#    val=val+1
dt.to_csv("Fichier_QGIS.csv",index = False, header=True)
dt.shape
print("Traitement achévé |:")