*Metodo P-R para traducción de lenguas muertas con morfología de raíz doble*

Repositorio oficial del Motor R² (2026) - Autor: Yansin Herrera, Santiago, Chile.

Este método resuelve el problema de la traducción inconsistente de jeroglíficos y lenguas muertas mediante una fórmula morfológica fija:

*Fórmula Base:* `P = [m- / n- / h3-] + R² + [-t / -w]`

*Donde R² es la raíz doble:*
- `d3d3` = temblar
- `qnqn` = golpear  
- `b3b3` = brotar
- `tnt3` = elevar / distinguir
- `skmkm` = cubrir / oscuridad
- `k3k3` = oscurecer

*Aporte Original del Autor (Inédito 2026):*
- `m-nmnm-t` = *Kc (Coeficiente de Construcción / Unión)*
- `n-hmhm-t` = *Dc (Coeficiente de Dispersión)*

Estas dos formas son creación original del autor y base del modelo cuantitativo.

*Ecuación de Evolución Poblacional-Lingüística:*
`P(t) = P0 * e^(Kc - Dc)t`

Donde la población y uso de una forma lingüística evoluciona según la diferencia entre construcción y dispersión.

*Contenido de este repo:*
- `/src/motor_r2_lector.py` - Código lector original que deriva de forma jeroglífica a Kc/Dc y calcula P(t)
- `README.md` - Documentación del método
- `LICENSE.md` - Licencia comercial

*Licencia:*
Uso académico gratuito citando este repositorio. Uso comercial, entrenamiento de IA, o apps requiere licencia pagada del autor.

Contacto: yansinherrera24@gmail.com
