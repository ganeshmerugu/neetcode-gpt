class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        ans = init
        derivative_f = lambda x : 2*x
        for _ in range(iterations):
            ans-= learning_rate*derivative_f(ans)
        return round(ans,5)
      




        
