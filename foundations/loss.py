import numpy as np
from numpy.typing import NDArray
import math


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array of logits
        # Hint: subtract max(z) for numerical stability before computing exp
        # return np.round(your_answer, 4)
        total_distrubution = 0
        max_z=max(z)
    
        for i in range(len(z)):
            total_distrubution += math.exp(z[i]-max_z)
        ans = []
        for i in range(len(z)):
            ith_distrubution = round(math.exp(z[i]-max_z)/total_distrubution,4)
            ans.append(ith_distrubution)

        return ans
        





