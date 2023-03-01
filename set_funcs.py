# TODO: convert to use Argparse library 
 
import sys, getopt, pprint as pp

def read_to_set(filename1, filename2):
    with open(filename1) as file1, open(filename2) as file2:
        items1, items2 = file1.readlines(), file2.readlines()
        return set(items1), set(items2)

def union(items1, items2):
    return sorted(items1.union(items2))

def intersection(items1, items2):
    return sorted(items1.intersection(items2))

def difference(items1, items2):
    return sorted(items1.difference(items2))

def symmetric_difference(items1, items2):
    return sorted(items1.symmetric_difference(items2))

def is_subset(items1, items2):
    return  sorted(items1.issubset(items2))

def is_superset(items1, items2):
    return sorted(items1.issuperset(items2))

def is_disjoint(items1, items2):
    return  sorted(items1.isdisjoint(items2))

def is_same(items1, items2):
    return (items1==items2)


if __name__ == "__main__":
    options, args = getopt.getopt(sys.argv[1:], 
                                    "uids",
                                    ["union",
                                        "intersection",
                                        "difference",
                                        "symmetric-difference",
                                        "is-subset",
                                        "is-superset",
                                        "is-disjoint",
                                        "is-same",  
                                        ])
    
    item_sets = read_to_set(*args)
    
    for opt, arg in options:
        match opt:
            case "--union":
                pp.pprint(union(*item_sets))
            case "-u":
                pp.pprint(union(*item_sets))
            case "--intersection":
                pp.pprint(intersection(*item_sets))
            case "-i":
                pp.pprint(intersection(*item_sets))
            case "--difference":
                pp.pprint(difference(*item_sets))
            case "-d":
                pp.pprint(difference(*item_sets))
            case "--symmetric-difference":
                pp.pprint(symmetric_difference(*item_sets))
            case "-s":
                pp.pprint(symmetric_difference(*item_sets))
            case "--is-subset":
                pp.pprint(is_subset(*item_sets))
            case "--is-superset":
                pp.pprint(is_superset(*item_sets))
            case "--is-disjoint":
                pp.pprint(is_disjoint(*item_sets))
            case "--is-same":
                pp.pprint(is_same(*item_sets))
                