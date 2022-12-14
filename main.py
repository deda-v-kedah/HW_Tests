from pprint import pprint
from data import geo_logs, stats, random_list as data_list


def geo_logs_sort():
    num = 0
    for id, dict in enumerate(geo_logs):
        for key, value in dict.items():
            if value[1] != "Россия":
                geo_logs[id] = "del"
                num += 1
    while num > 0:
        geo_logs.remove("del")
        num -= 1
    return geo_logs


def max_stats():
    max_value = 0

    for key, value in stats.items():
        if max_value < value:
            max_value = value
            max_key = key
    return max_key


def list_to_dict(random_list):
    random_list.reverse()
    interim_dict = {}
    received_dict = {}
    i = 0

    while len(random_list) - 2 > i:
        i += 1

        if not interim_dict:
            interim_dict[random_list[i]] = random_list[i - 1]  
        else:
            interim_dict.clear()
            interim_dict = received_dict.copy()
            received_dict.clear()

        received_dict[random_list[i+1]] = interim_dict.copy()
    

    return received_dict



if __name__ == '__main__':
    geo_logs_sort()
    max_stats()
    list_to_dict(data_list)
