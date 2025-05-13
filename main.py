def calculate_polygon_area_utm(points):
  """
  Calculate the area of a polygon given UTM coordinates.

  Parameters:
  points (list of tuples): List of (Easting, Northing) tuples.

  Returns:
  float: Area in square meters.
  """
  n = len(points)
  area = 0.0

  for i in range(n):
      x1, y1 = points[i]
      x2, y2 = points[(i + 1) % n]  # Wrap around to first point
      area += (x1 * y2) - (x2 * y1)

  return abs(area) / 2


# Example usage
utm_points = [
  (692149, 2166169),
  (692134, 2166169),
  (692131, 2166283),
  (692143, 2166285)
]

area = calculate_polygon_area_utm(utm_points)
print(f"Area: {area:.2f} square meters")
