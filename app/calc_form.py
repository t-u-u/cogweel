from numpy import cos, sin, pi


def pol2cart(r, theta):
    """
    Conversion from polar coordinates to cartesian
    :param r: 2
    :param theta: pi/3
    :return: (1.73205080756887721, 1)
    """
    x = r*cos(theta)
    y = r*sin(theta)
    return (x, y)


def calc_cogs(inner_radius, outer_radius, segment_count=6, precision=10):
    pass


def calc_arc(radius=1, end_radius=None, start_angle=0, end_angle=1, precision=10):
    """
    Generate points for a circular arc or Archimedean spiral
    If end_radius is omitted, circular arc would be calculated.
    Start and end points are not included in result
    :param radius:
    :param end_radius:
    :param start_angle:
    :param end_angle:
    :param precision:
    :return: list of points (tuples) in polar coordinates
    """
    assert precision > 0

    arc = []

    radius_step = 0
    if end_radius:
        radius_step = (end_radius - radius) / precision

    angle_step = (end_angle - start_angle)/precision

    for i in range(1, precision):
        arc.append((radius + i*radius_step, start_angle + i*angle_step))

    return arc



def calc_cog(inner_radius, outer_radius, start_angle, end_angle, gap_width, precision: int):
    """
    Generate points for one segment depending on given angles and radius.
    :param inner_radius:
    :param outer_radius:
    :param start_angle:
    :param gap_width: radians!!!
    :param end_angle:
    :param precision:
    :return:
    """
    assert outer_radius > inner_radius
    assert end_angle > start_angle
    assert precision > 0

    cog_polar_points = []

    #TODO: recalculate gap_radians from gap width to actual radians
    outer_gap_radians = gap_width
    middle_gap_radians = gap_width
    inner_gap_radians = gap_width

    middle_radius = inner_radius + (outer_radius - inner_radius) / 2
    middle_angle = start_angle + (end_angle - start_angle) / 2

    start_nose_angle = start_angle + middle_gap_radians
    start_side_angle = middle_angle + outer_gap_radians
    end_side_angle = end_angle + (end_angle - start_angle) / 2

    # nose point
    cog_polar_points.append((middle_radius, start_nose_angle))

    # nose outer arc
    arc = calc_arc(radius=middle_radius, end_radius=outer_radius - gap_width, start_angle=start_nose_angle, end_angle=start_side_angle, precision=precision)
    cog_polar_points.extend(arc)

    # outer side start points
    cog_polar_points.append((outer_radius - gap_width, start_side_angle))
    cog_polar_points.append((outer_radius, start_side_angle))

    # outer side arc
    arc = calc_arc(radius=outer_radius, start_angle=start_side_angle,
                   end_angle=end_side_angle, precision=2*precision)
    cog_polar_points.extend(arc)

    # outer side end point
    cog_polar_points.append((outer_radius, end_side_angle))

    # outer tail arc
    arc = calc_arc(radius=outer_radius, end_radius=middle_radius - gap_width, start_angle=end_side_angle,
                   end_angle=end_angle, precision=precision)
    cog_polar_points.extend(arc)

    # tail middle points
    cog_polar_points.append((middle_radius + gap_width, end_angle))
    cog_polar_points.append((middle_radius - gap_width, end_angle))

    # inner tail arc
    arc = calc_arc(radius=middle_radius - gap_width, end_radius=inner_radius, start_angle=end_angle,
                   end_angle=end_side_angle, precision=precision)
    cog_polar_points.extend(arc)

    # inner side start point
    cog_polar_points.append((inner_radius, end_side_angle))

    # inner side arc
    arc = calc_arc(radius=inner_radius, start_angle=end_side_angle,
                   end_angle=start_side_angle, precision=2*precision)
    cog_polar_points.extend(arc)

    # inner side end points
    cog_polar_points.append((inner_radius, start_side_angle))
    cog_polar_points.append((inner_radius + gap_width, start_side_angle))

    # nose inner arc
    arc = calc_arc(radius=inner_radius + gap_width, end_radius=middle_radius, start_angle=start_side_angle,
                   end_angle=start_nose_angle, precision=precision)
    cog_polar_points.extend(arc)

    # cog_polar_points.append((0, 0))

    result = [tuple(pol2cart(r, theta)) for (r, theta) in cog_polar_points]
    return result
