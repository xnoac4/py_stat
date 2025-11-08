#correlation analysis
from scipy import stats

def check_correlation(x, y):
    return stats.pearsonr(x, y)