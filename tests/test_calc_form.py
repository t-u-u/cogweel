# -*- coding: utf-8 -*-

from app.calc_form import calc_arc, pi, pol2cart
from app.KiCad_tools import KiCad_poly, KiCad_format


def calc2KiCad(data):
    points = [pol2cart(r, theta) for r, theta in data]
    poly = KiCad_poly(points, layer='F.SilkS', width=0.001)
    return KiCad_format(poly)


def test_counter_clockwise_arc():
    data = calc_arc(radius=4, start_angle=pi/3, end_angle=2*pi/3, precision=5)
    data.append((0, 0))
    approved = '(fp_poly (pts (xy 1.236068 3.804226) (xy 0.418114 3.978088) (xy -0.418114 3.978088) (xy -1.236068 3.804226) (xy 0.000000 0.000000)) (layer F.SilkS) (width 0.001))'
    assert calc2KiCad(data) == approved


def test_clockwise_arc():
    data = calc_arc(radius=4, start_angle=2*pi/3, end_angle=pi/3, precision=5)
    data.append((0, 0))
    approved = '(fp_poly (pts (xy -1.236068 3.804226) (xy -0.418114 3.978088) (xy 0.418114 3.978088) (xy 1.236068 3.804226) (xy 0.000000 0.000000)) (layer F.SilkS) (width 0.001))'
    assert calc2KiCad(data) == approved


def test_counter_clockwise_raising_spiral():
    data = calc_arc(radius=4, end_radius=6, start_angle=pi/3, end_angle=2*pi/3, precision=5)
    data.append((0, 0))
    approved = '(fp_poly (pts (xy 1.359675 4.184649) (xy 0.501737 4.773705) (xy -0.543548 5.171514) (xy -1.730495 5.325916) (xy 0.000000 0.000000)) (layer F.SilkS) (width 0.001))'
    assert calc2KiCad(data) == approved


def test_counter_clockwise_descending_spiral():
    data = calc_arc(radius=6, end_radius=4, start_angle=0, end_angle=pi/3, precision=5)
    data.append((0, 0))
    approved = '(fp_poly (pts (xy 5.477627 1.164305) (xy 4.750436 2.115031) (xy 3.883282 2.821369) (xy 2.944175 3.269837) (xy 0.000000 0.000000)) (layer F.SilkS) (width 0.001))'
    assert calc2KiCad(data) == approved