from datetime import datetime

records = [

    {'source': '48-996355555', 'destination': '48-666666666', 'end': 1564610974, 'start': 1564610674},

    {'source': '41-885633788', 'destination': '41-886383097', 'end': 1564506121, 'start': 1564504821},

    {'source': '48-996383697', 'destination': '41-886383097', 'end': 1564630198, 'start': 1564629838},

    {'source': '48-999999999', 'destination': '41-885633788', 'end': 1564697158, 'start': 1564696258},

    {'source': '41-833333333', 'destination': '41-885633788', 'end': 1564707276, 'start': 1564704317},

    {'source': '41-886383097', 'destination': '48-996384099', 'end': 1564505621, 'start': 1564504821},

    {'source': '48-999999999', 'destination': '48-996383697', 'end': 1564505721, 'start': 1564504821},

    {'source': '41-885633788', 'destination': '48-996384099', 'end': 1564505721, 'start': 1564504821},

    {'source': '48-996355555', 'destination': '48-996383697', 'end': 1564505821, 'start': 1564504821},

    {'source': '48-999999999', 'destination': '41-886383097', 'end': 1564610750, 'start': 1564610150},

    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564505021, 'start': 1564504821},

    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564627800, 'start': 1564626000}

]

DAY_TIME_TAX = 0.09

NIGHT_TIME_TAX = 0.0

PERMANENT_TAX = 0.36

DAY_TIME = 6

NIGHT_TIME = 22

MINUTE = 60


def calculate_tax(start, end):
    # Calculate tax for calls that started between 6am and 10pm

    if DAY_TIME <= start.hour < NIGHT_TIME:

        #  Calculate tax for calls that ended until 22pm

        if end.hour < NIGHT_TIME:
            # Connection time

            call = end - start

            # Calculate tax at each cycle of 60 sec.

            tax = PERMANENT_TAX + ((call.total_seconds() // MINUTE) * DAY_TIME_TAX)

            return tax

    else:

        # For night calls between 22pm and 6am

        return PERMANENT_TAX


def classify_by_phone_number(records):
    final_records = []

    new_dict = {}

    records = sorted(records, key=lambda k: k['source'])

    for record in records:

        source = record['source']

        start = datetime.fromtimestamp(record['start'])

        end = datetime.fromtimestamp(record['end'])

        tax = calculate_tax(start, end)

        if record['source'] not in new_dict.values():

            new_dict = {'source': source, 'total': round(tax, 2)}
            final_records.append(new_dict)

        else:

            new_dict['total'] += tax

    return sorted(final_records, key=lambda k: k['total'], reverse=True)
