import math


EPS = "<epsilon>"  # Define once. Use the same EPS everywhere
CHARS = list("abcdefghijklmnopqrstuvwxyz")
INFINITY = 1000000000


def calculate_arc_weight(frequency):
    """Function to calculate the weight of an arc based on a frequency count

    Args:
        frequency (float): Frequency count

    Returns:
        (float) negative log of frequency

    """
    # to varos mias metavashs, enos arc
    return -math.log(frequency)


def format_arc(src, dst, ilabel, olabel, weight=0):
    """Create an Arc, i.e. a line of an openfst text format file

    Args:
        src (int): source state
        dst (int): sestination state
        ilabel (str): input label 
        olabel (str): output label
        weight (float): arc weight

    Returns:
        (str) The formatted line as a string
    http://www.openfst.org/twiki/bin/view/FST/FstQuickTour#CreatingShellFsts
    """
    # ** To pipeline gia na spaei thn leksh kai na to petaei se arxeio k na to kanei compile. 
    return str(src) + " " + str(dst) + " " + ilabel + " " + olabel + " " + str(int(weight))
