import statistics


def calculate_pixel_brightness(red: int, green: int, blue: int) -> int:
    """Calculates the brightness of a pixel based on its r, g, b values."""
    return statistics.mean([red, green, blue])