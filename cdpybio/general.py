import re
R_REGEX = re.compile('(.*):(.*)-(.*)')
R_REGEX_STRAND = re.compile('(.*):(.*)-(.*):(.*)')

def parse_region(region):
    """
    Parse region of type chr1:10-20 or chr1:10-20:+

    Parameters:
    -----------

    region : str
        Region of type chr1:10-20 or chr1:10-20:+.

    Returns
    -------
    groups : tuple
        Tuple of groups from regex e.g. (chr1, 10, 20) or (chr1, 10, 20, +).

    """
    m = R_REGEX_STRAND.search(region)
    if not m:
        m = R_REGEX.search(region)
    if m:
        groups = m.groups()
        return groups
    else:
        return None

def _sample_names(files, kwargs):
    """
    Make sample (or other) names.

    Parameters:
    -----------

    files : list of string
        Typically a list of file paths although could be any list of strings
        that you want to make names for. If neither names nor define_sample_name
        are provided, then files is returned as is.

    kwargs : dict
        kwargs from another function. Can include the following keys with
        appropriate arguments.

    names : list of strings
        Names to use. Overrides define_sample_name if provided.

    define_sample_name : function that takes string as input
        Function mapping string to name. For instance, you may have a sample
        name in a file path and use a regex to extract it.

    """
    if 'define_sample_name' not in kwargs.keys():
        define_sample_name = lambda x: x
    else:
        define_sample_name = kwargs['define_sample_name']
    
    if 'names' in kwargs.keys():
        names = kwargs['names']
    else:
        names = [define_sample_name(f) for f in files]
    
    assert len(names) == len(files)
    return names
