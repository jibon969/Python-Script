
# import csv
#
# with open('Product-2020-05-31.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     for line in csv_reader:
#         print(line)


# import csv
#
# with open('Product-2020-05-31.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#
#     with open('new_csv.csv', 'w') as new_file:
#         csv_writer = csv.writer(new_file, delimiter='\t')
#
#         for line in csv_reader:
#             csv_writer.writerow(line)
#             print(line)


import csv
with open('Product-2020-05-31.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('new_csv.csv', 'w') as new_file:
        field_names = ['title', 'brand']
        csv_writer = csv.DictWriter(new_file, fieldnames=field_names, delimiter='\t')
        csv_writer.writeheader()
        for line in csv_reader:
            csv_writer.writerow(line)
