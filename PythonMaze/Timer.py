import time


class Timer:

	def __init__(self):
		self.initial_time = 0

	def start(self):
		self.initial_time = time.perf_counter()

	def get_seconds(self):
		return int(time.perf_counter() - self.initial_time)

	def get_minutes(self):
		return (time.perf_counter() - self.initial_time) / 60

