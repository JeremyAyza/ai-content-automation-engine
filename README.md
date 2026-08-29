# Generate Videos CLI

CLI automatizado para generar y subir videos cortos (`short`) y largos (`long`).

## Instalación Global

Asegúrate de estar en el directorio raíz del proyecto y corre:
```bash
npm install -g .
```

## Uso Básico
El comando principal ahora es `gen`.

### Comandos de Generación
- `gen short new` : Genera un nuevo video (ejecuta todo el pipeline desde el paso 1 hasta el final).
- `gen short s1` : Ejecuta solo un paso específico (puedes usar `s1`, `s2`, `s3`, `s4`, `s5`, `s6`, `s7`, `fixed`, `all`).

### Comando de Subida
- `gen short up` : Ejecuta el script de subida (`upload_youtube.py`) para el primer video pendiente.

### Multiplicadores (Repetición en bucle)
Puedes agregar `x[n]` al final de cualquier comando para ejecutarlo `n` veces automáticamente. ¡Ideal para automatizar lotes!

**Ejemplos prácticos:**
- `gen short new x3` : Genera **3 videos nuevos** de corrido.
- `gen short up x5` : Sube **5 videos pendientes** seguidos a YouTube.
- `gen short s1 x10` : Ejecuta el paso 1 (creación de ideas) 10 veces consecutivas.
