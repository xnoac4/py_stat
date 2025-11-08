#statistics description
import numpy as np
from scipy import stats

def analyze_dataset(data):
    return {
        'mean': np.mean(data),
        'median': np.median(data),
        'std': np.std(data),
        'skewness': stats.skew(data)
    }

