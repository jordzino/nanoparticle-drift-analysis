Nanoparticle Drift Analysis (Python + MATLAB)

This project simulates 3D Brownian motion with directional drift using Python and applies numerical drift correction using MATLAB. It formed part of my undergraduate engineering dissertation and demonstrates an end-to-end scientific workflow involving simulation, data analysis, and velocity estimation. These scripts were used to validate a larger MATLAB-based optical imaging system.

Context:

This project was originally developed as part of my final-year dissertation in Electrical and Electronic Engineering. It focuses on simulating nanoparticle movement using Brownian motion models with directional drift and correcting that drift numerically using MATLAB.

At the time, the full workflow was tested and validated using MATLAB 2023a and Python.

Please Note: I no longer have access to MATLAB, so I’m unable to tweak or test the `drift_correction.m` script or change the input file paths. The script may require slight updates to filenames or data formatting. However, the logic and structure were validated during the dissertation and remain useful for reference and future adaptation.


Overview of Files:

SND1.py - Python script that simulates 3D Brownian motion with known drift, including visualisation and CSV export. SND stands for 'Simulated Nanoparticles with Drift'.
drift_correction.m.txt - MATLAB script that estimates and removes drift from the simulated particle trajectories (The MATLAB script is included as drift_correction.m.txt due to system limitations. It should be renamed to .m when used in MATLAB).
nanoparticle_positionsNP101d.csv - Example dataset that can be used for testing
README.md


How to Use:

Python Simulation:

1. Install Python dependencies:
   ```bash
   pip install numpy pandas matplotlib

2. Run the Python simulation (can be edited in IDLE):
	python SND1.py

3. Output:
	- nanoparticle_positions.csv: a synthetic dataset with directional drift
	- plot of the particle trajectory

MATLAB Drift Correction:

Note: MATLAB is required for this part, but I no longer have access to it.
The script was last tested in MATLAB 2023a, and should work after adjusting the input filename to match your .csv file (e.g. NP3Ca.csv or nanoparticle_positions.csv).

1. Open drift_correction.m in MATLAB

2. Update this line to reflect your input filename:
	opts = detectImportOptions('your_csv_filename.csv');

3. Run the script in MATLAB

4. Output:
	- estimated_drift.csv: contains estimated X, Y, Z drift velocity and their variance

