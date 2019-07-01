# -*- coding: utf-8 -*-


def KiCad_format(data):
    """
    Convert nested dictionary to KiCad s-expression string. Tuples considered as coordinates
    :param data: {'xy': (-9.712245, 9)}
    :return: '(xy -9.712245 9.000000)'
    """
    if isinstance(data, dict):
        res = []
        for key, value in data.items():
            res.append('({0} {1})'.format(key, KiCad_format(value)))
            return ' '.join(res)
    elif isinstance(data, tuple):
        # supposed we have coordinates here
        return ' '.join((format(float(item), '.6f') for item in data))
    elif isinstance(data, list):
        return ' '.join((KiCad_format(item) for item in data))
    else:
        return str(data)


def KiCad_circle(center=(0, 0), endpoint=(1, 1), layer='F.SilkS', width=0.001):
    """
    Create nested dict for KiCad circle.
    :param center: The position of the centre
    :param endpoint: The position of a point on the circle. The radius is calculated as the
distance of this point from the centre.
    :param layer: The name of the layer for the line
    :param width: The pen width.
    :return:
    """
    return {'fp_circle':
                [{'center': center},
                 {'end': endpoint},
                 {'layer': layer},
                 {'width': width}
                 ]
            }


def KiCad_poly(pts, layer='F.SilkS', width=0.001):
    """
    Create nested dict for KiCad polygon.
    :param pts: list of coordinates for polygon. Coordinates supposed to be in tuples, like (-16.2, -0.2)
    :param layer: The name of the layer for the line
    :param width: The pen width.
    :return:
    """
    pts_value = []
    for item in pts:
        assert isinstance(item, tuple)
        pts_value.append({'xy': item})

    return {'fp_poly':
                [{'pts': pts_value},
                 {'layer': layer},
                 {'width': width}
                 ]
            }
