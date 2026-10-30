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
* **Uso Comercial / IA:** El uso comercial, entrenamiento de modelos de Inteligencia Artificial o integración en aplicaciones propietarias requiere una **licencia pagada** emitida directamente por el autor.r()
    print("Motor R² inicializado correctamente. Autor: Yansin Herrera (2026).")
