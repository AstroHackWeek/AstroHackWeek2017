# Machine learning

## Introduction

I think of machine learning as a set of algorithms and implementations that make
data-driven predictions or decisions. This is why machine learning has become
all the buzz in industry, but isn't always applicable in scientific studies;
we're often interested in making some inference about a parameter after
marginalizing over nuisance parameters so we can learn some thing about
"physics." (We're usually not trying to serve ads to teenagers.) Another reason
that machine learning algorithms are not obviously applicable to science is that
the rarely incorporate observational uncertainties in a justifiable way. More on
that later...

The typical problems for which you might consider using machine learning methods
can be grouped into four main types of problems:

* **Supervised** methods:
    * *Classification*: For example, we have photometry for 100,000 sources from
      some imaging survey and want to know which ones are galaxies, stars,
      quasars.
    * *Regression*: We want to learn the parameters of some model, usually to
      make good predictions.
* **Unsupervised** methods:
    * *Dimensionality reduction*: We have spectra for 100,000 galaxies and want
      to decompose the spectra into common spectral templates (eigenspectra).
    * *Clustering*: We have colors, sizes, and shapes for 100,000 galaxies and
      want to know if there are sub-populations with similar characteristics.
    * *Density estimation*: We want to know the relative abundance of blue vs.
      red galaxies given photometry.

With supervised methods, our data are a set of "features" and some known
"labels" for (a subset of) the data. That is, for a subset of the data, we know
the true classes or true values. In the first example above, the photometry or
colors are the features and the label can be "galaxy", "star", or "quasar". In
the case of regression, the labels can be continuous.

With unsupervised methods, are data are only the "features."

For all of the above, there are many, many algorithms and options within the
options. Often, there is no definitive answer or easy way to determine what
algorithm will perform best for your use case. It generally takes a lot of trial
and error, and help from experts! In some cases, you get the best performance
from using *many algorithms simultaneously* and combining the predictions /
results (see: Netflix prize).

Luckily, most of the relevant algorithms are implemented in the Python package
`scikit-learn` and have a common interface for interacting with them. This makes
it fairly easy to write code that is "learning algorithm agnostic," meaning you
can swap in and out different methods.

## Supervised methods

### Classification

The goal of a classification problem is to train a model that will successfully
predict the classes of new objects that I feed in to the model. Let's stick with
the idea of classifying photometric objects as an example. Imagine we have a
huge database of photometry for astronomical objects, and for some subset of
that database I've gone through by hand and classified the data into two
classes: "star" and "galaxy." I don't want to have to go through the whole
dataset and label all of the targets, instead I want to train the computer to
learn the best way to discriminate these classes based on the smaller *training
set* of data that I provide.

A generic problem for any machine learning application is: How do we decide on
the model? As mentioned above, that often comes from a mixture of "physical
intuition," trial and error, and computational cost. You first have to decide on
an algorithm. To do that, you have to think about what accuracy you want, how
flexible / nonlinear the model can be (e.g., number of parameters), how much
time and data it will take to train the model. Once we choose an algorithm, we
then need to figure out a way to determine a "score" for a given choice of
parameters. Lastly, we need to decide on how we're going to optimize over the
model parameters.

A few relevant tools / algorithms:
* K nearest neighbors (KNN)
* Support vector machines (SVM)
* Decision trees / random forest (RF)
* Neural networks

### Regression

Similar to classification, we want to train a model to predict some quantity or
quantities given some set of "features." However, here the predicted quantity
is typically a continuous variable instead of a discrete class.

A few relevant tools / algorithms:
* Least-squares regression
* Ridge regression

## Unsupervised methods

### Dimensionality reduction

The goal of dimensionality reducton algorithms is to compress the data by
finding a representation of the data that preserves "information" (or some other
metric) with fewer dimensions.

A few relevant tools / algorithms:
* Principle components analysis (PCA)
* Independent components analysis (ICA)
* Locally linear embedding (LLE)
* t-Distributed Stochastic Neighbor Embedding (t-SNE)

### Clustering

A few relevant tools / algorithms:
* K-means
* Gaussian mixture models (GMM)

### Density estimation

A few relevant tools / algorithms:
* Kernel density estimation (KDE)
* Gaussian mixture models (GMM)
