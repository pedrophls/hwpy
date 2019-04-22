def scan(direction):
    l_return = []
    if( "north" in direction):
        l_return.append(("direction", "north"))
    if( "south" in direction):
        l_return.append(("direction","south"))
    if( "east" in direction):
        l_return.append(("direction","east"))
    if( "west" in direction):
        l_return.append(("direction","west"))
    if( "go" in direction):
        l_return.append(("verb","go"))
    return l_return
    