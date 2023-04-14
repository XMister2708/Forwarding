from dataclasses import dataclass, field
from enum import Enum
from typing import Dict


@dataclass
class PageSwitchCommand():
	next_page: Enum
	content: Dict = field(default_factory=dict)


PAGE = Enum('PAGE', (
	'MAIN',
	'INFO',

	'NO_PAGE',
))


PAGE_TEXT = {
	PAGE.MAIN: 'Привет! Я бот, который поможет тебе проверить твои знания в физике. Давай начнем!',
	PAGE.INFO: 'Это бот, помогающий понять насколько хорошо Вы знаете физику. Сделали его две лучшие'
			' ученицы из 10 "Н" класса.',
}

PAGE_REPLY_BUTTONS = {
	PAGE.MAIN: {
		'О нас': PageSwitchCommand(PAGE.INFO),
		#'Играть': PageSwitchCommand(PAGE.CGMD),
	},
	PAGE.INFO: {
		'Назад': PageSwitchCommand(PAGE.MAIN),
	},

}

PAGE_COMMANDS = {
}

