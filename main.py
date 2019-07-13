# -*- coding: utf-8 -*-
"""
Create specific form for KiCad Footprint

Usage:
    main.py <inner-radius> <outer-radius> [options]
    main.py -h --help           Show help message

Arguments:
    <inner-radius>  inner radius of the wheel
    <outer-radius>  outer radius of the wheel

Options:
    -o --output <file>          path to output file, %scrit_path%\\data\\cogwheel.kicad_mod by default
    -m --module <module>        name of created KiCad module
    -s --segments <segments>    number of segments on the wheel, 6 by default
    -n --noses <noses>          [NOT SUPPORTED] number of noses for each segment, 1 by default
    -g --gap-width <gap-width>  width of the gap between segments, 0.1 by default
    -p --precision <precision>  how many dots on the element would be used for approximation
    -l --layer <layer>          name of KiCad layer, 'F.Cu' by default

"""
import os
from docopt import docopt
from app.KiCad_tools import KiCad_poly, KiCad_format
from app.calc_form import calc_cogs


def create_KiCad_file(args):
    inner_radius = args.get('<inner-radius>')
    outer_radius = args.get('<outer-radius>')
    module_name = args.get('--module', '')
    output_file = args.get('--output', 'cogwheel.kicad_mod')
    segment_count = args.get('--segments', 6)
    nose_count = args.get('--noses', 1)
    gap_width = args.get('--gap-width', 0.1)
    precision = args.get('--precision', 100)
    layer = args.get('--layer', 'F.Cu')

    print(output_file)
    print('_______________________________')

    cogs = []
    for cog in calc_cogs(inner_radius, outer_radius, segment_count=segment_count, nose_count=nose_count, gap_width=gap_width, precision=precision):
        cogs.append(KiCad_poly(cog, layer=layer))
    # cogs.append(KiCad_circle(center=(0, 0), endpoint=(0, 7), layer='F.SilkS', width=0.001))
    res = KiCad_format({'module {0}\n'.format(module_name): cogs})

    if not os.path.basename(output_file):
        output_file = os.path.join(os.path.dirname(output_file), 'cogwheel.kicad_mod')

    if not os.path.dirname(output_file):
        cur_path = os.path.dirname(os.path.realpath(__file__))
        output_file = os.path.join(os.path.join(cur_path, 'data'), os.path.basename(output_file))

    directory = os.path.dirname(output_file)
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(output_file, 'w') as f:
        f.write(res)


def parse_args():
    args = docopt(__doc__)
    print(args)
    string_params = ['--module', '--output', '--layer']
    float_params = ['<inner-radius>', '<outer-radius>', '--gap-width']
    int_params = ['--segments', '--noses', '--precision']

    res = {p: args[p] for p in string_params}

    for k in float_params:
        try:
            if args[k]:
                v = float(args[k])
                res[k] = v
            # else:
            #     res[k] = None
        except TypeError:
            print("Argument '{0}' is '{1}', but should be float".format(k, v))
            quit()

    for k in int_params:
        try:
            if args[k]:
                v = int(args[k])
                res[k] = v

        except TypeError:
            print("Argument '{0}' is '{1}', but should be integer".format(k, v))
            quit()

    return res

def main():
    args = parse_args()
    print(args)
    create_KiCad_file(args)

# create_KiCad_file(7,9, 'Test')
if __name__ == '__main__':
    main()
