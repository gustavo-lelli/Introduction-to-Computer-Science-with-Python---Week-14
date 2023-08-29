def soma_lista(vector):
    if len(vector) == 1:
        return vector[0]
    return vector[0] + soma_lista(vector[1:])
