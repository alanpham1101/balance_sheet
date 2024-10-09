import sys

from generate_data import GenerateSampleData
from process_data import ProcessData


if __name__ == '__main__':
    service_name = sys.argv[1]
    if service_name == 'generate_data':
        service = GenerateSampleData(num_lines=100)
        service.generate_data_file()
        sys.stdout.write("Done generating data file")
    elif service_name == 'process_data':
        option = input("Select:\n\tOption 1: Number\n\tOption 2: Chart\n")
        service = ProcessData(data_path='data/sample_data.csv')
        service.read_data_from_file()
        service.process_data(option)
    else:
        sys.stdout.write("Invalid service")
