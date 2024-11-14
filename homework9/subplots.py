import matplotlib.pyplot as plt
import numpy as np

def horizontal(start,stop,title_1,title_2,x_label="X-Axis",y_label="Y-Axis"):
    x_data = np.linspace(start,stop,10000)
    h = np.cos(x_data)
    k = np.sin(x_data)
    
    fig, ax = plt.subplots(1, 2, figsize=(10,5))
    ax[0].plot(x_data,h,label='h(x)=cos(x)')
    ax[0].set_title(title_1)
    ax[1].set_title(title_2)
    ax[1].plot(x_data,k,label='k(x)=sin(x)')
    
    for i in range(2):
        ax[i].set_xlabel("X-Axis")
        ax[i].set_ylabel("Y-Axis")
        ax[i].legend()

def vertical(start,stop,title_1,title_2,x_label="X-Axis",y_label="Y-Axis"):
    x_data = np.linspace(start,stop,10000)
    h = np.cos(x_data)
    k = np.sin(x_data)
    
    fig, ax = plt.subplots(2, 1, figsize=(5,10))
    ax[0].plot(x_data,h,label='h(x)=cos(x)')
    ax[0].set_title(title_1)
    ax[1].set_title(title_2)
    ax[1].plot(x_data,k,label='k(x)=sin(x)')
    
    for i in range(2):
        ax[i].set_xlabel("X-Axis")
        ax[i].set_ylabel("Y-Axis")
        ax[i].legend()