import csv


def calculate_ncsm(old_code, new_code):
    # Calculate lengths of the code strings
    old_size = len(old_code)
    new_size = len(new_code)

    # Calculate NCSM
    ncsm = min(old_size, new_size) / max(old_size, new_size)

    return ncsm

if __name__ == "__main__":
    # Replace this path with the path to your CSV file
    code_pairs_csv = "./Java_train.csv"

    # Read data from the CSV file
    with open(code_pairs_csv, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        rows = list(reader)

    # Modify data and write back to the CSV file
    with open(code_pairs_csv, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        for row in rows:
            old_code = row[0] if row else ''
            new_code = row[1] if len(row) > 1 else ''

            ncsm = calculate_ncsm(old_code, new_code)
            label = "CUP" if ncsm > 0.89 else "hebCUP"

            row.append(label)
            row.append(ncsm)  # Append NCSM score to the row
            writer.writerow(row)