import csv
import pandas as pd
import numpy as np
from datetime import datetime
merge_file = pd.read_csv('QGIS_FILE.csv',sep=',', encoding='latin-1',low_memory= False)
def sum_frame_by_column(frame, new_col_name, list_of_cols_to_sum):
        frame[new_col_name] = frame[list_of_cols_to_sum].astype(int).sum(axis=1) 
        return(frame) 
collecte = []
boyugues = merge_file [merge_file['adm_lb_nom'] == 'BOUYGUES TELECOM']
orange =merge_file [merge_file['adm_lb_nom'] == 'ORANGE']
sfr = merge_file [merge_file['adm_lb_nom'] == 'SFR']
free = merge_file [merge_file['adm_lb_nom'] == 'FREE MOBILE']
count_boyugues = boyugues.emr_lb_systeme.value_counts()
count_boyugues_total = boyugues.emr_lb_systeme.value_counts().sum()
count_orange = orange.emr_lb_systeme.value_counts()
coun_orange_total = orange.emr_lb_systeme.value_counts().sum()
count_sfr = sfr.emr_lb_systeme.value_counts()
count_sfr_total = sfr.emr_lb_systeme.value_counts().sum()
count_free = free.emr_lb_systeme.value_counts()
count_free_total =  free.emr_lb_systeme.value_counts().sum()
df = pd.DataFrame([list(count_orange) ,list(count_sfr)], columns = ["umts_900", "gsm_900", "umts_2100","lte_800"
                                                                                          ,"lte_1800" ,  "gsm_1800" ,"lte_2600"  , "lte_2100" , "lte_700"])

df = df.append({'umts_900' :count_free[0] , 'gsm_900' : 0 , 'umts_2100' : count_free[1] ,  'lte_800' : 0 , 'lte_1800' :count_free[3]  ,'gsm_1800':0 , 'lte_2600' : count_free[2] , 'lte_2100' : 0 , 'lte_700' : count_free[4] } , ignore_index=True)
df = df.append({'umts_900' :count_boyugues[0] , 'gsm_900' : count_boyugues[1] ,  'lte_800' :  count_boyugues[2] , 'umts_2100' : count_boyugues[3] ,  'lte_1800' :count_boyugues[4]  ,'gsm_1800':count_boyugues[5] , 'lte_2600' : count_boyugues[6] , 'lte_2100' : count_boyugues[7] , 'lte_700' : count_boyugues[8] } , ignore_index=True)
df = df.fillna(0)
df = sum_frame_by_column(df, 'Total_Operateur', [ 'gsm_900' , 'umts_900' , 'lte_800', 'umts_2100', 'lte_1800', 'gsm_1800',"lte_2600" , 'lte_2100', 'lte_700'])
df = df.append({ 'gsm_900' : int(df.gsm_900.sum()) , 'umts_900' : int(df.umts_900.sum()) ,'lte_800' : int(df.lte_800.sum()) , 'umts_2100' : int(df.umts_2100.sum()) , 'lte_1800' : int(df.lte_1800.sum())  , 'lte_2600' : int(df.lte_2600.sum())  , 'gsm_1800' : int(df.gsm_1800.sum()) , 'lte_2100' : int(df.lte_2100.sum()) , 'lte_700' : int(df.lte_700.sum()), 'Total_Operateur':int(df.Total_Operateur.sum()) } , ignore_index=True)
df['Operateurs_gsm'] = ['ORANGE','SFR','FREE MOBILE','BOUYGUES TELECOM','TOTAL_GENERAL']
df.set_index("Operateurs_gsm", inplace = True) 
df_4g = merge_file.copy()
df_4g = df_4g.drop_duplicates(subset=['adm_lb_nom' , 'sup_id' , 'generation'])
boyugues_1 = df_4g [df_4g['adm_lb_nom'] == 'BOUYGUES TELECOM']
orange_1 = df_4g [df_4g['adm_lb_nom'] == 'ORANGE']
sfr_1 = df_4g[df_4g['adm_lb_nom'] == 'SFR']
free_1 = df_4g[df_4g['adm_lb_nom'] == 'FREE MOBILE']
boyugues_1_2G = len(boyugues_1[boyugues_1['generation'] == '2G'])
boyugues_1_3G = len(boyugues_1[boyugues_1['generation'] == '3G'])
boyugues_1_4G = len(boyugues_1[boyugues_1['generation'] == '4G'])
orange_1_2G = len(orange_1[orange_1['generation'] == '2G'])
orange_1_3G = len(orange_1[orange_1['generation'] == '3G'])
orange_1_4G = len(orange_1[orange_1['generation'] == '4G'])
sfr_1_2G = len(sfr_1[sfr_1['generation'] == '2G'])
sfr_1_3G = len(sfr_1[sfr_1['generation'] == '3G'])
sfr_1_4G = len(sfr_1[sfr_1['generation'] == '4G'])
free_1_2G =len(free_1[free_1['generation'] == '2G'])
free_1_3G =len(free_1[free_1['generation'] == '3G'])
free_1_4G = len(free_1[free_1['generation'] == '4G'])
data_4g = {'Operateurs_mobiles':  ['BOUYGUES TELECOM' ,'ORANGE' , 'SFR' , 'FREE MOBILE','Total_General'],
          '2G': [boyugues_1_2G , orange_1_2G , sfr_1_2G , free_1_2G, (boyugues_1_2G+ orange_1_2G+sfr_1_2G+free_1_2G )] ,
           '3G': [boyugues_1_3G,orange_1_3G,sfr_1_3G, free_1_3G, (boyugues_1_3G+orange_1_3G+sfr_1_3G+free_1_3G) ] , 
           '4G': [boyugues_1_4G,orange_1_4G, sfr_1_4G,free_1_4G, (boyugues_1_4G+orange_1_4G+sfr_1_4G+free_1_4G) ] , 
        'Total': [(boyugues_1_2G+boyugues_1_3G+boyugues_1_4G),(orange_1_2G+orange_1_3G+orange_1_4G )
                  , (sfr_1_2G+sfr_1_3G+sfr_1_4G ), (free_1_2G+free_1_3G+free_1_4G )
                  , (boyugues_1_2G+ orange_1_2G+sfr_1_2G+free_1_2G ) + (boyugues_1_3G+orange_1_3G+sfr_1_3G+free_1_3G) + (boyugues_1_4G+orange_1_4G+sfr_1_4G+free_1_4G) ] }
