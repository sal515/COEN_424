import csv
import json

NDBench_testing = "workload_data/NDBench-testing.csv"
NDBench_training = "workload_data/NDBench-training.csv"
DVD_testing = "workload_data/DVD-testing.csv"
DVD_training = "workload_data/DVD-training.csv"

NDBench_testing_json = "workload_data_json/NDBench-testing.json"
NDBench_training_json = "workload_data_json/NDBench-training.json"
DVD_testing_json = "workload_data_json/DVD-testing.json"
DVD_training_json = "workload_data_json/DVD-training.json"

csv_files = [NDBench_testing, NDBench_training, DVD_testing, DVD_training]
json_files = [NDBench_testing_json, NDBench_training_json, DVD_testing_json, DVD_training_json]


# Open the CSV
def generate_json_from_csv(csv_file_path, json_file_path):
    try:
        with open(csv_file_path, 'r') as file:
            # Change each field name to the appropriate field name
            reader = csv.DictReader(file, fieldnames=(
                "CPU",
                "NetworkIn",
                "NetworkOut",
                "Memory",
                "Final_Target"
            ))
            # Parse the CSV into JSON
            output = json.dumps([row for row in reader])
            # print("JSON parsed!")
            # f.close()


    except:
        print("Couldn't open CSV file")

    try:
        with open(json_file_path, 'w') as file:
            # Save the JSON
            file.write(output)
            # f.close()
            # print("JSON saved!")
    except:
        print("Couldn't save the JSON file")


def remove_header_row(json_file):
    try:
        with open(json_file, 'r') as f:
            remove_first_element = json.load(f)
            del remove_first_element[0]
            f.close()

        with open(json_file, 'w') as f:
            json.dump(remove_first_element, f)
            # f.write(remove_first_element)
            # f.close()

    except:
        print("Error modifying the JSON file")


for i in range(0, len(csv_files)):
    generate_json_from_csv(csv_files[i], json_files[i])
    remove_header_row(json_files[i])

    # What the loop is doing:
    # generate_json_from_csv(NDBench_testing, NDBench_testing_json)
    # generate_json_from_csv(NDBench_training, NDBench_training_json)
    # generate_json_from_csv(DVD_testing, DVD_testing_json)
    # generate_json_from_csv(DVD_training, DVD_training_json)

    # pretty_print_json = json.dumps(remove_first_element, indent=4)
