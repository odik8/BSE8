#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def check_positions(teams, points):
    sorted_teams = sorted(zip(teams, points), key=lambda x: x[1], reverse=True)

    sorted_teams = [t[0] for t in sorted_teams]

    if sorted_teams == teams:
        return "Команды перечислены в соответствии с их позициями в чемпионате."
    else:
        return "Команды перечислены не в соответствии с их позициями в чемпионате."


if __name__ == "__main__":
    print(check_positions(["Team A", "Team B", "Team C"], [30, 2, 20]))
