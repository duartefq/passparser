import argparse

from .report import report
from .parser import parse_pass
from .optimizer import optimize, sanitize
from . import io


def main():
    parser = argparse.ArgumentParser(description='Sanitizes passwords.')

    parser.add_argument('bitwarden_file', metavar='bitwarden_file',
                        help='CSV file from bitwarden')
    parser.add_argument('--keychain-file', dest='keychain_file',
                        help='Keychain file')
    parser.add_argument('--sanitize', dest='sanitize',
                        default=False, nargs='?', const=True,
                        help='Further sanitize logins')
    parser.add_argument('--report', dest='report',
                        default=False, nargs='?', const=True,
                        help='Report weak login and passwords')
    parser.add_argument('--output-optimized', dest='output_file_name',
                        default='optimized_pass.csv',
                        help='Output optimized (default: optimized_pass.csv)')
    parser.add_argument('--output-report', dest='output_report',
                        default='reports.csv',
                        help='Output report (default: reports.csv)')
    args = parser.parse_args()
    # file_name, no_sanitze, report, output_file_name
    pass_list = io.read(args.bitwarden_file)
    if args.keychain_file:
        """
        - Parse
        - Merge into [bitwarden file]
        - Generate output of [parsed passes]
        """
        keychain_passes = io.read(args.keychain_file)
        parsed_keychain_passes = parse_pass(keychain_passes)
        pass_list = optimize(pass_list, parsed_keychain_passes)
    if args.sanitize:
        print('sanitize')
        return
        """
        - Get [parsed passes] or [bitwarden file]
        - Sanitize
        - Generate output of [sanitized passes]
        """
        pass_list = sanitize(pass_list)
    if args.report:
        """
        - Using [sanitized passes] or [bitwarden file]
        - Generate reports
        """
        fieldnames = ['name', 'login_uri', 'login_username', 'login_password']
        report_passes = report(pass_list)
        io.write(args.output_report, fieldnames, report_passes)
    fieldnames = ['folder', 'favorite', 'type', 'name', 'notes', 'fields',
                  'login_uri', 'login_username', 'login_password',
                  'login_totp']
    io.write(args.output_file_name, fieldnames, pass_list)
