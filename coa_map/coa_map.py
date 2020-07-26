import csv

def read_map(file):
    with open(file, newline='') as mapfile:
        reader = csv.reader(mapfile, delimiter=',' quotechar='"')
        for row in reader:
            print(row)



def write_file(lst):

    with open('out.csv', 'w', newline='') as csvfile:
        fieldnames = ['A', 'B']
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)

        writer.writeheader()
        writer.writerow({'A': 1, 'B': 2})

if __name__=='__main__':
    write_file([])

