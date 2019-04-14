def parse_pass(keychain_passes):
    """
    Export your keychain as a csv file using this tutorial:
    https://gist.github.com/rmondello/b933231b1fcc83a7db0b
    ---
    Keychain format:
    "Where","Account","Password","Label","Comment","Created","Modified","Kind","Type","Domain","AuthType","Class","Creator"

    Bitwarden format:
    folder,favorite,type,name,notes,fields,login_uri,login_username,login_password,login_totp
    """
    return [transform(row) for row in keychain_passes]


def transform(row):
    return {
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
    }
