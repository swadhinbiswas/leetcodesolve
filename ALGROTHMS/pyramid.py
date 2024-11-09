import math
from typing import Tuple

def get_volume_and_surface_area(base_side: float, height: float) -> Tuple[float, float]:
    """
    Calculate volume and surface area of a pyramid given base side and height.
    
    Args:
        base_side: Length of one side of the square base
        height: Height of the pyramid
    
    Returns:
        Tuple of (volume, surface_area)
    """
    # Volume = (1/3) * base_area * height
    volume = (1/3) * base_side * base_side * height
    
    # Surface area = base_area + 4 * triangle_area
    slant_height = math.sqrt(height * height + (base_side/2) * (base_side/2))
    surface_area = base_side * base_side + 2 * base_side * slant_height
    
    return volume, surface_area

def find_optimal_dimensions(target_surface_area: float) -> Tuple[float, float, float]:
    """
    Find the base side length and height that maximize volume for given surface area.
    Uses numerical optimization with binary search.
    
    Args:
        target_surface_area: Desired total surface area
    
    Returns:
        Tuple of (max_volume, optimal_base_side, optimal_height)
    """
    if target_surface_area <= 0:
        return 0.0, 0.0, 0.0
    
    # Start with reasonable bounds for base side
    # Surface area must be at least base_side^2, so base_side ≤ √surface_area
    max_base = math.sqrt(target_surface_area)
    min_base = max_base / 1000  # Arbitrary small value
    
    max_volume = 0.0
    optimal_base = 0.0
    optimal_height = 0.0
    
    # Binary search for optimal base side
    for _ in range(100):  # Sufficient iterations for precision
        third = (max_base - min_base) / 3
        base1 = min_base + third
        base2 = max_base - third
        
        # For each base side, find height that gives target surface area
        # Use quadratic formula to solve for height
        def find_height(base: float) -> float:
            a = 2 * base  # coefficient of slant_height in surface area equation
            b = 0
            c = base * base - target_surface_area
            
            # height = sqrt(slant_height^2 - (base/2)^2)
            # Substitute and solve
            quarter_base_sq = (base/2) * (base/2)
            
            if a == 0:
                return 0
                
            slant_height = -c/a  # simplified from quadratic formula as b=0
            if slant_height * slant_height <= quarter_base_sq:
                return 0
                
            return math.sqrt(slant_height * slant_height - quarter_base_sq)
        
        height1 = find_height(base1)
        height2 = find_height(base2)
        
        vol1 = (1/3) * base1 * base1 * height1
        vol2 = (1/3) * base2 * base2 * height2
        
        if vol1 > vol2:
            max_base = base2
            if vol1 > max_volume:
                max_volume = vol1
                optimal_base = base1
                optimal_height = height1
        else:
            min_base = base1
            if vol2 > max_volume:
                max_volume = vol2
                optimal_base = base2
                optimal_height = height2
    
    return max_volume, optimal_base, optimal_height

def main():
    while True:
        surface_area = float(input())
        if surface_area < 0:
            break
            
        max_volume, _, _ = find_optimal_dimensions(surface_area)
        print(f"{max_volume:.4f}")

if __name__ == "__main__":
    main()