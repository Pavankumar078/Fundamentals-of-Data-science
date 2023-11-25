from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import numpy.random as random

# Scatterplot and Correlations
# Data
x = random.randn(100)
y1 = x * 5 + 9
y2 = -5 * x
y3 = random.randn(100)

# Plot
plt.rcParams.update({'figure.figsize': (10, 8), 'figure.dpi': 100})
plt.scatter(x, y1, label='y1 Correlation: {:.2f}'.format(np.corrcoef(x, y1)[0, 1]))
plt.scatter(x, y2, label='y2 Correlation: {:.2f}'.format(np.corrcoef(x, y2)[0, 1]))
plt.scatter(x, y3, label='y3 Correlation: {:.2f}'.format(np.corrcoef(x, y3)[0, 1]))

# Plot settings
plt.title('Scatterplot and Correlations')
plt.legend()
plt.show()
