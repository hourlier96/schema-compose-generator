import argparse
import subprocess
import json

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
    # proc = subprocess.Popen(['python', 'parsing.py', get_file_name()])
    # print(f"Before COMMUNICATE \n {proc.communicate()[0]} \n AFTER COMMUNICATE")

    out = subprocess.check_output(["python", "parsing.py", get_file_name()])
    decoded_output = out.decode()
    print(f"Before OUTPUT \n {decoded_output} \n AFTER OUTPUT")


    # json = proc.communicate()[0]
    # print(f"Before JSON \n {json} \n AFTER JSON")
    return decoded_output

def run_diag_generation():
    print("diag generation")

def main():
    tab = json.loads(get_parsing_output())

    for key, value in tab.items():
        if None != tab:
            print(f"{key}, {value}")

    run_diag_generation()
    print("main")

if __name__ == '__main__':
    main()
    print("toto")