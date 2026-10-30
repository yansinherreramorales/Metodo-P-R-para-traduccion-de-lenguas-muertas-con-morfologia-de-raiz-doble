# Motor R²: Método P-R para Traducción de Lenguas Muertas

**Repositorio Oficial (2026)**  
**Autor:** Yansin Herrera (Santiago, Chile)  

---

## Descripción del Proyecto

El **Método P-R** (Raíz Doble más Sujeto y Prefijo) resuelve el problema de la traducción inconsistente en jeroglíficos y lenguas muertas mediante la implementación de una fórmula morfológica fija y un modelo cuantitativo de evolución lingüística.

### 1. Fórmula Base
La estructura morfológica fundamental del sistema se define como:

$$P = [m\text{-} \mid n\text{-} \mid h_3\text{-}] + R^2 + [\-t \mid \-w]$$

Donde **$R^2$** representa la raíz doble documentada:
* `d3d3` $\rightarrow$ Temblar
* `qnqn` $\rightarrow$ Golpear
* `b3b3` $\rightarrow$ Brotar
* `tnt3` $\rightarrow$ Elevar / Distinguir
* `skmkm` $\rightarrow$ Cubrir / Oscuridad
* `k3k3` $\rightarrow$ Oscurecer

### 2. Aportes Originales (Inédito 2026)
Este modelo introduce dos coeficientes cuantitativos originales para el análisis morfológico:
* **$m\text{-}nmnm\text{-}t$ ($K_c$):** Coeficiente de Construcción / Unión.
* **$n\text{-}hmhm\text{-}t$ ($D_c$):** Coeficiente de Dispersión.

### 3. Ecuación de Evolución Poblacional-Lingüística
La viabilidad, uso y evolución temporal de una forma lingüística dentro de una población se modela mediante la siguiente ecuación diferencial:

$$P(t) = P_0 \cdot e^{(K_c - D_c)t}$$

---

## Estructura del Repositorio

* `src/motor_r2_lector.py`: Código lector original que procesa formas jeroglíficas, deriva los coeficientes $K_c$ y $D_c$, y calcula $P(t)$.
* `LICENSE.md`: Términos y condiciones de uso académico y comercial.

---

## Licencia y Derechos de Autor

* **Uso Académico:** Gratuito, sujeto a la citación obligatoria de este repositorio y del autor (Yansin Herrera).
* **Uso Comercial / IA:** El uso comercial, entrenamiento de modelos de Inteligencia Artificial o integración en aplicaciones propietarias requiere una **licencia pagada** emitida directamente por el autor.
3. Estructura base para src/motor_r2_lector.py
Una base limpia en Python para que el script comience a operar bajo la lógica que diseñaste:

Python
"""
Motor R² - Lector Morfológico y Evolutivo (Método P-R)
Autor: Yansin Herrera (Santiago, Chile, 2026)
Licencia: Académica gratuita / Comercial bajo licencia del autor.
"""

import math

class MotorR2Lector:
    def __init__(self):
        # Diccionario de raíces dobles soportadas
        self.raices_dobles = {
            "d3d3": "temblar",
            "qnqn": "golpear",
            "b3b3": "brotar",
            "tnt3": "elevar / distinguir",
            "skmkm": "cubrir / oscuridad",
            "k3k3": "oscurecer"
        }
        
        # Prefijos y sufijos válidos según la Fórmula Base
        self.prefijos_validos = ["m-", "n-", "h3-"]
        self.sufijos_validos = ["-t", "-w"]

    def validar_forma_base(self, prefijo: str, raiz: str, sufijo: str) -> bool:
        """Valida que la estructura cumpla con la Fórmula Base P."""
        return (prefijo in self.prefijos_validos and 
                raiz in self.raices_dobles and 
                sufijo in self.sufijos_validos)

    def calcular_coeficientes(self, forma_analizada: str) -> dict:
        """
        Deriva de forma jeroglífica los coeficientes de Construcción (Kc) 
        y Dispersión (Dc) según los aportes originales del autor.
        """
        # Lógica propietaria de derivación basada en morfología
        # (Ejemplo preliminar sujeto a tu implementación algorítmica específica)
        kc = forma_analizada.count("nmnm") * 1.5 + 0.8
        dc = forma_analizada.count("hmhm") * 1.2 + 0.5
        return {"Kc": kc, "Dc": dc}

    def evolucion_poblacional(self, p0: float, kc: float, dc: float, t: float) -> float:
        """
        Calcula la Ecuación de Evolución Poblacional-Lingüística:
        P(t) = P0 * e^(Kc - Dc)t
        """
        exponent = (kc - dc) * t
        return p0 * math.exp(exponent)

# Ejemplo de uso rápido
if __name__ == "__main__":
    motor = MotorR2Lector()
    print("Motor R² inicializado correctamente. Autor: Yansin Herrera (2026).")
