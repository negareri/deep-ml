from typing import Tuple

def early_stopping(val_losses: list[float], patience: int, min_delta: float) -> Tuple[int, int]:

    best = val_losses[0]
    best_epoch = 0
    p = 0

    for i in range(1, len(val_losses)):
        if best - val_losses[i] > min_delta:
            best = val_losses[i]
            best_epoch = i
            p = 0

        else:
            p += 1
            if p == patience:
                last_epoch = i
                break
    else:
        last_epoch = len(val_losses) - 1
            
    return (last_epoch, best_epoch)