import datetime

def get_date(date_str):
    format_str = '%Y-%m-%d' # The format
    return datetime.datetime.strptime(date_str, format_str)