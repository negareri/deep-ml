# --- cell 1 ---
import numpy as np
from sklearn.decomposition import PCA

class MyReducer:

    def __init__(self):
        self.n_components = 10
        self.reducer = PCA(
            n_components=10,
            svd_solver="full",
            whiten=True
        )

    def fit(self, X):
        self.reducer.fit(X)
        return self

    def transform(self, X):
        return self.reducer.transform(X)

    def fit_transform(self, X):
        return self.fit(X).transform(X)