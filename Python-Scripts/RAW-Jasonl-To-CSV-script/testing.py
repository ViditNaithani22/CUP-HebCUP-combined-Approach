import json
import csv

# Open JSONL file for reading
with open('test_clean.jsonl', 'r', encoding='utf-8') as jsonl_file:  # Specify encoding as utf-8
    # Open CSV file for writing
    with open('Java_test.csv', 'w', newline='', encoding='utf-8') as csvfile:  # Specify encoding as utf-8
        fieldnames = ['Source', 'Target', 'ID']  # Adjusted fieldnames to include 'ID'
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # Read each line of the JSONL file
        for line in jsonl_file:
            # Load JSON data from the line
            data = json.loads(line)

            # Extract required fields
            id = data['sample_id']
            source = data['src_method']  # Adjusted field name
            target = data['dst_method']  # Adjusted field name

            # Write extracted data to CSV
            writer.writerow({'Source': source, 'Target': target, 'ID': id})  # Adjusted field names

print("Test CSV file generated successfully!")
