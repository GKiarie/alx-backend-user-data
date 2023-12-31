import logging
import employee

logging.basicConfig(filename='sample.log', level=logging.DEBUG,
                     format='%(asctime)s:%(name)s:%(message)s')

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)

# formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

# file_handler = logging.FileHandler('sample.log')
# file_handler.setLevel(logging.ERROR)
# file_handler.setFormatter(formatter)

# stream_handler = logging.StreamHandler()
# stream_handler.setFormatter(formatter)

# logger.addHandler(file_handler)
# logger.addHandler(stream_handler)


def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    return x / y


num_1 = 10
num_2 = 5

add_result = add(num_1, num_2)
logging.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
logging.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
logging.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
logging.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result))