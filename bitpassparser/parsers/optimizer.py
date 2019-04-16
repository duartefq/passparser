from tldextract import extract


def optimize(bitwarden_passes, parsed_keychain_passes):
    """
    Optionally optimize your passwords getting rid of duplicates. Export
    your bitwarden passwords and change the file names in this script.
    """
    optimized_passes = []
    pass_hashes = {}
    for row in bitwarden_passes:
        key = (
            row['login_uri'],
            row['login_username'],
            row['login_password']
        )
        if key not in pass_hashes:
            optimized_passes.append(row)
            pass_hashes[key] = True
    for row in parsed_keychain_passes:
        key = (
            row['login_uri'],
            row['login_username'],
            row['login_password']
        )
        if key not in pass_hashes:
            optimized_passes.append(row)
            pass_hashes[key] = True
    return optimized_passes


def sanitize(pass_list):
    optimized_passes = []
    pass_hashes = {}
    for row in pass_list:
            hostname = extract(row['login_uri']).domain
            key = (
                hostname,
                row['login_username'],
                row['login_password']
            )
            if key not in pass_hashes:
                optimized_passes.append(row)
                pass_hashes[key] = True
    return optimized_passes
