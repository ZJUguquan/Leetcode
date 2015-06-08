
'''
So if it fits in the pixmap, the first four points will always be (0,0)->(q,q)->(q,0)->(0,q) with q = 2**n with a maximal n so that q still fits in the pixmap.

The second group will always be ->(p,p)->(q+p,q+p)->(q+p,p)->(p,q+p) with p = q / 2.

The third group will be ->(p,0)->(p+q,q)->(q+p,0)->(p,q).

The fourth group will be ->(0,p)->(q,q+p)->(q,p)->(0,q+p).
'''

def dithering(width, height):
    """yields coordinates in the given pixmap"""
