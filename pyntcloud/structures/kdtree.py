#  HAKUNA MATATA

"""
KDTree Class extending cKDTree
"""


from scipy.spatial import cKDTree

class KDTree(cKDTree):
    # TODO instead of extend cKDTree make this class a wrapper
    # around different KDTree implementations: scipy, pyflann, etc.

    def __init__(self, points, leafsize=16):
        super().__init__(points)

        self.id = "{}|leafsize: {}".format("scipy's kdtree", self.leafsize)

    def __repr__(self):

        return self.id