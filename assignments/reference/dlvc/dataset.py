
from abc import ABCMeta, abstractmethod
from collections import namedtuple
from enum import Enum

'''
A dataset sample.
  idx: index of the sample in the dataset.
  data: sample data.
  label: target label.
'''
Sample = namedtuple('Sample', ['idx', 'data', 'label'])


class Subset(Enum):
    '''
    Dataset subsets.
    '''

    TRAINING = 1
    VALIDATION = 2
    TEST = 3


class Dataset(metaclass=ABCMeta):
    '''
    Base class of all datasets.
    '''

    @abstractmethod
    def __len__(self) -> int:
        '''
        Returns the number of samples in the dataset.
        '''

        pass

    @abstractmethod
    def __getitem__(self, idx: int) -> Sample:
        '''
        Returns the idx-th sample in the dataset.
        Raises IndexError if the index is out of bounds.
        '''

        pass


class ClassificationDataset(Dataset):
    '''
    Base class of image classification datasets.
    Sample data are numpy arrays of shape rows*cols (grayscale) or rows*cols*channels (color).
    Sample labels are integers from 0 to num_classes() - 1.
    '''

    @abstractmethod
    def num_classes(self) -> int:
        '''
        Returns the number of classes.
        '''

        pass
