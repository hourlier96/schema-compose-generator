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
                #print('Pattern found on service', service, ':', item, 'in', key)


def set_links(service, x_communication):
    """
    Set communicate key to identify communications between containers
    """
    MATCH_DATA[service]['communicate'] = []
    for link in x_communication:
        elems = link.split('>>')
        if elems[0].replace(' ', '') == service:
             MATCH_DATA[service]['communicate'].append(elems[1].replace(' ', ''))


def find_pattern_in_sub_key(service, sub_key, compare):
    for key, data in compare.items():
        for item in data:
            if item.lower() in sub_key.lower():
                MATCH_DATA[service][key] = item
                #print('Pattern found on sub_key', sub_key, ':', item, 'in', key)


def match_other_data(service, serviceData):
    if 'ports' in serviceData:
        MATCH_DATA[service]['ports'] = serviceData['ports']
    if 'networks' in serviceData:
        MATCH_DATA[service]['networks'] = serviceData['networks']
    if 'depends_on' in serviceData:
        MATCH_DATA[service]['depends_on'] = serviceData['depends_on']
    # if 'restart' in serviceData:
    #     MATCH_DATA[service]['restart'] = serviceData['restart']
    # if 'volumes' in serviceData:
    #     MATCH_DATA[service]['volumes'] = serviceData['volumes']
    # if 'command' in serviceData:
    #     MATCH_DATA[service]['command'] = serviceData['command']


def build_match_data(yamldict):
    with open('compare.json') as f:
        compare = json.loads(f.read())
        if 'services' in yamldict:
            print('Starting matching services...')
            # Problem: if mutiple match, it replace previous one
            for service in yamldict['services']:
                # Find match from service name
                find_pattern_in_service(service, compare)

                set_links(service, yamldict['x-communication'])

                # In each service, find match from image name if exists
                if 'image' in yamldict['services'][service]:
                    find_pattern_in_sub_key(service, yamldict['services'][service]['image'], compare)

<<<<<<< HEAD
                # In each service, find match from container name if exists
=======
                # In each service, fidn match from image name if exists
>>>>>>> 6588883 (fix: should rework if__name.. in order to avoid Shadows name...)
                if 'container_name' in yamldict['services'][service]:
                    find_pattern_in_sub_key(service, yamldict['services'][service]['container_name'], compare)

                match_other_data(service, yamldict['services'][service])

<<<<<<< HEAD
    print(json.dumps(MATCH_DATA, indent=4))


if __name__ == "__main__":
    args = main()
    yamldict = as_json(args.filename[0])
    build_match_data(yamldict)
=======
    iter_match()
>>>>>>> 6588883 (fix: should rework if__name.. in order to avoid Shadows name...)
