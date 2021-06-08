import argparse
import json
import os
import re
import yaml

MATCH_DATA = {}

def main():
    parser = argparse.ArgumentParser(description='Generate docker-compose yaml definition from running container.')
    parser.add_argument('filename', nargs=1, type=str, default='docker-compose.yml', help='The name of the docker-compose to parse.')
    return parser.parse_args()

def as_json(filename):
    file = yaml.Loader(open(os.getcwd() + '/' + filename).read())
    
    return file.get_single_data()

def find_pattern_in_service(service):
    
    with open('compare.json') as f:
        content = json.loads(f.read())
        for key, data in content.items():
            for item in data:
                if item.lower() in service.lower():
                    MATCH_DATA[service] = {}
                    MATCH_DATA[service][key] = item
                    print('Pattern found on service', service, ':', item, 'in', key)

def iter_match():
    print('\nResult', MATCH_DATA)
    """ for key, value in MATCH_DATA.items():
        print(key, value) """


if __name__ == "__main__":
    args = main()
    yamldict = as_json(args.filename[0])
    # print(json.dumps(yamldict, indent=4))

    if 'services' in yamldict:
        print('Starting matching services...')
        for service in yamldict['services']:
            find_pattern_in_service(service)

    # PART 2
    if 'build' in yamldict['services']:
        if 'image' in yamldict['services']:
            pass
    
    iter_match()