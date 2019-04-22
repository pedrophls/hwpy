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
    if( "kill" in direction):
        l_return.append(("verb","kill"))
    if( "eat" in direction):
        l_return.append(("verb","eat"))
    if( "the" in direction):
        l_return.append(("stop","the"))
    if( "in" in direction):
        l_return.append(("stop","in"))
    if( "of" in direction):
        l_return.append(("stop","of"))
    return l_return
    