import numpy as np

def adam_optimizer(f, grad, x0, learning_rate=0.001, beta1=0.9, beta2=0.999, epsilon=1e-8, num_iterations=10):
    # Note: `f` is accepted only for interface parity with the PyTorch/Tinygrad
    # variants, which derive gradients from it via autograd. This version uses
    # `grad` only — the objective value `f` is never evaluated.
    
    t = 0
    m = 0
    v = 0
    x = x0

    for i in range(num_iterations):
        t += 1
        gradian = grad(x)
        m = beta1 * m + (1 - beta1) * gradian
        v = beta2 * v + (1 - beta2) * (gradian**2)
        m_hat = m / (1 - beta1**t)
        v_hat = v / (1 - beta2**t)

        x = x - learning_rate * m_hat / (v_hat**0.5 + epsilon)

    return x