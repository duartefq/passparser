#!/usr/bin/env python

"""
Export your keychain as a csv file using this tutorial:
https://gist.github.com/rmondello/b933231b1fcc83a7db0b

---

Keychain format:
"Where","Account","Password","Label","Comment","Created","Modified","Kind","Type","Domain","AuthType","Class","Creator"

Bitwarden format:
folder,favorite,type,name,notes,fields,login_uri,login_username,login_password,login_totp

Run via the CLI: `python passparser.py
"""

import csv


def parse_pass():
    passed_passes = []
    with open('pass.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            passed_passes.append({
                'folder': 'Keychain',
                'favorite': '',
                'type': 'login',
                'name': row['Where'],
                'notes': '',
                'fields': '',
                'login_uri': row['Where'],
                'login_username': row['Account'],
                'login_password': row['Password'],
                'login_totp': '',
            })
    with open('parsedpass.csv', 'w', newline='') as csvfile:
        fieldnames = ['folder', 'favorite', 'type', 'name', 'notes', 'fields',
                      'login_uri', 'login_username', 'login_password',
                      'login_totp']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in passed_passes:
            writer.writerow(row)


if __name__ == '__main__':
    parse_pass()
