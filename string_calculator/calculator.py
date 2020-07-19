import re


def add(numbers):
    if '' == numbers:
        return 0
    else:
        integers = parse(numbers)
        check_for_negatives(integers)
        return sum([i for i in integers if i < 1001])


def check_for_negatives(integers):
    negatives = [n for n in integers if n < 0]
    if len(negatives) > 0:
        raise RuntimeError('negatives not allowed ' + str(negatives))


def parse(numbers):
    tokens = tokenize(numbers)
    return [int(x) for x in tokens]


def tokenize(numbers):
    delimiters, numbers = delimiters_and_numbers(numbers)
    return re.split(delimiters, numbers)


def delimiters_and_numbers(numbers):
    match = re.compile('//(.+)\n(.+)').match(numbers)
    if match:
        return (generate_delimiters_regex(match.group(1)), match.group(2))
    else:
        return (',|\n', numbers)


def generate_delimiters_regex(delimiters_definition):
    if delimiters_definition[0] == '[' and delimiters_definition[-1] == ']':
        delimiters = re.findall('\[([^\[\]]+)\]', delimiters_definition)
        return '|'.join(re.escape(d) for d in delimiters)
    else:
        return re.escape(delimiters_definition)

print(add('1,1002\n3'))