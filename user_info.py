from dataclasses import dataclass
from typing import Tuple


@dataclass()
class UserInfo():
	user_id: int
	best_topic: str
	worst_topic: str
	max_num_cor_ans: int = 0
	average_value: int = 0



