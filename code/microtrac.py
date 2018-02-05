"""
Microtrac results of particle size measurements from the fresh and used sand
samples taken from the NREL 2FBR system. Plot figures are saved to the results/
folder in the main repository.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Data Analysis
# ------------------------------------------------------------------------------

# dataframes for fresh sand (fsand) and used sand (usand)
fsand = pd.read_csv('../data/microtrac_fsand.csv', skiprows=[1])
usand = pd.read_csv('../data/microtrac_usand.csv', skiprows=[1])

# diameter area
Da_fresh = fsand['Da']
Da_used = usand['Da']

# feret length
FL_fresh = fsand['FLength']
FL_used = usand['FLength']

# sphericity
Sph_fresh = fsand['Sphericity']
Sph_used = usand['Sphericity']

# char estimate
FL_fresh_max = FL_fresh.max()
FL_fresh_vals = FL_fresh.values
FL_used_vals = FL_used.values
idx_FL_char = np.where(FL_used_vals > FL_fresh_max)[0]
n_FL_char = len(idx_FL_char)

# calculations
Sph_fresh_min = Sph_fresh.min()
Sph_fresh_vals = Sph_fresh.values
Sph_used_vals = Sph_used.values
idx_Sph_char = np.where(Sph_used_vals < Sph_fresh_min)[0]
n_Sph_char = len(idx_Sph_char)

n_fresh = len(FL_fresh)
n_used = len(FL_used)
tot_char = n_FL_char + n_Sph_char
tot_FL = FL_used.count()
print('Number fresh sand particles', n_fresh)
print('Number used sand particles', n_used)
print('Total char particles', tot_char)
print(f'Percent char {tot_char/tot_FL:.3f}%')

# Plot Data
# ------------------------------------------------------------------------------

plt.ion()
plt.close('all')
plt.style.use('ggplot')

plt.figure()
plt.hist(Da_fresh, bins=60, color='C1', label='fresh sand')
plt.hist(Da_used, bins=60, color='C0', alpha=0.8, label='used sand')
plt.xlabel('Da [um]')
plt.ylabel('Number')
plt.legend()
plt.tight_layout()
plt.savefig('../results/micotrac_sand1.pdf', bbox_inches='tight')

f, (ax1, ax2) = plt.subplots(1, 2, sharey=True, sharex=True)
ax1.scatter(FL_fresh, Sph_fresh, color='C1', alpha=0.5)
ax1.set_title('Fresh Sand')
ax1.set_xlabel('Feret Length [um]')
ax1.set_ylabel('Sphericity [-]')
ax2.scatter(FL_used, Sph_used, color='C0', alpha=0.5)
ax2.axvline(FL_fresh.max(), color='black')
ax2.axhline(Sph_fresh.min(), color='black')
ax2.set_title('Used Sand')
ax2.set_xlabel('Feret Length [um]')
plt.tight_layout()
plt.savefig('../results/micotrac_sand2.pdf', bbox_inches='tight')

