def report(pass_list):
    weak_passes = []
    weak_hashes = {}
    for row in pass_list:
            key = (
                row['login_username'],
                row['login_password']
            )
            if key in weak_hashes:
                weak_passes.append(row)
            else:
                weak_hashes[key] = True
    return sorted(weak_passes, key=lambda i: i['login_username'])
