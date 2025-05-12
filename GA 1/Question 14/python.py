import csv

# Symbols we're interested in
target_symbols = {'Š', '’', 'OR'}

# Running total
total_sum = 0

# File 1: data1.csv (CP-1252 encoded CSV)
with open('data1.csv', encoding='cp1252') as f:
    reader = csv.reader(f)
    for row in reader:
        if row and row[0] in target_symbols:
            total_sum += float(row[1])

# File 2: data2.csv (UTF-8 encoded CSV)
with open('data2.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        if row and row[0] in target_symbols:
            total_sum += float(row[1])

# File 3: data3.txt (UTF-16 encoded tab-separated)
with open('data3.txt', encoding='utf-16') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        if row and row[0] in target_symbols:
            total_sum += float(row[1])

# Output the final sum
print(f"Total sum for symbols {target_symbols}: {total_sum}")

