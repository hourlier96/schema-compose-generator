import argparse
import subprocess
import json

from generator import *


def get_file_name():
    parser = argparse.ArgumentParser()
    parser.add_argument('dc', help="The docker-compose.yml file", type=argparse.FileType('r'))
    args = parser.parse_args()
    open_file = args.dc
    return open_file.name


def get_parsing_output():
    out = subprocess.check_output(["python", "parsing.py", get_file_name()])
    decoded_output = out.decode()
    return decoded_output


def run_diag_generation(parsed_yaml):
    print(json.dumps(parsed_yaml, indent=4))
    output = Generator()
    output.create_diag("Docker-compose diagram")

    elems = {}
    # Creation entrypoint (1 seul)
    for key, value in parsed_yaml.items():
        print("in", key, value)
        if "entrypoints" in value:
            output.create_cluster("Entrypoint")
            output.create_element(service_name=key, element_name=value['entrypoints'])
            output.create_cluster(value['entrypoints'] + " network")
            break
            
    
    for key, value in parsed_yaml.items():
        elem = None
        if "service" in value:
            elem = value['service']
        elif "type" in value:
            elem = value['type']
        elif "framework" in value:
            elem = value['framework']
        elif "langage" in value:
            elem = value['langage']

        if elem is not None:
            output.create_element(service_name=key, element_name=elem)
            elems[key] = elem
        else:
            elems[key] = "N/A"

    print(output.output)
    print(elems)

    for key, value in parsed_yaml.items():
        for link in value['communicate']:
            output.create_link(key, link)

    with open("output.py", "a+")as f:
        f.truncate(0)
        f.write(output.output)

    subprocess.check_output(["python", "output.py"])


def main():
    parsed_yaml = json.loads(get_parsing_output())
    run_diag_generation(parsed_yaml)


if __name__ == '__main__':
    main()
