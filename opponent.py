import random
OpponentRelaxationLevel = [77223576, 95788951,93504189, 443234095, 99555635, 78291697, 75539833, 190897708, 32324690471, 102499099, 71863821, 94696463, 91911430, 113006834, 81249800, 111177291657, 111192456414, 111190197708, 1111165124284, 111196499099, 11168412011, 111106696463, 11195464637, 11116834, 1111911084, 11111657, 111120663, 111197708, 1111176306, 111199099, 111133433, 111196463, 111164637, 111196463, 111194464637, 1111123006834, 111185911084, 111179291657, 111195420663, 111190897708, 1111125176306, 111192499099, 111177733433, 111196696463, 111194464637, 1230068341111, 111185911084, 1111799291657, 1111905420663, 1111100897708, 1111225176306, 111192499099, 111177733433, 111196696463, 1111104464637, 1111123006834, 859110841111, 111179291657, 111195420663, 111190897708]
index = -1

def GetOpponentRelaxationLevel():
    global index
    index += 1
    return OpponentRelaxationLevel[index%len(OpponentRelaxationLevel)]
