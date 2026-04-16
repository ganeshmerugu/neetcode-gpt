import numpy as np
from numpy.typing import NDArray

class Solution:

    def get_model_prediction(self, X: NDArray[np.float64], weights: NDArray[np.float64]) -> NDArray[np.float64]:
        # X is (n, m), weights is (m,) -> return (n,) predictions
        # Round to 5 decimal places
        ans = X @ weights
        rounded_ans = [round(i,5) for i in ans]
        return rounded_ans

    def get_error(self, model_prediction: NDArray[np.float64], ground_truth: NDArray[np.float64]) -> float:
        # Compute mean squared error between predictions and ground truth
        # Round to 5 decimal places
        ans = (1/len(ground_truth))*(sum((model_prediction - ground_truth)*(model_prediction - ground_truth) ))
        print(ans)
        rounded_ans_value= [round(i,5).item() for i in ans]
        return rounded_ans_value[0]
