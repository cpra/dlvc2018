
# Deep Learning for Visual Computing - Assignment 2

The second assignment covers iterative optimization and parametric (deep) models for image classification.

## Part 1

This part is about implementing and experimenting with different flavors of gradient descent.

Download the data from [here](https://github.com/cpra/dlvc2018/tree/master/assignments/assignment2). Your task is to implement `gradient_descent_2d.py`. See the code comments for instructions. The `fn/` folder contains sampled 2D functions for use with that script. You can add more functions if you want, [here](https://www.sfu.ca/~ssurjano/optimization.html) is a list of interesting candidates.

The goal of this part is for you to understand gradient descent better by playing around with it. Try different parameters, starting points, and functions. This nicely highlights the function and limitations of gradient descent, which we've already covered in the lecture.

## Part 2

Time for some Deep Learning. We already implemented most of the required functionality during Assignment 1. The main thing that's missing is a subtype of `Model` that wraps a PyTorch CNN classifier. Implement this type, which is defined inside `dlvc/models/pytorch.py` and named `CnnClassifier`. Details are stated in the code comments. The PyTorch documentation of `nn.Module`, which is the base class of PyTorch models, is available [here](https://pytorch.org/docs/stable/nn.html#containers).

PyTorch (and other libraries) expects the channel dimension of a single sample to be the first one, rows the second one, and columns the third one (`CHW` for short). However in our case they are `HWC`. To address this, implement the `hwc2chw()` function in `ops.py` (`git pull` the reference code if that function is missing) and its inverse `chw2hwc()`. In the same file you will also find two more new function definitions, `add()` and `mul()`. Implement those as well. We will use these for basic input normalization.

Once this is in place, create a script named `cnn_cats_dogs.py`. This file will be very similar to the knn version developed for Assignment 1 so you might want to use that one as a reference. This file should implement the following in the given order:

1. Load the training and validation subsets of the `PetsDataset`
2. Initialize `BatchGenerator`s for both with batch sizes of 128 or so (feel free to experiment) and the input transformations required for the CNN. This should include input normalization. A basic option is `ops.add(-127.5), ops.mul(1/127.5)` but for bonus points you can also experiment with more sophisticated alternatives such as per-channel normalization using statistics from the training set (if so create corresponding operations in `ops.py` and document your findings in the report).
3. Define a PyTorch CNN with an architecture suitable for cat/dog classification. To do so create a subtype of `nn.Module` and overwrite the `__init__()` and `forward()` methods (do this inside `cnn_cats_dogs.py`). If you use our servers, you *must run  these models on the GPUs*. To do so, call the `.cuda()` method of the CNN object. See below for additional remarks.
4. Wrap the CNN object `net` in a `CnnClassifier`, `clf = CnnClassifier(net, ...)`.
5. Inside a `for epoch in range(1, 101):` loop (i.e. train for 100 epochs which is sufficient for now), train `clf` on the training set and store the losses returned by `clf.train()` in a list. Then convert this list to a numpy array and print the mean loss. Then print the accuracy on the validation set using the `Accuracy` class developed in Assignment 1.

The console output should thus be similar to the following (ignoring the values):

    epoch 1
     train loss: 0.689 +- 0.006
     val acc: accuracy: 0.561
    epoch 2
     train loss: 0.681 +- 0.008
     val acc: accuracy: 0.578
    epoch 3
     train loss: 0.673 +- 0.009
     val acc: accuracy: 0.585
    epoch 4
     train loss: 0.665 +- 0.013
     val acc: accuracy: 0.594
    epoch 5
     train loss: 0.658 +- 0.014
     val acc: accuracy: 0.606
    ...

The goal of this part is for you to get familiar with PyTorch and to be able to try out different architectures and layer combinations. The pets dataset is ideal for this purpose because it is small; on our servers 100 epochs should take less than five minutes even with rather complex architectures. Validation accuracy is not critical though, so experiment manually by editing the code rather than automatically via hyperparameter optimization. What you will find is that the training loss will approach 0 even with simple architectures (demonstrating how powerful CNNs are and how well SGD works with them) while the validation accuracy will likely not exceed 75%. The latter is due to the small dataset size, resulting in overfitting. We will address this in the next part.

You will likely find that training is too slow on your computer unless you have an Nvidia GPU with CUDA support. If so, copy the code into your home directory on the DLVC server and run it there. **Detailed instructions will follow as soon as some remaining issues with the server are resolved (sorry).**
