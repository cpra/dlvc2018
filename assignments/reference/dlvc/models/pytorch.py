
from ..model import Model

import numpy as np
import torch.nn as nn

class CnnClassifier(Model):
    '''
    Wrapper around a PyTorch CNN for classification.
    The network must expect inputs of shape NCHW with N being a variable batch size,
    C being the number of (image) channels, H being the (image) height, and W being the (image) width.
    The network must end with a linear layer with num_classes units (no softmax).
    The cross-entropy loss and SGD are used for training.
    '''

    def __init__(self, net: nn.Module, input_shape: int, num_classes: int, lr: float, wd: float):
        '''
        Ctor.
        net is the cnn to wrap. see above comments for requirements.
        input_shape is the expected input shape, i.e. (0,C,H,W).
        num_classes is the number of classes (> 0).
        lr: learning rate to use for training (sgd with Nesterov momentum of 0.9).
        wd: weight decay to use for training.
        '''

        # TODO implement

        # inside the train() and predict() functions you will need to know whether the network itself
        # runs on the cpu or on a gpu, and in the latter case transfer input/output tensors via cuda() and cpu().
        # do termine this, check the type of (one of the) parameters, which can be obtained via parameters() (there is an is_cuda flag).
        # you will want to initialize the optimizer and loss function here. note that pytorch's cross-entropy loss includes normalization so no softmax is required

        pass

    def input_shape(self) -> tuple:
        '''
        Returns the expected input shape as a tuple.
        '''

        # TODO implement

        pass

    def output_shape(self) -> tuple:
        '''
        Returns the shape of predictions for a single sample as a tuple, which is (num_classes,).
        '''

        # TODO implement

        pass

    def train(self, data: np.ndarray, labels: np.ndarray) -> float:
        '''
        Train the model on batch of data.
        Data has shape (m,C,H,W) and type np.float32 (m is arbitrary).
        Labels has shape (m,) and integral values between 0 and num_classes - 1.
        Returns the training loss.
        Raises TypeError on invalid argument types.
        Raises ValueError on invalid argument values.
        Raises RuntimeError on other errors.
        '''

        # TODO implement
        # make sure to set the network to train() mode
        # see above comments on cpu/gpu

        pass

    def predict(self, data: np.ndarray) -> np.ndarray:
        '''
        Predict softmax class scores from input data.
        Data has shape (m,C,H,W) and type np.float32 (m is arbitrary).
        The scores are an array with shape (n, output_shape()).
        Raises TypeError on invalid argument types.
        Raises ValueError on invalid argument values.
        Raises RuntimeError on other errors.
        '''

        # TODO implement

        # pass the network's predictions through a nn.Softmax layer to obtain softmax class scores
        # make sure to set the network to eval() mode
        # see above comments on cpu/gpu

        pass
