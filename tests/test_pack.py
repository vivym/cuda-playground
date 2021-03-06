import random
import time

import numpy as np
import torch

from cuda_playground.ops.vb_matrices import VBMatrices
from cuda_playground.ops.vb_mm import VBMMAlgo, vbmm


def main():
    random.seed(0)

    batch_size = 4096
    A_, B_ = [], []
    for _ in range(batch_size):
        m, n, k = random.randint(32, 256), random.randint(32, 256), 64
        # m, n, k = 256, 256, 64
        A_.append(torch.randn(m, k).contiguous().cuda())
        B_.append(torch.randn(k, n).contiguous().cuda())

    A = VBMatrices(A_)
    A_packed = A.pack_up()

    print("num_pack:", len(A_packed))
    for A_i in A_packed:
        print(A_i.shape)

    print("done")


if __name__ == "__main__":
    main()
