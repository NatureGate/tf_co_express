from GENIE3 import *
import pandas as pd
import numpy as np

data = loadtxt('gene_express.txt',skiprows=1)
#idx = np.argwhere(np.all(data[...,:] == 0,axis=0))
#删除全程不表达的基因
#data = np.delete(data,idx,axis=1)

#删除方差为0的基因ps:方差为0其实包含全程不表达
data_vars = np.var(data, axis=0)
zero_vars = np.argwhere(data_vars==0)
data = np.delete(data,zero_vars,axis=1)
idx = list(zero_vars.squeeze(-1))
print (idx)
print (data)
f = open('gene_express.txt')
gene_names = f.readline()
gene_names = gene_names.rstrip('\n').split('\t')
for index in idx:
    gene_names.pop(index)


tfs_families = pd.read_excel("Y1H-5414PDI.xlsx",sheet_name='TF_family')
tfs = tfs_families['TF']
regulators = list(tfs)
VIM = GENIE3(data,gene_names=gene_names,regulators=regulators,nthreads=1)
get_link_list(VIM,gene_names=regulators,regulators=regulators,file_name='ranking.txt')