import argparse
import subprocess
import json

def get_file_name():
    parser = argparse.ArgumentParser()
    parser.add_argument('dc', help="The docker-compose.yml file", type=argparse.FileType('r'))
    args = parser.parse_args()

    open_file = args.dc

    return open_file.name

def get_parsing_output():
    print("parsing_output")
    
    out = subprocess.check_output(["python", "parsing.py", get_file_name()])
    decoded_output = out.decode()

    return decoded_output

def run_diag_generation():
    print("diag generation")

def main():
    tab = json.loads(get_parsing_output())

    for key, value in tab.items():
        # print(f"{key}, {value}")
        # print(f"{value}")
        values = value["communicate"]
        print(f"{key} -> {values}")
        # for subKey, subValue in value.items():

    run_diag_generation()
    print("main")

if __name__ == '__main__':
    main()
    print("toto")