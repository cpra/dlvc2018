
import numpy as np

from typing import List, Callable

# All operations are functions that take and return numpy arrays
# See https://docs.python.org/3/library/typing.html#typing.Callable for what this line means
Op = Callable[[np.ndarray], np.ndarray]

def chain(ops: List[Op]) -> Op:
    '''
    Chain a list of operations together.
    '''

    def op(sample: np.ndarray) -> np.ndarray:
        for op_ in ops:
            sample = op_(sample)
        return sample

    return op

def type_cast(dtype: np.dtype) -> Op:
    '''
    Cast numpy arrays to the given type.
    '''

    # TODO implement (see above for guidance).

    pass

def vectorize() -> Op:
    '''
    Vectorize numpy arrays via "numpy.ravel()".
    '''

    # TODO implement (see above for guidance).

    pass

def hwc2chw() -> Op:
    '''
    Flip a 3D array with shape HWC to shape CHW.
    '''

    # TODO implement (see np.transpose)

    pass

def chw2hwc() -> Op:
    '''
    Flip a 3D array with shape CHW to HWC.
    '''

    # TODO implement (see np.transpose)

    pass

def add(val: float) -> Op:
    '''
    Add a scalar value to all array elements.
    '''

    # TODO implement

    pass

def mul(val: float) -> Op:
    '''
    Multiply all array elements by the given scalar.
    '''

    # TODO implement

    pass

def hflip() -> Op:
    '''
    Flip arrays with shape HWC horizontally with a probability of 0.5.
    '''

    # TODO implement (numpy.flip will be helpful)

    pass

def rcrop(sz: int, pad: int, pad_mode: str) -> Op:
    '''
    Extract a square random crop of size sz from arrays with shape HWC.
    If pad is > 0, the array is first padded by pad pixels along the top, left, bottom, and right.
    How padding is done is governed by pad_mode, which should work exactly as the 'mode' argument of numpy.pad.
    Raises ValueError if sz exceeds the array width/height after padding.
    '''

    # TODO implement
    # https://docs.scipy.org/doc/numpy-1.15.1/reference/generated/numpy.pad.html will be helpful

    pass
