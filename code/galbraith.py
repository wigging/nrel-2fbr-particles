"""
Galraith results from sample analyses of the NREL 2FBR particles. Plot figures
are saved to the results/ folder in the main repository.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Read data and assign to variables
# ------------------------------------------------------------------------------

df = pd.read_csv('../data/galbraith.csv', index_col='sample')

ash_dry = df['ash_dry[%]']
vm_dry = df['vm_dry[%]']
fc_dry = df['fc_dry[%]']

char_vm_dry = vm_dry[0:7].values
pine_vm_dry = vm_dry[7:14].values
xvals = ['500', '425', '355', '300', '212', '125', 'pan']

char_fc_dry = fc_dry[0:7].values
pine_fc_dry = fc_dry[7:14].values

hoc_dry_pine = df['hoc_dry[btu/lb]'].loc['pine_p355_m425']
lhv_dry_pine = df['lhv_dry[btu/lb]'].loc['pine_p355_m425']
hoc_dry_char = df['hoc_dry[btu/lb]'].loc['char_p355_m425']
lhv_dry_char = df['lhv_dry[btu/lb]'].loc['char_p355_m425']

# Print data
# ------------------------------------------------------------------------------

print('pine_p355_m425')
print('hoc_dry =', hoc_dry_pine, 'BTU/lb')
print('lhv_dry =', lhv_dry_pine, 'BTU/lb')

print('char_p355_m425')
print('hoc_dry =', hoc_dry_char, 'BTU/lb')
print('lhv_dry =', lhv_dry_char, 'BTU/lb')

# Plot data
# ------------------------------------------------------------------------------

plt.ion()
plt.close('all')
plt.style.use('ggplot')

# you can list style colors with the following command
# list(plt.rcParams['axes.prop_cycle'])

char_c = ['#E24A33' for _ in range(7)]
pine_c = ['#8EBA42' for _ in range(7)]
cat_c = ['#988ED5', '#988ED5']
sand_c = ['#FBC15E', '#FBC15E']
sample_c = char_c + pine_c + cat_c + sand_c

plt.figure()
ash_dry.plot(kind='bar', color=sample_c)
plt.xlabel('Sample')
plt.ylabel('Ash [% dry]')
plt.savefig('../results/galbraith_ash.pdf', bbox_inches='tight')

plt.figure()
vm_dry.plot(kind='bar', color=sample_c)
plt.xlabel('Sample')
plt.ylabel('Volatile Matter [% dry]')
plt.savefig('../results/galbraith_vm.pdf', bbox_inches='tight')

plt.figure()
fc_dry.plot(kind='bar', color=sample_c)
plt.xlabel('Sample')
plt.ylabel('Fixed Carbon [% dry]')
plt.savefig('../results/galbraith_fc.pdf', bbox_inches='tight')

plt.figure()
plt.plot(char_vm_dry, label='char')
plt.plot(pine_vm_dry, c='#8EBA42', label='pine')
plt.xticks([0, 1, 2, 3, 4, 5, 6], xvals)
plt.xlabel('Sieve Size [um]')
plt.ylabel('Volatile Matter [% dry]')
plt.legend(loc='best')
plt.savefig('../results/galbraith_vm_compare.pdf', bbox_inches='tight')

plt.figure()
plt.plot(char_fc_dry, label='char')
plt.plot(pine_fc_dry, c='#8EBA42', label='pine')
plt.xticks([0, 1, 2, 3, 4, 5, 6], xvals)
plt.xlabel('Sieve Size [um]')
plt.ylabel('Fixed Carbon [% dry]')
plt.legend(loc='best')

