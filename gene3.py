from GENIE3 import *
import pandas as pd


data = pd.read_excel("Dd_counts_czw.xlsx")
tfs_families = pd.read_excel("Y1H-5414PDI.xlsx")
tfs = tfs_families['TF']
print(data.shape,tfs.shape)

stages = ['egg', 'j2', 'j3j4', 'male', 'female']
#求平均值
for idx, stage in enumerate(stages):
    data[stage] = data.iloc[:, idx + 1:idx + 3].mean(axis=1)
    #print(data[stage])
print(data.head())
#选择列
##tf_datas = data[data.Geneid.isin(tfs)]
#mean_data = tf_datas[['Geneid','egg','j2','j3j4','male','female']]
mean_data = data[['Geneid','egg','j2','j3j4','male','female']]
print(mean_data.head())
t_mean_data = mean_data.T
t_mean_data.to_csv("gene_express.txt",index=False,sep="\t",header=None)


