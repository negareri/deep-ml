def product_rule_derivative(f_coeffs: list, g_coeffs: list) -> list:
    """
    Compute the derivative of the product of two polynomials.
    """

    def deriv(c):
        l = []
        for i in range(1, len(c)):
            l.append(c[i] * i)

        if len(l) == 0:
            return [0]

        return l

    def multiply(a, b):
        result = [0] * (len(a) + len(b) - 1)

        for i in range(len(a)):
            for j in range(len(b)):
                result[i + j] += a[i] * b[j]

        return result

    def add(a, b):
        result = [0] * max(len(a), len(b))

        for i in range(len(result)):
            if i < len(a):
                result[i] += a[i]

            if i < len(b):
                result[i] += b[i]

        return result

    result = add(
        multiply(deriv(f_coeffs), g_coeffs),
        multiply(deriv(g_coeffs), f_coeffs)
    )

    # remove trailing zeros
    while len(result) > 1 and result[-1] == 0:
        result.pop()

    # round and convert to float
    result = [round(float(x), 4) for x in result]

    return result