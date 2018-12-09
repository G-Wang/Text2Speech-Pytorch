from nnmnkwii.datasets import FileSourceDataset, FileDataSource
import numpy as np

def _pad(seq, max_len, constant_values=0):
    return np.pad(seq, (0, max_len - len(seq)),
                  mode='constant', constant_values=constant_values)

