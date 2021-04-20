import datetime
import json


class DateFormatEncoder(json.JSONEncoder):
    """
    Converts date and time data in JSON format using custom format:
    {
        "value": "01/02/1990 12:57:31",
        "__date__": true
    }
    """

    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return {
                'value': obj.strftime('%d/%m/%Y %H:%M:%S'),
                '__datetime__': True
            }
        elif isinstance(obj, datetime.date):
            return {
                'value': obj.strftime('%d/%m/%Y'),
                '__date__': True
            }
        return json.JSONEncoder.default(self, obj)


data = {
    'first_name': 'User_name',
    'last_name': 'User_lastname',
    'birthday': datetime.date(1986, 9, 29),
    'hired_at': datetime.datetime(2006, 9, 29, 12, 30, 5),
    'hobbies': [
        'guitar',
        'cars',
    ]
}

json_data = json.dumps(data, cls=DateFormatEncoder, indent=4)
print(json_data)

with open('data.json', 'w') as f:
    json.dump(data, f, cls=DateFormatEncoder)


def as_date_datetime(dct):
    """
    Converts date and time data in python type

    {
        "value": "01/02/1990 12:57:31",
        "__date__": true
    }
    to datetime(1990, 2, 1, 12, 57, 31)

    {
        "value": "01/02/1990",
        "__date__": true
    }
    to date(1990, 2, 1)
    """
    print(dct)
    if '__datetime__' in dct:
        return datetime.datetime.strptime(dct['value'], '%d/%m/%Y %H:%M:%S')
    if '__date__' in dct:
        return datetime.datetime.strptime(dct['value'], '%d/%m/%Y').date()
    return dct


with open('data.json', 'r') as f:
    data = json.load(f, object_hook=as_date_datetime)
    print(data)
