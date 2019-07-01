"""
Create specific form for KiCad
"""

def main():
    pass


def format_numbers(item):
    if isinstance(item, float):
        return format(item, )


def KiCad_format(data):
    if isinstance(data, dict):
        res = []
        for key, value in data.items():
            res.append('({0} {1})'.format(key, KiCad_format(value)))
            return ' '.join(res)
    elif isinstance(data, tuple):
        return ' '.join((str(item) for item in data))
    else:
        return str(data)



def KiCad_circle(center = (0, 0), endpoint = (1, 1), layer = 'F.SilkS', width = 1):
    output = 'fp_circle/n{}'


