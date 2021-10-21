
class Clock:

  def __init__(self, minutes, seconds):
    if 0 <= minutes < 60:
      self.minutes = minutes
    if 0 <= seconds < 60:
      self.seconds = seconds
      self.times_up = False

  def minus(self):
    if self.minutes == 0 and self.seconds == 1:
      self.times_up = True
    elif self.seconds == 0:
      self.minutes -= 1
      self.seconds = 60
    self.seconds -= 1

  def is_time_up(self):
    return self.times_up

  def __str__(self):
    return f"{self.minutes:02d}:{self.seconds:02d}"