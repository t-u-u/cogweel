# cogwheel

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
