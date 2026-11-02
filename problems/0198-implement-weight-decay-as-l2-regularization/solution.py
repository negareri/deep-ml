import numpy as np

def apply_weight_decay(parameters: list[list[float]], gradients: list[list[float]], 
                       lr: float, weight_decay: float, apply_to_all: list[bool]) -> list[list[float]]:
	"""
	Apply weight decay (L2 regularization) to parameters.
	
	Args:
		parameters: List of parameter arrays
		gradients: List of gradient arrays
		lr: Learning rate
		weight_decay: Weight decay factor
		apply_to_all: Boolean list indicating which parameter groups get weight decay
	
	Returns:
		Updated parameters
	"""
	parameters = np.array(parameters)
	grad = np.array(gradients)
	apply_to_all = np.array(apply_to_all)
	
	decay_mask = apply_to_all[:, np.newaxis]
	
	updated_parameters = (
        parameters
        - lr * grad
        - lr * weight_decay * parameters * decay_mask
    )
	
	return updated_parameters.tolist()