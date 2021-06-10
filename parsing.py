import argparse
import json
import os
import yaml

MATCH_DATA = {}


def main():
    parser = argparse.ArgumentParser(description='Generate docker-compose yaml definition from running container.')
    parser.add_argument('filename', nargs=1, type=str, default='docker-compose.yml',
                        help='The name of the docker-compose to parse.')
    return parser.parse_args()


def as_json(filename):
    """
    Transform docker-compose as Python dict
    """
    file = yaml.Loader(open(os.getcwd() + '/' + filename).read())
    return file.get_single_data()


def find_pattern_in_service(service, compare):
    """
    Search corresponding element in diagram from service name
    """
    MATCH_DATA[service] = {}
    for key, data in compare.items():
        for item in data:
            if item.lower() in service.lower() or \
               service.lower() in item.lower():
                MATCH_DATA[service][key] = item
                # print('Pattern found on service', service, ':', item, 'in', key)


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
    """
    Search corresponding element in diagram from other service key
    """
    for key, data in compare.items():
        for item in data:
            if item.lower() in sub_key.lower() or \
               sub_key.lower() in item.lower():
                MATCH_DATA[service][key] = item
                # print('Pattern found on sub_key', sub_key, ':', item, 'in', key)


def match_other_data(service, service_data):
    """
    Complementary informations set in output
    """
    if 'ports' in service_data:
        MATCH_DATA[service]['ports'] = service_data['ports']
    if 'networks' in service_data:
        MATCH_DATA[service]['networks'] = service_data['networks']
    if 'depends_on' in service_data:
        MATCH_DATA[service]['depends_on'] = service_data['depends_on']
    # if 'restart' in serviceData:
    #     MATCH_DATA[service]['restart'] = serviceData['restart']
    # if 'volumes' in serviceData:
    #     MATCH_DATA[service]['volumes'] = serviceData['volumes']
    # if 'command' in serviceData:
    #     MATCH_DATA[service]['command'] = serviceData['command']


def build_match_data(yamldict_in):
    """
    Compare parsed docker-compose with compare.json dictionnary
    representing multiple class from diagram
    """
    with open('compare.json') as f:
        compare = json.loads(f.read())
        if 'services' in yamldict_in:
            # print('Starting matching services...')
            # Problem: if mutiple match, it replace previous one
            for service in yamldict_in['services']:
                # Find match from service name
                find_pattern_in_service(service, compare)

                set_links(service, yamldict_in['x-communication'])

                # In each service, find match from image name if exists
                if 'image' in yamldict_in['services'][service]:
                    find_pattern_in_sub_key(service, yamldict_in['services'][service]['image'], compare)

                # In each service, find match from container name if exists
                if 'container_name' in yamldict_in['services'][service]:
                    find_pattern_in_sub_key(service, yamldict_in['services'][service]['container_name'], compare)

                match_other_data(service, yamldict_in['services'][service])

    # Output used by other script
    print(json.dumps(MATCH_DATA, indent=4))


if __name__ == "__main__":
    args = main()
    yamldict = as_json(args.filename[0])
    build_match_data(yamldict)
