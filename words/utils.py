from .models import Abbreviation


def read_simple_abbr_list(file):
    """reads a text file which one abbrevation per line
    and returns a python dict with the abbreviations"""
    with open(file, 'r', encoding='UTF-8') as f:
        content = f.readlines()
    if len(content) > 0:
        content = [x.strip() for x in content if not x.startswith('#')]
        result = {
            'list': content,
            'number_of_words': len(content)
        }
        return result
    else:
        None


def save_simple_abbr_list(file, verbose=True):
    """reads a text file which one abbrevation per line
    and saves them as Abbreviation objects"""
    abbrlist = read_simple_abbr_list(file)
    if abbrlist:
        abbr_objects = []
        for x in abbrlist['list']:
            temp_abbr, _ = Abbreviation.objects.get_or_create(
                orth=x
            )
            abbr_objects.append(temp_abbr)
            if verbose:
                print("{}".format(temp_abbr))
        return abbr_objects, abbrlist
    else:
        return None
