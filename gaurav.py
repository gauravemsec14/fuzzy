import json
from fuzzywuzzy import process

def find_emails_fuzzy(obj):
    emails = []

    if isinstance(obj, dict):
        for key, value in obj.items():
            if isinstance(value, str):
                ratio = process.extractOne('email', [key, value], score_cutoff=80)
                if ratio and ratio[1] >= 80:
                    emails.append(value)
            else:
                emails.extend(find_emails_fuzzy(value))

    elif isinstance(obj, list):
        for item in obj:
            emails.extend(find_emails_fuzzy(item))

    return emails

def read_and_find_emails(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        json_data = json.load(file)

    emails = find_emails_fuzzy(json_data)
    return emails

def save_to_json(output_file_path, data):
    try:
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            json.dump(data, output_file, indent=2)
        print(f'Found Email Addresses saved to {output_file_path}')
    except Exception as e:
        print(f'Error saving to JSON file: {e}')

def main():
    input_file_path = 'C:\\Users\\Gaurav Kumar\\Desktop\\testing\\test.json'
    found_emails = read_and_find_emails(input_file_path)

    output_file_path = 'C:\\Users\\Gaurav Kumar\\Desktop\\testing\\emails.json'
    save_to_json(output_file_path, found_emails)

if __name__ == "__main__":
    main()
