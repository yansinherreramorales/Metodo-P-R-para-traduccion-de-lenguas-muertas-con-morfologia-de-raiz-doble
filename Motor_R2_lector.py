 # Motor R2 Predictivo - Metodo P-R
# Autor: Yansin Herrera 2026 - Santiago Chile
# yansinherrera24@gmail.com
# Repo: Metodo-P-R-para-traduccion-de-lenguas-muertas-con-morfologia-de-raiz-doble

# APORTE ORIGINAL 2026:
# Prediccion por raiz repetida: m-nmnm-t = Kc, n-hmhm-t = Dc
# Logica: Raiz doble = intensificacion morfologica

import re
from collections import Counter

def detectar_raiz_repetida(palabra):
    """Detecta raiz con duplicacion tipo nmnm, hmhm"""
    palabra = palabra.lower().strip()
    # Busca patron: letra + repeticion
    # Ej: m-nmnm-t -> detecta nmnm
    patron = re.search(r'(.)\1*([a-z]{2,})\2', palabra)
    if patron:
        return patron.group(2)
    # Busca repeticion directa nmnm, hmhm, etc
    for i in range(len(palabra)-3):
        par = palabra[i:i+2]
        if palabra[i+2:i+4] == par:
            return par+par
    return None

def predecir_por_raiz(palabra):
    """Motor que predice Kc/Dc por raiz repetida"""
    palabra = palabra.lower()
    raiz_repetida = detectar_raiz_repetida(palabra)
    
    # Base de conocimiento original 2026
    mapa_kc = ["mnmn", "nmnm", "nana", "mama"]
    mapa_dc = ["hmhm", "mh mh", "huhu", "mhmh"]
    
    # Limpia guiones
    limpia = palabra.replace("-", "")
    
    for raiz in mapa_kc:
        if raiz in limpia:
            return {
                "palabra": palabra,
                "raiz_detectada": raiz,
                "prediccion": "Kc",
                "significado": "Construccion / Union / Fijar",
                "confianza": 0.9
            }
    
    for raiz in mapa_dc:
        if raiz in limpia:
            return {
                "palabra": palabra,
                "raiz_detectada": raiz,
                "prediccion": "Dc",
                "significado": "Dispersion / Separacion / Expandir",
                "confianza": 0.9
            }
    
    return {
        "palabra": palabra,
        "raiz_detectada": raiz_repetida,
        "prediccion": "Desconocido",
        "significado": "No mapeado",
        "confianza": 0.0
    }

# Demo - Prueba de autoria 2026
if __name__ == "__main__":
    pruebas = ["m-nmnm-t", "n-hmhm-t", "m-nana-t", "s-hmhm-s"]
    for p in pruebas:
        resultado = predecir_por_raiz(p)
        print(f"{p} -> {resultado['prediccion']} ({resultado['significado']}) Raiz: {resultado['raiz_detectada']}")
