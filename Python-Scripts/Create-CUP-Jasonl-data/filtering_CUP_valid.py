import csv
import json

def read_jsonl_file(jsonl_file):
    """Reads data from a JSONL file and returns it as a list of dictionaries."""
    data = []
    with open(jsonl_file, 'r', encoding='utf-8') as file:
        for line in file:
            data.append(json.loads(line))
    return data

def write_jsonl_file(data, filename):
    """Writes data to a JSONL file."""
    with open(filename, 'w', encoding='utf-8') as file:
        for item in data:
            json.dump(item, file)
            file.write('\n')

if __name__ == "__main__":
    # Replace this path with the path to your CSV file
    csv_file = "Java_valid.csv"
    jsonl_file = "valid_clean.jsonl"

    # Read the CSV file and identify rows labeled "CUP"
    cup_rows = []
    with open(csv_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            if row[3] == "CUP":  # Assuming the label is in the fourth column
                cup_rows.append(int(row[2]))  # Convert ID to integer

    print("IDs from CSV file:", cup_rows)

    # Read JSONL file and filter data based on cup_rows
    filtered_data = []
    jsonl_data = read_jsonl_file(jsonl_file)
    jsonl_ids = [item['sample_id'] for item in jsonl_data]
    print("IDs from JSONL file:", jsonl_ids)

    for item in jsonl_data:
        if int(item['sample_id']) in cup_rows:  # Convert ID to integer for comparison
            filtered_data.append(item)

    print("Filtered data:", filtered_data)

    # Write filtered data to a new JSONL file
    write_jsonl_file(filtered_data, "filtered_data_validCUP.jsonl")