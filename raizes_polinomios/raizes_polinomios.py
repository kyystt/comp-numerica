class Polinomio:
    def __init__(self, coefs: list[float]):
        self.coef= coefs
        self.grau: int = len(self.coef) - 1
    
    def eval_pol(self, x: float) -> float:
        res: float = 0
        for i in range(self.grau+1):
            res += self.coef[len(self.coef)-i-1] * pow(x, i)
        
        return res
    
    def find_interval(self, a: float = -100.0, b: float = 100.0, full_res = None, tol: float = 1e-7) -> list[list[float]] | list[float]:
        if full_res is None:
            full_res = []

        if abs(b - a) < tol:
            return full_res

        if self.eval_pol(a) * self.eval_pol(b) <= 0:
            full_res.append([a, b])
        else:
            mid = (a + b) / 2
            self.find_interval(a, mid, full_res, tol)
            self.find_interval(mid, b, full_res, tol)
            
        return full_res
    
    def bissection(self, lower_bound: float, upper_bound: float, tol: float = 1e-15, max_iter: int = 100) -> float | None:
        eval_lower = self.eval_pol(lower_bound)
        eval_upper = self.eval_pol(upper_bound)

        if eval_lower * eval_upper > 0:
            return None
        
        for _ in range(max_iter):
            mid = (upper_bound + lower_bound) / 2
            if upper_bound - lower_bound < tol:
                return mid
            
            eval_mid = self.eval_pol(mid)

            if abs(eval_mid) < tol:
                return mid

            if eval_lower * eval_mid < 0:
                upper_bound = mid
                eval_upper = eval_mid
            else:
                lower_bound = mid
                eval_lower = eval_mid

        return (upper_bound + lower_bound) / 2
    
    def false_position(self, lower_bound: float, upper_bound: float, tol: float = 1e-15, max_iter: int = 100) -> float | None:
        eval_lower = self.eval_pol(lower_bound)
        eval_upper = self.eval_pol(upper_bound)

        if eval_lower * eval_upper > 0:
            return None
        
        for _ in range(max_iter):
            mid = (lower_bound * eval_upper - upper_bound * eval_lower) / (eval_upper - eval_lower)
            if upper_bound - lower_bound < tol:
                return mid
            
            eval_mid = self.eval_pol(mid)

            if abs(eval_mid) < tol:
                return mid

            if eval_lower * eval_mid < 0:
                upper_bound = mid
                eval_upper = eval_mid
            else:
                lower_bound = mid
                eval_lower = eval_mid

        return (lower_bound * eval_upper - upper_bound * eval_lower) / (eval_upper - eval_lower)
                
def main():
    n = 1

    pol1 = Polinomio([1, -8, 12])
    pol1_intervals = pol1.find_interval(a=0, b=10)
    print(f"pol1: {pol1_intervals}")
    for interval in pol1_intervals:
        print(f"raiz #{n}: {pol1.false_position(interval[0], interval[1])}")
        n += 1
    print("="*50)
    n = 1

    pol2 = Polinomio([1, 2, -3, 0])
    pol2_intervals = pol2.find_interval(a=-5, b=5)
    print(f"pol2: {pol2_intervals}")
    for interval in pol2_intervals:
        print(f"raiz #{n}: {pol2.false_position(interval[0], interval[1])}")
        n += 1
    print("="*50)
    n = 1

    pol3 = Polinomio([1, 0, -10, 0, 9])
    pol3_intervals = pol3.find_interval(a=-4, b=4)
    print(f"pol3: {pol3_intervals}")
    for interval in pol3_intervals:
        print(f"raiz #{n}: {pol3.false_position(interval[0], interval[1])}")
        n += 1
    print("="*50)
    n = 1

    pol4 = Polinomio([1, -4, 2])
    pol4_intervals = pol4.find_interval(a=0, b=4)
    print(f"pol4: {pol4_intervals}")
    for interval in pol4_intervals:
        print(f"raiz #{n}: {pol4.false_position(interval[0], interval[1])}")
        n += 1
    print("="*50)
    n = 1

    pol5 = Polinomio([1, -4, 4, 0])
    pol5_intervals = pol5.find_interval(a=-1, b=3)
    print(f"pol5: {pol5_intervals}")
    for interval in pol5_intervals:
        print(f"raiz #{n}: {pol5.false_position(interval[0], interval[1])}")
        n += 1
    n = 1

main()


