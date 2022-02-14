import os
import sys
import numpy as np

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../'))
)

import app.np.cplx.t as t
import app.np.cplx.normalize as normalize

def create(bit: int = 7) -> np.ndarray:
    N = 2 ** bit
    r_list = np.random.uniform(0, 1, N)
    theta_list = np.random.uniform(0, 2 * np.pi, N)
    sin_list = np.sin(theta_list)
    cos_list = np.cos(theta_list)

    t.t()

    return normalize.normalize(r_list * sin_list + 1j * r_list * cos_list)