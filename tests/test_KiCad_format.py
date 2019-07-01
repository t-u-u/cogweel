# -*- coding: utf-8 -*-

from app.KiCad_tools import KiCad_format


def test_one_point():
    data = {'xy': (-9.712245, 9.000000)}
    approved = '(xy -9.712245 9.000000)'
    assert(KiCad_format(data) == approved)


def test_polygon():
    data = {'fp_poly':
                [{'pts': [{'xy': (-16.2, -0.2)}, {'xy': (-16.8, 0.2)}, {'xy': (-16.8, 9)}, {'xy': (-16.2, 9.0)}]},
                 {'layer': 'F.Cu'},
                 {'width': 0.001}]
            }
    approved = '(fp_poly (pts (xy -16.200000 -0.200000) (xy -16.800000 0.200000) (xy -16.800000 9.000000) (xy -16.200000 9.000000)) (layer F.Cu) (width 0.001))'
    assert (KiCad_format(data) == approved)


def test_circle():
    data = {'fp_circle':
                [{'center': (0, 0)},
                 {'end': (5, 5)},
                 {'layer': 'F.SilkS'},
                 {'width': 0.002}
                 ]
            }
    approved = '(fp_circle (center 0.000000 0.000000) (end 5.000000 5.000000) (layer F.SilkS) (width 0.002))'
    assert (KiCad_format(data) == approved)