
# Deep Learning for Visual Computing - Assignment 1

The first assignment allows you to become familiar with basic dataset handling, image processing, and machine learning.

As this is a new course, this text or the reference code might not be without errors. If you find a significant error (not just typos but errors that affect the assignment), please contact us via [email](mailto:dlvc@cvl.tuwien.ac.at). Students who find and report such errors will get extra points.

## Part 0

This part is about setting up the environment for developing. 

All assignments will be implemented in Python 3 and [PyTorch](https://pytorch.org/). So first make sure Python 3.5 or newer is installed on your computer as that's the minimal requirement of the most recent PyTorch version. If not, [download](https://www.python.org/downloads/) and install a recent version.

Then setup, create, and enable a [virtualenv](https://virtualenv.pypa.io/en/stable/userguide/#usage). This facilitates package installation and ensures that these packages don't interfere with other Python code you might already have. Once done, make sure `$ python --version` returns something like `python 3.7.0`. Finally, install the core packages we'll need:

    pip install numpy opencv-python

The PyTorch setup varies a bit depending on the OS, see [here](https://pytorch.org/). Use a version with CUDA only if you have an Nvidia GPU. In any case, ensure to install the current version of PyTorch, which is 0.4.1. This is the version I'll use for testing all assignments and if they fail due to version issues, you'll get significant point deductions. Confirm this via:

    python -c "import torch; print(torch.__version__)"

## Part 1

Download the reference code from [here](https://github.com/cpra/dlvc2018/tree/master/assignments/reference), making sure that the file structure is preserved, and rename the root folder to something other than `reference`. Read the code and make sure that you understand what the individual classes and methods are doing.

[Download](https://www.cs.toronto.edu/~kriz/cifar.html) and extract the *Python* version of the CIFAR10 dataset somewhere *outside* the code folder. Read the website to understand which classes there are and how the data are structured and read.

Then implement the `PetsDataset` (`datasets/pets.py`). Make sure to follow the instructions in the code exactly. Make sure the following applies. If not, you made a mistake somewhere:

* Number of samples in the individual datasets: 7959 (training), 2041 (validation), 2000 (test).
* Total number of cat and dog samples: 6000 per class
* Image shape: always `(32, 32, 3)`, image type: always `np.uint8`
* Labels of first 10 training samples: `0 0 0 0 1 0 0 0 0 1`
* Make sure that the color channels are in BGR order (not RGB) by displaying the images and verifying the colors are correct (`cv2.imshow`, `cv2.imwrite`).

Do not change any other files and do not create additional files.

## Part 2

Make sure you have the most recent [reference code](https://github.com/cpra/dlvc2018/tree/master/assignments/reference). If not, follow the procedure described in the first paragraph of Part 1.

In this part we will implement common functionality for classifier training. As we'll see in the lecture, training and testing is almost always done in mini-batches, with each being a small part of the whole data. The knn classifier we've covered so far is an exception but we'll already implement this functionality anyways as we'll need it later. To do so, finish the `BatchGenerator` class in `batches.py`. Make sure to read the comments and implement type and value checks accordingly.

The `BatchGenerator`'s constructor has as optional `op` argument that is a function. If this argument is given, the generator will apply this function to the data of every sample before adding it to a batch. This is a flexible mechanism that will later allow us to implement data augmentation. For now we'll use it to transform the data to the form expected by the knn classifier (see `knn.py`). For this we need to convert the images to float vectors, as covered in the lecture. To do so, implement the `type_cast` and `vectorize` functions inside `ops.py`. These are functions that return other functions. See the `chain` function, which is already implemented for reference. That function allows for chaining other operations together like so:

```python
op = ops.chain([
    ops.vectorize(),
    ops.type_cast(np.float32)
])
```

We can then use the batch generator with a batch size equal to the number of samples in the dataset (subset) to obtain data that is compatible with the classifier (and other classifiers that operate on feature vectors). Make sure the following applies:

* The number of training batches is `1` if the batch size is set to the number of samples in the dataset
* The number of training batches is `16` if the batch size is set to 500
* The data and label shapes are `(500, 3072)` and `(500,)`, respectively, unless for the last batch
* The data type is always `np.float32` and the label type is integral (one of the `np.int` and `np.uint` variants)
* The first sample of the first training batch returned *without shuffling* has label `0` and data `[116. 125. 125. 91. 101. ...]`.
* The first sample of the first training batch returned *with shuffling* must always the different.

Finally, implement the `KnnClassifier` in `knn.py`. Training is as simple as storing the training samples and labels. See the lecture slides for how to implement the prediction of softmax class scores ("probabilities"). You can use the L1 or L2 distance (the L1 distance should work a bit better). You are *not* allowed to use third-party machine learning libraries in your implementation.

## Part 3

We will use the accuracy as the performance measure for the knn classifier (and other classifiers in the future). See the lecture slides for how this measure is defined and implement the `Accuracy` class in `test.py` accordingly. This class supports batch-wise updates which will be handy in the future (we already talked about minibatches in the lecture).

Finally, combine the functionality implemented so far in a script `knn_cats_dogs.py` that does the following, in this order:

1. Load the training, validation, and test sets as individual `PetsDataset`s.
2. Create a `BatchGenerator` for each one with a minibatch size equal to the number of dataset samples.
3. Implement random or grid search (your choice) for finding a good value for `k`, assuming `0 k <= 100`. Test at least 5 values. This is not a lot but testing a single `k` will probably take a long time.
4. For each `k` to test, "train" a `KnnClassifier` and then calculate the accuracy on the validation set.
5. Report the best `k` found and the corresponding validation accuracy.
6. Compute and report the accuracy on the test set with that `k`

Steps 3 to 6 must be implemented in a generic way using a loop, like so:

```python
for k in range(1, 101, 10):  # grid search example
    knn = KnnClassifier(k, ...)
    accuracy = Accuracy()
    # train and compute validation accuracy ...
    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_k = k

knn = KnnClassifier(best_k, ...)
# compute test accuracy
```

## Report

Write a short report (1 to 2 pages) that answers the following questions:

* What is image classification?
* What is the purpose of the training, validation, and test sets and why do we need all of them?
* How do knn classifiers work?

Also include your results obtained from `knn_cats_dogs.py`. Include the validation accuracies for the different `k` you considered as a table or (better) a plot. Also include the final test accuracy, compare the best validation accuracy and the final test accuracy, and discuss the results.

## Submission

Submit your assignment until **11.11 at 11pm**. To do so, create a zip archive including the report, the complete `dlvc` folder with your implementations as well as `knn_cats_dogs.py`. More precisely, after extracting the archive I should obtain the following:

    group_x/
        report.pdf
        knn_cats_dogs.py
        dlvc/
            batches.py
            ...
            datasets/
                ...
            ...

Then upload that archive to the submission folder (`assignment1`) on the DLVC server. You will find this folder inside your group folder in your home directory. Make sure you've read the general assignment information [here](https://github.com/cpra/dlvc2018/blob/master/assignments/general.md) before your final submission.
