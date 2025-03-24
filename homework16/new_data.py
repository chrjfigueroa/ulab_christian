import torch
import numpy as np

x_data = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
y_data = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
X, Y = np.meshgrid(x_data, y_data)

pattern = np.arctan(X) + Y

N, D_in, H, D_out = 1000, 2, 50, 1

#Input data
x = torch.randn(N, D_in) * 3.1415
y = (x[:, 0].arctan() + x[:, 1]).unsqueeze(1)

noise = torch.randn(N, D_out) * 0.1
y += noise

x_values = x.numpy()[:, 0]
y_values = x.numpy()[:, 1]
color_values = y.numpy().flatten()
