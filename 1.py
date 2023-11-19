#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    data = [
        ('Команда1', 15),
        ('Команда2', 20),
        ('Команда3', 30),
    ]

    sorted_data = sorted(data, key=lambda x: x[1], reverse=True)
    return sorted_data



if __name__ == "__main__":
    print(main())