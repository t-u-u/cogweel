# -*- coding: utf-8 -*-
"""
Create specific form for KiCad
"""
import os
from app.KiCad_tools import KiCad_poly, KiCad_format
from app.calc_form import calc_cog, pi


def main():
    cog_coords = calc_cog(6, 8, pi/6, pi/2, 0.1, 100)
    cog = KiCad_poly(cog_coords, layer='F.Cu')

    cur_path = os.path.dirname(os.path.realpath(__file__))
    output_file = os.path.join(os.path.dirname(cur_path), 'data')
    output_file = os.path.join(output_file, 'Tst.kicad_mod')
    with open(output_file, 'w') as f:
        f.write('(module Test\n')
        f.write(KiCad_format(cog))
        f.write('\n)')


main()
