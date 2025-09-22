import time

def is_valid(solution, row, col):
    for c in range(col):
        if solution[c] == row or \
           abs(solution[c] - row) == abs(c - col):
            return False
    return True

def solve_n_queens(n):
    solutions = []
    def backtrack(col=0, solution=[]):
        if col == n:
            solutions.append(solution[:])
            return
        for row in range(n):
            if is_valid(solution, row, col):
                solution.append(row)
                backtrack(col + 1, solution)
                solution.pop()
    backtrack()
    return solutions

def main():
    ns = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    print(f"{'n':>2} | {'# soluciones':>12} | {'Tiempo (s)':>10}")
    print("-" * 32)
    for n in ns:
        start = time.time()
        sols = solve_n_queens(n)
        elapsed = time.time() - start
        print(f"{n:>2} | {len(sols):>12} | {elapsed:>10.5f}")
        

if __name__ == "__main__":
    main()
    