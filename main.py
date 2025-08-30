from copy import deepcopy
import time

import numpy as np

from src.constants import QUIZ_SAMPLE
from src.solver import get_all_combinations, compare


def get_size(quiz):
    return len(quiz["h"]), len(quiz["v"])

class NonogramsSolver:
    def __init__(self, quiz):
        self.quiz = deepcopy(quiz)
        self.result = None
        self.v = None
        self.h = None
        self._combinations_dict = None

    def setup(self):
        # get_size, get_all_combinations
        self.result = np.full(get_size(self.quiz), "?", dtype=str)
        self.v, self.h = self.result.shape
        self._combinations_dict = {"v": [], "h": []}
        for i in range(self.v):
            combs = get_all_combinations(self.quiz["v"][i], self.h)
            self._combinations_dict["v"].append(combs)
        for i in range(self.h):
            combs = get_all_combinations(self.quiz["h"][i], self.v)
            self._combinations_dict["h"].append(combs)

    def solve(self):
        n_unknown = self.v * self.h
        while True:
            for i in range(self.v):
                combs = self._combinations_dict["v"][i]
                now_pattern = "".join(list(self.result[:, i]))
                new_pattern = compare(combs, now_pattern)
                self.result[:, i] = list(new_pattern)
            for i in range(self.h):
                combs = self._combinations_dict["h"][i]
                now_pattern = "".join(list(self.result[i, :]))
                new_pattern = compare(combs, now_pattern)
                self.result[i, :] = list(new_pattern)

            n_unknown_now = np.sum(self.result == "?")
            if n_unknown_now == n_unknown or n_unknown_now < 1:
                break
            n_unknown = n_unknown_now


if __name__ == "__main__":
    start = time.time()

    solver = NonogramsSolver(QUIZ_SAMPLE)
    solver.setup()
    solver.solve()

    print("\n".join(["".join(list(elem)) for elem in list(solver.result)]))
    end = time.time()
    print(f"Elapsed: {end - start}")
