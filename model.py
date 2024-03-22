import pandas as pd
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error
from tensorflow import keras
df = pd.read_csv("C:\\Users\\Ball.sna\\source\\repos\\jakkritsena1\\Flask-Project\\dataset\\dataset.csv")
class Model_Engine:
    def FrontModel(self, speed, tps):
        inj = 'd_inj_pw_front'
        O2use = 'd_front_o2'
        tpsPCT = 'd_tps_pct'
        map = 'd_map_v'
        ve = 'd_ve_front'
        veNew = 'd_new_ve_front'
        RPM = 'd_eng_speed'

        condition = ((df[RPM] >= 0) & (df[RPM] <= speed) & (df[tpsPCT] <= tps))
        X = df.loc[condition, [tpsPCT,map,RPM,inj,O2use]]
        y = df.loc[condition, [veNew]]

        X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=0)

        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)

        model = keras.Sequential([
        keras.layers.Input(shape=(5,)),
        keras.layers.Dense(32, activation='relu'),
        keras.layers.Dense(32, activation='relu'),
        keras.layers.Dense(64, activation='relu', kernel_regularizer=keras.regularizers.l2(0.01)),
        keras.layers.Dense(1)
                                ])
        model.compile(optimizer='adam', loss=['mean_squared_error'], metrics=['mean_absolute_error'])
        model.fit(X_train, y_train, epochs=1000,
              batch_size=64, validation_split=0.3)

        predictions = model.predict(X_test)
        predictions_avg = np.mean(predictions)

        mse = mean_squared_error(y_test, predictions)
        rmse = np.sqrt(mse)
        mae = mean_absolute_error(y_test, predictions)

        print("ค่าเฉลี่ยของค่าที่ทำนายได้:", predictions_avg)
        print("Mean squared error :", mse)
        print("Root Mean Squared Error :", rmse)
        print("Mean Absolute Error (MAE):", mae)


       
     


    def RearModel(self, speed, tps):
        inj = 'd_inj_pw_rear'
        O2use = 'd_rear_o2'
        tpsPCT = 'd_tps_pct'
        map = 'd_map_v'
        ve = 'd_ve_rear'
        veNew = 'd_new_ve_rear'
        RPM = 'd_eng_speed'

        condition = ((df[RPM] >= 0) & (df[RPM] <= speed) & (df[tpsPCT] <= tps))
        X = df.loc[condition, [tpsPCT,map,RPM,inj,O2use]]
        y = df.loc[condition, [veNew]]

        X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=0)

        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)

        model = keras.Sequential([
        keras.layers.Input(shape=(5,)),
        keras.layers.Dense(32, activation='relu'),
        keras.layers.Dense(32, activation='relu'),
        keras.layers.Dense(64, activation='relu', kernel_regularizer=keras.regularizers.l2(0.01)),
        keras.layers.Dense(1)
                                ])
        model.compile(optimizer='adam', loss=['mean_squared_error'], metrics=['mean_absolute_error'])
        model.fit(X_train, y_train, epochs=1000,
              batch_size=64, validation_split=0.3)

        predictions = model.predict(X_test)
        predictions_avg = np.mean(predictions)

        mse = mean_squared_error(y_test, predictions)
        rmse = np.sqrt(mse)
        mae = mean_absolute_error(y_test, predictions)

        print("ค่าเฉลี่ยของค่าที่ทำนายได้:", predictions_avg)
        print("Mean squared error :", mse)
        print("Root Mean Squared Error :", rmse)
        print("Mean Absolute Error (MAE):", mae)
