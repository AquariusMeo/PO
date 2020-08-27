import yaml


def get_data(test_data):
    with open('./data/' + test_data + '.yml', 'r') as f:
        return yaml.load(f)
