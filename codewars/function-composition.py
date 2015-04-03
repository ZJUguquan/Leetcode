def compose(f,g):
    # Compose the two functions here!
    return lambda *x: f(g(*x))