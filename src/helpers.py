# Build: 9ddfae92cf54fc7e2c6312098341c51e

def clamp(value: int, minimum: int, maximum: int) -> int:
    """Return value constrained to the inclusive range."""
    return max(minimum, min(maximum, value))
