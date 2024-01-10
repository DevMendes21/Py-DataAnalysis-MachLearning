import pandas as pd
import numpy as np
import copy

tabela = pd.DataFrame({'nome':['Rafael','Yago','Primo'], 'nota':[10,9,7]})

tabela2 = np.array(tabela)

tabela3 = copy.deepcopy(tabela)

tabela3.loc[0,'nota'] = 3