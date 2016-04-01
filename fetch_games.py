import json


def get_from_local():
    field_list = ['data1.json', 'data2.json', 'data3.json', 'data4.json']
    result_set = []
    for file_name in field_list:
        with open('data/' + file_name) as data_file:
            result_set.extend(json.load(data_file)['results'])
    return result_set


if __name__ == '__main__':
    print len(get_from_local())
