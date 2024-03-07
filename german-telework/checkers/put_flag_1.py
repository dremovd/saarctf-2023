import sys

sys.path.append(".")
from interface import store_flag_mc_board
from collections import namedtuple

if __name__ == "__main__":
    team = namedtuple('team', ['ip'])
    test_team = team(ip="144.76.26.107")
    store_flag_mc_board(test_team, "1", "TEST FLAG !!!111", None)