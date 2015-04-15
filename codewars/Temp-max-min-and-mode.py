class TempTracker:

  def __init__(self):
    # initialize instance variables
    self.max = self.min = self.maxseentemp = None
    self.sum = self.count = self.maxseen = 0
    self.seen = {}

  def insert(self, temperature):
    # insert new temperature
    if not self.max or temperature > self.max:
      self.max = temperature
    if not self.min or temperature < self.min:
      self.min = temperature
    self.sum += temperature
    self.count += 1
    self.seen[temperature] = self.seen.get(temperature, 0) + 1
    if self.seen[temperature] > self.maxseen:
      self.maxseentemp = temperature
      self.maxseen = self.seen[temperature]

  def get_max(self):
    # return max temp ever added
    return self.max

  def get_min(self):
    # return min temp ever added
    return self.min

  def get_mean(self):
    # return mean of all temps added
    if self.count:
      return self.sum * 1.0 / self.count

  def get_mode(self):
    # return mode of all temps added
    return self.maxseentemp