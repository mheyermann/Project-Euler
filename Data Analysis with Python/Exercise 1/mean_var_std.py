import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError('List must contain nine numbers.')
    else:
        narray = np.array(list).reshape((3,3))
        narray_mean = [np.mean(narray, axis = 0).tolist(), np.mean(narray, axis = 1).tolist(), np.mean(narray)]
        narray_var = [np.var(narray, axis = 0).tolist(), np.var(narray, axis = 1).tolist(), np.var(narray)]
        narray_std = [np.std(narray, axis = 0).tolist(), np.std(narray, axis = 1).tolist(), np.std(narray)]
        narray_max = [np.max(narray, axis = 0).tolist(), np.max(narray, axis = 1).tolist(), np.max(narray)]
        narray_min = [np.min(narray, axis = 0).tolist(), np.min(narray, axis = 1).tolist(), np.min(narray)]
        narray_sum = [np.sum(narray, axis = 0).tolist(), np.sum(narray, axis = 1).tolist(), np.sum(narray)]

        calculations = {'mean': narray_mean, 'variance': narray_var, 'standard deviation': narray_std, 'max': narray_max, 'min': narray_min, 'sum': narray_sum}

    return calculations