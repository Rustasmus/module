from get_data import get_data


def validate_data():
    get_data_list = get_data()
    datas = []
    for data in get_data_list:
        if data.isdigit():
            datas.append(int(data))
            print(datas)

        else:
            print(f'Enter not valid {data}')
            return
    return datas