df_4gg = pd.DataFrame (data_4g, columns = ['Operateurs_mobiles','2G','3G','4G','Total'])
dft = merge_file.copy()
dft = dft.drop_duplicates(subset=['sup_id', 'emr_lb_systeme'])
lte_800 = dft[dft['emr_lb_systeme'] == 'LTE 800']
lte_1800 = dft[dft['emr_lb_systeme'] == 'LTE 1800']
lte_2600 = dft[dft['emr_lb_systeme'] == 'LTE 2600']
lte_700 = dft[dft['emr_lb_systeme'] == 'LTE 700']
lte_2100 = dft[dft['emr_lb_systeme'] == 'LTE 2100']
umts_900 = dft[dft['emr_lb_systeme'] == 'UMTS 900']
gsm_900 = dft[dft['emr_lb_systeme'] == 'GSM 900']
umts_2100 = dft[dft['emr_lb_systeme'] == 'UMTS 2100']
gsm_1800 = dft[dft['emr_lb_systeme'] == 'GSM 1800']
len2_total = len(lte_800 )+ len(lte_1800)+ len(lte_2600 ) +len(lte_700 )+len(lte_2100)+len(umts_900)+len(gsm_900)+len(umts_2100)+len(gsm_1800)
data2_4g = {'Systemes':  ['lte_800' ,'lte_1800' , 'lte_2600' , 'lte_700' , 'lte_2100', 'umts_900', 'gsm_900', 'umts_2100', 'gsm_1800', 'Total_General'],
        'Total_Systeme': [ len(lte_800 ) , len(lte_1800), len(lte_2600 ) , len(lte_700 ),len(lte_2100),len(umts_900),len(gsm_900),len(umts_2100),len(gsm_1800) , len2_total ] }
df2_4gg = pd.DataFrame (data2_4g, columns = ['Systemes','Total_Systeme'])
dn=merge_file.copy()
dn=dn.drop_duplicates(subset=["sup_id" , "generation"])
two_g = dn[dn['generation'] == '2G']
three_g = dn[dn['generation'] == '3G']
four_g = dn[dn['generation'] == '4G']
dn_4g = {'Technologie': ["2G", "3G", "4G" ,"Total_general"],
        'Nbre_sup_id': [two_g.sup_id.count() , three_g.sup_id.count() , four_g.sup_id.count() , dn.sup_id.count().sum()] }
dn_4g_dt = pd.DataFrame (dn_4g, columns = ['Technologie', 'Nbre_sup_id'])    
writer = pd.ExcelWriter('Resultat_zone_ciblees.xlsx', engine='xlsxwriter')
# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Nbre_station_par_oper_freq.xlsx', index = True, header=True)
df_4gg.to_excel(writer, sheet_name='Nbre_station_par_operateur.xlsx', index = False, header=True)
df2_4gg.to_excel(writer, sheet_name='Nbre_station_par_systeme.xlsx', index = False, header=True)
dn_4g_dt.to_excel(writer, sheet_name='Nb_de_supports.xlsx', index = False, header=True)
# Close the Pandas Excel writer and output the Excel file.
writer.save()    
print('Traitement_achevé.......||........ANFR')
