from solution import json_to_matrix

def main():
    json_file_path = "records.json"

    with open(json_file_path) as json_file:
        matrix = json_to_matrix(json_file)

if __name__ == "__main__":
    main()
