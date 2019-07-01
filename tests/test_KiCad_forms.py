# -*- coding: utf-8 -*-

from app.KiCad_tools import KiCad_format, KiCad_poly, KiCad_circle


def test_simple_circle():
    data = KiCad_circle(center=(0, 0), endpoint=(5, 5), layer='F.SilkS', width=0.001)
    approved = '(fp_circle (center 0.000000 0.000000) (end 5.000000 5.000000) (layer F.SilkS) (width 0.001))'
    assert (KiCad_format(data) == approved)


def test_simple_poly():
    x = (4**2 - 2**2)**0.5
    data = KiCad_poly([(0, -4), (-x, 2), (x, 2), (0, 0)], layer='F.Cu', width=0.002)
    approved = '(fp_poly (pts (xy 0.000000 -4.000000) (xy -3.464102 2.000000) (xy 3.464102 2.000000) (xy 0.000000 0.000000)) (layer F.Cu) (width 0.002))'
    assert (KiCad_format(data) == approved)