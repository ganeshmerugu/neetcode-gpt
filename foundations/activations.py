import numpy as np
from numpy.typing import NDArray
import math


class Solution:
    
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: 1 / (1 + e^(-z))
        # return np.round(your_answer, 5)
        list_ans= []
        for i in range(len(z)):
            ans = round(1/(1+math.exp(-z[i])),5)
            list_ans.append(ans)

        return list_ans


    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: max(0, z) element-wise
        list_ans =[]
        for i in range(0,len(z)):
            if z[i]<0:
                list_ans.append(float(0))
            else:
                list_ans.append(z[i])

            
        return list_ans
