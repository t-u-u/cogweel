# -*- coding: utf-8 -*-
"""
Create specific form for KiCad
"""
import os
from app.KiCad_tools import KiCad_poly, KiCad_format
from app.calc_form import calc_cogs, pi


def main():
    cogs = []
    for cog in calc_cogs(6, 8, 6, 0.1, 100):
        cogs.append(KiCad_poly(cog, layer='F.Cu'))
    res = KiCad_format({'module Test\n': cogs})

    cur_path = os.path.dirname(os.path.realpath(__file__))
    output_file = os.path.join(os.path.dirname(cur_path), 'data')
    output_file = os.path.join(output_file, 'Tst.kicad_mod')
    with open(output_file, 'w') as f:
        f.write(res)


main()
