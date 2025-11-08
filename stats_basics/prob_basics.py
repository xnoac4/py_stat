#basics of probability
from scipy import stats

def binomal_probability(n, k, p):
    return stats.binom.pmf(k, n, p)
