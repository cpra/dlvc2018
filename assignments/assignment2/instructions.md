
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

You will likely find that training is too slow on your computer unless you have an Nvidia GPU with CUDA support. If so, copy the code into your home directory on the DLVC server and run it there. See [here](https://github.com/cpra/dlvc2018/blob/master/assignments/server.md) for details.

## Part 3

Address the overfitting issue of part 2 using a combination of the techniques we covered in the lecture, namely data augmentation, regularization, early stopping, and transfer learning. To get all points you are expected to utilize at least the first three:

* Data augmentation: implement (and use) at least random crops and left/right mirroring. The corresponding operations are already defined in `ops.py`. For bonus points you can try additional augmentation methods.
* Regularization: use at least weight decay but you can also experiment with dropout (in addition to or instead of weight decay).
* For early stopping you can simply [save](https://pytorch.org/tutorials/beginner/saving_loading_models.html#saving-loading-model-for-inference) the current model to disk to something like `best_model.pth` if it has the highest validation performance seen so far (and overwrite that file in the process of training).

In the report you should discuss how the individual techniques affected your training and validation set performance. Don't just compare part 2 and part 3 results, also compare at least a few combinations and settings like only regularization but no data augmentation vs. both, different regularization strengths and so on. I realize this can be a bit of a pain depending on the server load but only by experimenting you will gain a better understanding of which effect these techniques have. Try a couple combinations (like maybe 5) but please don't overdo it if our servers are loaded to give others a chance to finish their assignments.

Submit the configuration that lead to the best validation performance as a file `cnn_cats_dogs_pt3.py`. This file should be based on `cnn_cats_dogs.py` from part 2, i.e. it should train the CNN and output the training and validation performance in every epoch.

You must also submit the corresponding model you obtained (`best_model.pth`). I will run your model on my own secret test set and rank all submissions accordingly. The five best submissions will get bonus points and the winners get a chance to briefly explain their method in an upcoming lecture (optional).

For bonus points you can additionally experiment with transfer learning (likely required if you want to win the competition). PyTorch makes [loading pre-trained models](https://pytorch.org/docs/stable/torchvision/models.html) easy. For easy integration into the existing code you will want to replace the classification layers, freeze all other parameters (there are several ways to do this, see e.g. [here](https://discuss.pytorch.org/t/how-to-perform-finetuning-in-pytorch/419/10)) and then simply wrap the net inside `CnnClassifier`. This way you can reuse all code as you did in part 2.

## Report

Write a short report (2 to 3 pages) that answers the following questions:

* How does SGD work? What are your findings on the example data (part1)?
* Which network architecture did you choose for part 2 and why? Did you have problems reaching a low training error?
* What are the goals of data augmentation, regularization, and early stopping? How exactly did you use these techniques (hyperparameters, combinations) and what were your results (train and val performance)? List all experiments and results, even if they did not work well, and discuss them.
* If you utilized transfer learning, explain what you did and your results.

## Submission

Submit your assignment until **06.01 at 11pm**. To do so, create a zip archive including the report, the complete `dlvc` folder with your implementation and all scripts. More precisely, after extracting the archive I should obtain the following:

    group_x/
        report.pdf
        gradient_descent_2d.py
        cnn_cats_dogs.py
        cnn_cats_dogs_pt3.py
        dlvc/
            ...

Then upload that archive to the submission folder (`assignment2`) on the DLVC server. You will find this folder inside your group folder in your home directory. Make sure you've read the general assignment information [here](https://github.com/cpra/dlvc2018/blob/master/assignments/general.md) before your final submission.
