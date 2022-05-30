from enum import Enum


class Section(Enum):
    PHARMACY = {"name": "PHARMACY", "max_turns": 2}
    PERFUMERY = {"name": "PERFUMERY", "max_turns": 6}
    COSMETICS = {"name": "COSMETICS", "max_turns": 7}


