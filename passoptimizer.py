#!/usr/bin/env python

"""
Optionally optimize your passwords getting rid of duplicates. Export
your bitwarden passwords and change the file names in this script.

Run via the CLI: `python passoptimizer.py
"""

import csv


def parse_pass():
    optimized_passes = []
    pass_hashes = {}
    with open('bitwarden.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            key = (row['login_uri'], row['login_username'], row['login_password'])
            if key not in pass_hashes:
                optimized_passes.append(row)
                pass_hashes[key] = True
    with open('parsedpass.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            key = (row['login_uri'], row['login_username'], row['login_password'])
            if key not in pass_hashes:
                optimized_passes.append(row)
                pass_hashes[key] = True
    # print(optimized_passes)
    with open('optimizedpass.csv', 'w', newline='') as csvfile:
        fieldnames = ['folder', 'favorite', 'type', 'name', 'notes', 'fields',
                      'login_uri', 'login_username', 'login_password',
                      'login_totp']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in optimized_passes:
            writer.writerow(row)


if __name__ == '__main__':
    parse_pass()
