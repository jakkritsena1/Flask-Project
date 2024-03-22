import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class report: 
    
    def plot_3d_surface(self,predict):
        dataset = pd.read_csv("C:\\Users\\Ball.sna\\source\\repos\\jakkritsena1\\Flask-Project\\dataset\\dataset.csv")
        tpsPCT = 'd_tps_pct'
        RPM = 'd_eng_speed'

        x = dataset.loc[[RPM]]
        y = dataset.loc[[tpsPCT]]
    
        x, y = np.meshgrid(x, y)
        z = predict

        data = {'X': x.flatten(), 'Y': y.flatten(), 'Z': z.flatten()}
        df = pd.DataFrame(data)

        fig = plt.figure(figsize=(12, 6))
        ax1 = fig.add_subplot(121, projection='3d')
        ax1.plot_surface(x, y, z, cmap='viridis')
        ax1.set_xlabel('X')
        ax1.set_ylabel('Y')
        ax1.set_zlabel('Z')
        ax1.set_title('Surface 3D Plot')

        ax2 = fig.add_subplot(122)
        scatter = ax2.scatter(df['X'], df['Y'], c=df['Z'], cmap='viridis')
        ax2.set_xlabel('X')
        ax2.set_ylabel('Y')
        ax2.set_title('Table with Color Coded Height')
        fig.colorbar(scatter, ax=ax2, label='Z (Color by Height)')

        plt.tight_layout()
        plt.show()


r = report()
r.plot_3d_surface(1500,80) 
