import numpy as np

def hist(x_distr, cajas):
    """
    
    Input: Lista de valores siguiendo una distribucion especifica
           Numero de cajas deseadas
    Output: Valores del histograma que representa la distribucion:
            posicion y altura (normalizados en la integral) y errores de las alturas
    """

    alturas,posiciones = np.histogram(x_distr, cajas, density=True)
    N = len(x_distr)
    pos_med = []
    for i in range(cajas):
        pos_med.append(0.5*(posiciones[i]+posiciones[i+1]))
        
    anchura = pos_med[1]-pos_med[0]
    errores = []
    
    for i in range(cajas):
        error = (1./anchura)*np.sqrt(alturas[i]*anchura*(1-alturas[i]*anchura)/N)
        errores.append(error)
        
    return pos_med, alturas, errores