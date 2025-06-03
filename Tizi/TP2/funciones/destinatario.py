def validar_destinatario(id_destinatario):
    """
    Se comprueba que el destinatario sea valido o este escrito de manera correcta y no este vacio

    Args:
        id_destinatario (string): Id del destinatario

    Returns:
        Booleano: True si la id de destinatario es correcta, False si no lo es o tiene caracteres invalidos
    """
    if not id_destinatario: # Si no esta definido o esta vacio, devuelve False
        return False

    caracteres_validos = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-" # Caracteres validos

    for caracter in id_destinatario:
        if caracter not in caracteres_validos:
            return False

    return True