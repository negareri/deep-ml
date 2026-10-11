import torch

class MyTransform:
    def __call__(self, x: torch.Tensor) -> torch.Tensor:
        """
        x: (1, 28, 28) float tensor in [0,1]
        Return: transformed tensor, same shape/dtype.
        Must be non-identity and deterministic.
        """
        mean = x.mean()
        std = x.std().clamp(min=1e-6)

        x = (x - mean) / std
        x = x.clamp(-3.0, 3.0)

        return x
