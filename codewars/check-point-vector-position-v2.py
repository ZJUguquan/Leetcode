

def point_vs_vector_v2((px, py), ((vbx, vby), (vex, vey))):
    if vbx == vex and vby == vey:
        return None
    cp = (vex - vbx) * (py - vby) - (px - vbx) * (vey - vby)
    if abs(cp) < 10 ** -9:
        return 0
    return (cp < 0) - (cp > 0)