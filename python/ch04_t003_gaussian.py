# generate some data
import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(-3, 3, 111)

sigma = .73

# one gaussian
a = 1 / (sigma * np.sqrt(2 * np.pi))
eTerm = -x ** 2 / (2 * sigma ** 2)
gaus = a * np.exp(eTerm)

plt.plot(x, gaus, 'k', linewidth=2)
plt.xlim(x[[0, -1]])
plt.xlabel('Numerical value')
plt.ylabel('Probability')
plt.title('Gaussian probability density', loc='center')

plt.tight_layout()
plt.savefig('desc_analytic_gaussian.png')
