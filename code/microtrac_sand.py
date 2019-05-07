"""
Microtrac particle size measurements from the fresh and used sand samples taken
from the NREL 2FBR system. Plot figures are saved to the results/ folder in the
main repository.
"""

import matplotlib.pyplot as plt
import pandas as pd

# Data Analysis
# -----------------------------------------------------------------------------

# dataframes for fresh sand (fsand) and used sand (usand)
fsand = pd.read_csv('../data/microtrac_fsand.csv', skiprows=[1])
usand = pd.read_csv('../data/microtrac_usand.csv', skiprows=[1])

# calculate Sauter mean diameters
ds_fresh = 6 * (fsand['Volume'] / fsand['Surface Area'])
ds_used = 6 * (usand['Volume'] / usand['Surface Area'])

# Print
# -----------------------------------------------------------------------------

print('\nDa (fresh sand)')
print(fsand['Da'].describe())
print('\nDa (used sand)')
print(usand['Da'].describe())

print('\nFeret Length (fresh sand)')
print(fsand['FLength'].describe())
print('\nFeret Length (used sand)')
print(usand['FLength'].describe())

print('\nSauter Diameter (fresh sand)')
print(ds_fresh.describe())
print('\nSauter Diameter (used sand)')
print(ds_used.describe())

print('\nSphericity (fresh sand)')
print(fsand['Sphericity'].describe())
print('\nSphericity (used sand)')
print(usand['Sphericity'].describe())

# Plot
# -----------------------------------------------------------------------------


def _config(ax, xlabel, ylabel):
    ax.grid(color='0.9')
    ax.set_axisbelow(True)
    ax.set_frame_on(False)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.tick_params(color='0.9')


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4.8), tight_layout=True)
ax1.hist(fsand['Da'], bins=60)
ax2.hist(fsand['Da'], bins=60, cumulative=True, density=True)
_config(ax1, 'Da [µm]', 'Number [-]')
_config(ax2, 'Da [µm]', 'Cumulative [-]')
fig.savefig('../results/microtrac_fsand_da.pdf')

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4.8), tight_layout=True)
ax1.hist(fsand['FLength'], bins=60)
ax2.hist(fsand['FLength'], bins=60, cumulative=True, density=True)
_config(ax1, 'Feret Length [µm]', 'Number [-]')
_config(ax2, 'Feret Length [µm]', 'Cumulative [-]')
fig.savefig('../results/microtrac_fsand_df.pdf')

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4.8), tight_layout=True)
ax1.hist(ds_fresh, bins=60)
ax2.hist(ds_fresh, bins=60, cumulative=True, density=True)
_config(ax1, 'Ds [µm]', 'Number [-]')
_config(ax2, 'Ds [µm]', 'Cumulative [-]')
fig.savefig('../results/microtrac_fsand_ds.pdf')

fig, ax = plt.subplots(tight_layout=True)
ax.hist(fsand['Da'], bins=60, label='fresh')
ax.hist(usand['Da'], bins=60, alpha=0.8, label='used')
ax.legend(loc='best')
ax.set_xlim(0, 885)
_config(ax, 'Da [µm]', 'Number [-]')
fig.savefig('../results/microtrac_fsand_usand.pdf')

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4.8), sharey=True, tight_layout=True)
ax1.scatter(fsand['FLength'], fsand['Sphericity'], alpha=0.5, color='C0', linewidths=0)
ax2.scatter(usand['FLength'], usand['Sphericity'], alpha=0.5, color='C1', linewidths=0)
ax1.set_ylim(0.35, 1.0)
_config(ax1, 'Feret Length [µm]', 'Sphericity [-]')
_config(ax2, 'Feret Length [µm]', '')
fig.savefig('../results/microtrac_sph.pdf')

plt.show()
