import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameters for the simulation
n = 1000  # Number of timesteps
d = 3  # Dimensions of BM
T = 1.0  # Total observation time; units s
D = 1.5e-4  # Diffusion coefficient (source 9); units microm^2 per ms
sigma = (2 * D * T * 1000) ** 0.5  # Variance of the random displacements between each time step; units microm
times = np.linspace(0., T, n)  # Creates equal time intervals for n time steps over a total observation time of T secs; units ms
dBM = np.random.normal(scale=sigma, size=(n-1, d))  # Generates an array of random BM increments, chosen from a normal distribution with a mean of 0 and variance sigma; units microm
BM0 = np.zeros(shape=(1, d))  # Creates an empty array for BM at time 0 to be written over with a BM trajectory for each d
BM = np.concatenate((BM0, np.cumsum(dBM, axis=0)), axis=0)  # Creates BM trajectories by cumulatively summing the dBM increments over all time steps for each value of d

# Add known drift
drift_velocity = np.array([0.1, 0.2, 0.3])  # Known drift in microm/step
drift = np.outer(np.arange(n), drift_velocity)
BM_with_drift = BM + drift

# Add frame numbers and particle IDs (assuming one particle with ID 1)
frame_numbers = np.arange(1, n + 1).reshape(-1, 1)
particle_ids = np.ones((n, 1))
data_with_ids_frames = np.hstack((particle_ids, frame_numbers, BM_with_drift))

# Save to CSV file
np.savetxt('nanoparticle_positions.csv', data_with_ids_frames, delimiter=',', header='ParticleID,FrameNumber,X,Y,Z', comments='')

# Plotting the trajectory
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(BM_with_drift[:, 0], BM_with_drift[:, 1], BM_with_drift[:, 2])
plt.xlabel('X displacement (µm)')
plt.ylabel('Y displacement (µm)')
ax.set_zlabel('Z displacement (µm)')
plt.title('3D Brownian Motion with Drift')
plt.show()
