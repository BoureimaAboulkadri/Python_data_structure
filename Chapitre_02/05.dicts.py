import csv
import codecs

with codecs.open('departement.csv ', encoding='utf8', errors='replace') as dept:
    rd = csv.reader(dept, delimiter=',')
    # codes = tuple(r[1] for r in rd)
    # dept.seek(0)
    # departements = tuple(r[2] for r in rd)

    # codes, departements = zip(*((r[1], r[2]) for r in rd))
    # melange = dict(((r[1], r[2]) for r in rd))

    melange = {r[1]: r[2] for r in rd}

# melange = dict(zip(codes, departements))

print(melange)
