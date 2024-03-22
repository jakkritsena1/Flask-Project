import pandas as pd
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error
from tensorflow import keras
df = pd.read_csv("C:\\Users\\Ball.sna\\source\\repos\\jakkritsena1\\Flask-Project\\dataset\\dataset.csv")
class Model_Engine:
    def FrontModel(self):
        inj = 'd_inj_pw_front'
        O2use = 'd_front_o2'
        tpsPCT = 'd_tps_pct'
        map = 'd_map_v'
        ve = 'd_ve_front'
        veNew = 'd_new_ve_front'
        RPM = 'd_eng_speed'
        ve_predict = ''

        


       
     


    def RearModel(self, speed, tps):
        inj = 'd_inj_pw_front'
        O2use = 'd_front_o2'
        tpsPCT = 'd_tps_pct'
        map = 'd_map_v'
        ve = 'd_ve_front'
        veNew = 'd_new_ve_front'
        RPM = 'd_eng_speed'
        ve_predict = ''

