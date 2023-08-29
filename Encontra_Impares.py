def encontra_impares(vector, new_vector=None):
    if new_vector == None:
        new_vector = []
        
    if len(vector) == 0:
        return new_vector
    elif vector[0] % 2 == 1:
        new_vector.append(vector[0])
        return encontra_impares(vector[1:], new_vector)
    else:
        return encontra_impares(vector[1:], new_vector)
