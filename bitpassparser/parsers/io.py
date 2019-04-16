import csv


def read(input_file):
    with open(input_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]


def write(output_file, fieldnames, data):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(parse(row, fieldnames))


def parse(row, keys):
    return {key: row[key] for key in keys}
