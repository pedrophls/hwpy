def scan(palavra):
    l_return = []
    palavras_separadas = palavra.split(' ')
    if( "north" in palavras_separadas):
        l_return.append(("direction", "north"))
    if( "south" in palavras_separadas):
        l_return.append(("direction","south"))
    if( "east" in palavras_separadas):
        l_return.append(("direction","east"))
    if( "west" in palavras_separadas):
        l_return.append(("direction","west"))
    if( "go" in palavras_separadas):
        l_return.append(("verb","go"))
    if( "kill" in palavras_separadas):
        l_return.append(("verb","kill"))
    if( "eat" in palavras_separadas):
        l_return.append(("verb","eat"))
    if( "the" in palavras_separadas):
        l_return.append(("stop","the"))
    if( "in" in palavras_separadas):
        l_return.append(("stop","in"))
    if( "of" in palavras_separadas):
        l_return.append(("stop","of"))
    if( "bear" in palavras_separadas):
        l_return.append(("noun","bear"))
    if( "princess" in palavras_separadas):
        l_return.append(("noun","princess"))
    for x in palavras_separadas :
        if x.isnumeric():
            l_return.append(("number", int(x)))
    if "ASDFADFASDF" in palavras_separadas :
        l_return.append(("error", "ASDFADFASDF"))
    if "IAS" in palavras_separadas :
        l_return.append(("error", "IAS"))


    return l_return