# -*- coding: utf-8 -*-
"""
Create specific form for KiCad

Usage:
    main.py
    main.py -h --help   show this message

Arguments:
    <inner-radius>
"""
import os
from app.KiCad_tools import KiCad_poly, KiCad_format
from app.calc_form import calc_cogs, pi

# from app.KiCad_tools import KiCad_circle

def create_KiCad_file(inner_radius, outer_radius, module_name, output_file='', segment_count=6, nose_count=1, gap_width=0.1, precision=100, layer='F.Cu'):
    cogs = []
    for cog in calc_cogs(inner_radius, outer_radius, segment_count, nose_count=nose_count, gap_width=gap_width, precision=precision):
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


def main():
    pass


# create_KiCad_file(7,9, 'Test')