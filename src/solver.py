import numpy as np


def get_all_combinations(list_: list[int], length: int) -> list[str]:
    if len(list_) == 0:
        result = [" " * length]
    else:
        first = list_[0]
        rem = list_[1:]
        result = []
        for i in range(length - (first + sum(rem) + len(rem)) + 1):
            prefix = " " * i + "O" * first
            if len(prefix) < length:
                prefix += " "
            result_sub = get_all_combinations(rem, length - len(prefix))
            result += [f"{prefix}{elem}" for elem in result_sub]
    return result

def compare(combinations: list[str], now_pattern: str) -> str:
    combs = np.array([list(comb) for comb in combinations])
    now_arr = np.array(list(now_pattern))
    is_unknown = now_arr == "?"

    is_match = np.apply_along_axis(
        lambda x: np.all((x == now_arr) | is_unknown),
        axis=1,
        arr=combs
    )
    combs = combs[is_match, :]

    is_all_same = (
        np.all(combs == "O", axis=0) |
        np.all(combs == " ", axis=0)
    )
    result = combs[0, :]
    result[~is_all_same] = "?"
    return "".join(list(result))
