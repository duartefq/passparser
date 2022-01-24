# passparser

Parse macOS Keychain passwords and output a bitwarden-compatible csv file.

## usage

```
passsanitizer.py [-h] [--keychain-file KEYCHAIN_FILE]
                      [--sanitize [SANITIZE]] [--report [REPORT]]
                      [--output-optimized OUTPUT_FILE_NAME]
                      [--output-report OUTPUT_REPORT]
                      bitwarden_file

Sanitizes passwords.

positional arguments:
  bitwarden_file        CSV file from bitwarden

optional arguments:
  -h, --help            show this help message and exit
  --keychain-file KEYCHAIN_FILE
                        Keychain file
  --sanitize [SANITIZE]
                        Further sanitize logins
  --report [REPORT]     Report weak login and passwords
  --output-optimized OUTPUT_FILE_NAME
                        Output optimized (default: optimized_pass.csv)
  --output-report OUTPUT_REPORT
                        Output report (default: reports.csv)
```
