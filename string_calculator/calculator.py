
def add(string):
    string_numbers = split_string(string)

    numbers = []
    negative_numbers = []
    for each in string_numbers:
        try:
            number = int(each)
        except:
            number = 0

        if number < 0:
            negative_numbers.append(number)
        numbers.append(number)

    if negative_numbers:
        message = ','.join([str(number) for number in negative_numbers])
        raise NegativesNotAllowedError(message)

    return sum(numbers)

def split_string(string):
    delimiter = ','
    if string.startswith('//' or '[***]' or '***'):
        delimiter = string[2]

        string = string[3:]
    
    string = string.replace('\n', delimiter)
    string_numbers = string.split(delimiter)
    return string_numbers

def NegativesNotAllowedError(Exception):
    pass


print(add('[***]1,2,3,4,5'))