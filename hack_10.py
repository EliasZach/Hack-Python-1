"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    result = result.replace('o','0').replace('i','1').replace('a','@')
    lista = [i.upper() for i in result]
    return lista  