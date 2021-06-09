import argparse
import json
import os
import re
import yaml

MATCH_DATA = {}


def main():
    parser = argparse.ArgumentParser(description='Generate docker-compose yaml definition from running container.')
    parser.add_argument('filename', nargs=1, type=str, default='docker-compose.yml',
                        help='The name of the docker-compose to parse.')
    return parser.parse_args()


def as_json(filename):
    file = yaml.Loader(open(os.getcwd() + '/' + filename).read())
    return file.get_single_data()


def find_pattern_in_service(service, compare):
    MATCH_DATA[service] = {}
    for key, data in compare.items():
        for item in data:
            if item.lower() in service.lower():
                MATCH_DATA[service][key] = item
                print('Pattern found on service', service, ':', item, 'in', key)


def find_pattern_in_sub_key(service, sub_key, compare):
    for key, data in compare.items():
        for item in data:
            if item.lower() in sub_key.lower():
                MATCH_DATA[service][key] = item
                print('Pattern found on sub_key', sub_key, ':', item, 'in', key)


<<<<<<< HEAD
def match_other_data(service, serviceData):
    if 'ports' in serviceData:
        MATCH_DATA[service]['ports'] = serviceData['ports']
    # if 'networks' in serviceData:
    #     MATCH_DATA[service]['networks'] = serviceData['networks']
    # if 'restart' in serviceData:
    #     MATCH_DATA[service]['restart'] = serviceData['restart']
    if 'depends_on' in serviceData:
        MATCH_DATA[service]['depends_on'] = serviceData['depends_on']
    # if 'volumes' in serviceData:
    #     MATCH_DATA[service]['volumes'] = serviceData['volumes']
    # if 'command' in serviceData:
    #     MATCH_DATA[service]['command'] = serviceData['command']
=======
def match_other_data(service, service_data):
    MATCH_DATA[service]['ports'] = service_data['ports']
    if 'networks' in service_data:
        MATCH_DATA[service]['networks'] = service_data['networks']
    if 'restart' in service_data:
        MATCH_DATA[service]['restart'] = service_data['restart']
    if 'depends_on' in service_data:
        MATCH_DATA[service]['depends_on'] = service_data['depends_on']
    if 'volumes' in service_data:
        MATCH_DATA[service]['volumes'] = service_data['volumes']
    if 'command' in service_data:
        MATCH_DATA[service]['command'] = service_data['command']
>>>>>>> 6588883b2a59d1d2745d7a05bb00395e33dbe57b


def iter_match():
    print(json.dumps(MATCH_DATA, indent=4))


if __name__ == "__main__":
    args = main()
    yamldict = as_json(args.filename[0])

    with open('compare.json') as f:
        compare = json.loads(f.read())
        if 'services' in yamldict:
            print('Starting matching services...')
            # Problem: if mutiple match, it replace previous one
            for service in yamldict['services']:
                # Find match from service name
                find_pattern_in_service(service, compare)

                # In each service, fidn match from image name if exists
                if 'image' in yamldict['services'][service]:
                    find_pattern_in_sub_key(service, yamldict['services'][service]['image'], compare)

                # In each service, fidn match from image name if exists
                if 'container_name' in yamldict['services'][service]:
                    find_pattern_in_sub_key(service, yamldict['services'][service]['container_name'], compare)

                match_other_data(service, yamldict['services'][service])

    iter_match()
