
import numpy as np

import types

def chain(ops: list) -> types.FunctionType:
    '''
    Chain a list of operations together.
    '''

    def op(sample: np.ndarray) -> np.ndarray:
        for op_ in ops:
            sample = op_(sample)
        return sample

    return op

def type_cast(dtype: np.dtype) -> types.FunctionType:
    '''
    Cast numpy arrays to the given type.
    '''

    # TODO implement (see above for guidance).

def vectorize() -> types.FunctionType:
    '''
    Vectorize numpy arrays via "numpy.ravel()".
    '''

    # TODO implement (see above for guidance).
