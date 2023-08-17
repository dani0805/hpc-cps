"""
The dataset in this example is the UCI ML hand-written digits dataset. This dataset is a set of 8x8 images of digits,
where each image is represented as an array of 64 integers (the grayscale values of the pixels), and the target is the
digit that the image represents (from 0 to 9). The task is a multi-class classification problem: the model has to
predict which digit the image represents.

We are using a Support Vector Classifier (SVC) model from scikit-learn. Support Vector Machines (SVM) are powerful
models that work well on a variety of datasets, and are especially suited for problems where the classes are not
linearly separable.

The parameters we're tuning with the grid search are:

- C: The regularization parameter. This parameter controls the trade-off between achieving a low error on the training
  data and minimizing the complexity of the model (to avoid overfitting). A low value for C will prioritize simplicity
  (leading to underfitting), while a high value will prioritize minimizing the training error (which may lead to
  overfitting).

- gamma: This parameter defines how far the influence of a single training example reaches. Low values mean 'far'
  and high values mean 'close'. This can be seen as the inverse of the radius of influence of samples selected by the
  model as support vectors.
- kernel: The kernel type to be used in the algorithm. It must be one of 'linear', 'poly', 'rbf', 'sigmoid',
  'precomputed' or a callable. If none is given, 'rbf' will be used. Here, we are exploring 'rbf', 'poly', and 'sigmoid'.
  The GridSearchCV function performs an exhaustive search over the specified parameter values for the estimator
  (in this case, the SVC model). The parameters of the estimator used to apply these methods are optimized by
  cross-validated grid-search over a parameter grid (in this case, all the combinations of the C, gamma,
  and kernel parameters).


"""


from dask.distributed import Client
from sklearn.datasets import load_digits
from sklearn.svm import SVC
from dask_ml.model_selection import GridSearchCV

# Create Dask client
client = Client("tcp://localhost:8786")

# Load sample data
digits = load_digits()

# Define hyperparameters grid
param_grid = {"C": [0.1, 1, 10, 100],
              "gamma": [1, 0.1, 0.01, 0.001],
              "kernel": ['rbf', 'poly', 'sigmoid']}

# Define model
model = SVC()

# Define grid search
grid_search = GridSearchCV(model, param_grid, cv=3, n_jobs=-1)

# Run grid search
grid_search.fit(digits.data, digits.target)

# Print best parameters
print("Best parameters found: ", grid_search.best_params_)
