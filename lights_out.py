import atexit

# from game import Game
from user_info import UserInfo


DUMP = 'dump.tmp'


class Bot_for_Sasha():

	_storage = {}
	try:
		with open(DUMP) as file:
			_storage = eval(file.read())
	except Exception:
		pass

	@atexit.register
	def _dump():
		with open(DUMP, 'w') as file:
			file.write(str(Bot_for_Sasha._storage))

	@classmethod
	def get_user_info(cls, user_id) -> UserInfo:
		info = cls._storage.get(user_id)
		if info is None:
			info = cls._build_info(user_id)
			cls._storage[user_id] = info
		return info

	@classmethod
	def _build_info(cls, user_id, ) -> UserInfo:
		return UserInfo(
			user_id=user_id, best_topic: str
		worst_topic: str
		max_num_cor_ans: int = 0
		average_value
		)
