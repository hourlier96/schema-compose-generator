import argparse
import subprocess

def get_file_name():
    parser = argparse.ArgumentParser()
    parser.add_argument('dc', help="The docker-compose.yml file", type=argparse.FileType('r'))
    args = parser.parse_args()

    open_file = args.dc

    return open_file.name
    # subprocess.call('python', 'parsing.py', open_file.name)


def get_parsing_output():
    print("parsing_output")
    # get_file_name()
    proc = subprocess.Popen(['python', 'parsing.py', get_file_name()])
    json = proc.communicate()[0]
    print(json)
    return json

def run_diag_generation():
    print("diag generation")

def main():
    json = get_parsing_output()

    for key, value in json.items():
        if None != json:
            print(f"{key}, {value}")

    run_diag_generation()
    print("main")

if __name__ == '__main__':
    main()
    print("toto")