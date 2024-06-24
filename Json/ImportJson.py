import json

def import_json_1():
    # Opening JSON file
    f = open('data_1.json')

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    # Iterating through the json
    # list
    for i in data['emp_details']:
        print(i)

    # Closing file
    f.close()

def import_json_2():
    f = '{"emp_name": "cris", "email": "cris@gmail.com", "job_profile": "intern"}'

    # returns JSON object as
    # a dictionary
    data = json.loads(f)

    # Iterating through the json
    # list
    print(data)
    print(data["emp_name"])
    print(data["email"])
    print(data["job_profile"])


if __name__ == '__main__':
    import_json_1()
    import_json_2()
