import time

from src.constants import QUIZ_SAMPLE
from src.solver import NonogramsSolver


if __name__ == "__main__":
    start = time.time()

    solver = NonogramsSolver(QUIZ_SAMPLE)
    solver.setup()
    solver.solve()

    print("\n".join(["".join(list(elem)) for elem in list(solver.result)]))
    end = time.time()
    print(f"Elapsed: {end - start}")
