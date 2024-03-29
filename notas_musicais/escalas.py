from enum import Enum


class ESCALAS(Enum):
    maior = (0, 2, 4, 5, 7, 9, 11)

NOTAS = 'C C# D D# E F F# G G# A A# B'.split()

def escalas(tonica: str, tonalidade: str) -> dict[str, list[str]]:
    """
    Gera uma escala apartir de uma nota tônica e uma tonalidade.

    Parameters:
       tonica: Nota que sera a tônica da escala
       tonalidade: Tonalidade da escala
    Returns:
       Um dicionário com as notas da escala e os graus
    Examples:
        >>> escalas('C', 'maior')
        {'notas': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

        >>> escalas('A', 'maior')
        {'notas': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
    """
    intervalos = ESCALAS[tonalidade].value
    tonica_pos = NOTAS.index(tonica)

    temp = []

    for intervalo in intervalos:
        nota = (tonica_pos + intervalo) % 12
        temp.append(NOTAS[nota])

    return {'notas': temp, 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
