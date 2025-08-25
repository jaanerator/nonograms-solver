import numpy as np

from src.constants import QUIZ_SAMPLE
from src.solver import get_all_combinations, compare


def get_size(quiz):
    return len(quiz["h"]), len(quiz["v"])

if __name__ == "__main__":
    result = np.full(get_size(QUIZ_SAMPLE), "?", dtype=str)
    v, h = result.shape
    n_unknown = v * h

    for i in range(v):
        combs = get_all_combinations(QUIZ_SAMPLE["v"][i], h)
        now_pattern = "".join(list(result[:, i]))
        new_pattern = compare(combs, now_pattern)
        result[:, i] = list(new_pattern)
    for i in range(h):
        combs = get_all_combinations(QUIZ_SAMPLE["h"][i], v)
        now_pattern = "".join(list(result[i, :]))
        new_pattern = compare(combs, now_pattern)
        result[i, :] = list(new_pattern)
    print("\n".join(["".join(list(elem)) for elem in list(result)]))
