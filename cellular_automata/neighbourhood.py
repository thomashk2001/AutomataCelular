class neighbourhood:
  def __init__(self, neighbourhood_type, neighbourhood_reach, frontier):
    self.frontier = frontier
    if neighbourhood_type == "v":
      self.count_neighbours = self.von_neumann
      if neighbourhood_reach == "2":
        self.count_neighbours = self.extended_von_neumann
    elif neighbourhood_type == "m":
      self.count_neighbours = self.moore
      if neighbourhood_reach == "2":
        self.count_neighbours = self.extended_moore
    else:
      print("Not a valid neighbourhood option.")
      exit()
    
  def out_of_bounds(self, m, r, c):
    return 0 > r or r >= m.shape[0] or 0 > c or c >= m.shape[1]

  def von_neumann_generic(self, m, r, c, reach):
    neighbours = [(r - reach, c), (r, c + reach), (r + reach, c), (r, c - reach)]
    total_neighbours = 0
    for (i, j) in neighbours:
      if self.out_of_bounds(m, i, j):
         total_neighbours += self.frontier.is_on(m, i, j)
      else:
         total_neighbours += m[i, j]
    return total_neighbours

  def von_neumann(self, m, r, c):
     return self.von_neumann_generic(m, r, c, 1)

  def extended_von_neumann(self, m, r, c):
    return self.von_neumann_generic(self, m, r, c, 2) + self.moore_generic(self, m, r, c, 1)

  def moore_generic(self, m, r, c, reach):
    total_neighbours = 0
    for i in range(-reach, reach + 1, 1):
       for j in range(-reach, reach + 1, 1):
          if i == r and j == c:
             pass
          elif self.out_of_bounds(m, r, c):
             total_neighbours += self.frontier.is_on(m, r, c)
          else:
              total_neighbours += m[i, j]
    return total_neighbours

  def moore(self, m, r, c):
    return self.moore_generic(m, r, c, 1)
  
  def extended_moore(self, m, r, c):
    return self.moore_generic(m, r, c, 2)