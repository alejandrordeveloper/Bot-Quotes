
# Bot-Cobranza

Proyecto simple para una pequeña empresa de servicios (ej. internet o gimnasio) que:

- Lee clientes desde un CSV.
- Detecta deudores con facturas vencidas.
- Genera un archivo `factura_[Nombre].txt` por deudor en la carpeta `facturas`.
- Intenta notificar por WhatsApp usando `pywhatkit`.

**Requisitos**

- Python 3.8+
- Instalar dependencias:

```bash
pip install -r requirements.txt
```

**Archivos principales**

- **`main.py`**: orquesta el flujo (lectura, generación y notificaciones). Ver: [main.py](main.py)
- **`modulos/gestor_archivos.py`**: lectura de CSV, filtrado de vencidos y generación de facturas. Ver: [modulos/gestor_archivos.py](modulos/gestor_archivos.py)
- **`modulos/notificaciones.py`**: envíos por WhatsApp con `pywhatkit`. Ver: [modulos/notificaciones.py](modulos/notificaciones.py)
- **`clientes.csv`**: entrada de datos (ver formato abajo).

**Formato `clientes.csv`**

La primera línea debe ser la cabecera exacta::

```
Nombre,Telefono,MontoDeuda,FechaVencimiento
```

- `Nombre`: nombre completo del cliente.
- `Telefono`: número con prefijo internacional (ej: `+5215550001111`).
- `MontoDeuda`: número (ej: `1500.50`).
- `FechaVencimiento`: `YYYY-MM-DD`.

Ejemplo mínimo:

```
Nombre,Telefono,MontoDeuda,FechaVencimiento
Juan Perez,+5215550001111,1500.50,2025-11-01
Maria Lopez,+5215550002222,0,2026-01-15
```

**Ejecutar**

1. Prueba segura (no abre WhatsApp):

```powershell
$env:DRY_RUN='1'
python main.py
```

2. Ejecución normal (abrirá WhatsApp Web para enviar mensajes):

```powershell
python main.py
```

**Notas importantes**

- La primera vez que `pywhatkit` abra WhatsApp Web deberás escanear el QR con tu teléfono.
- Si no quieres que el programa intente enviar mensajes, usa `DRY_RUN=1` como se muestra arriba.
- El programa maneja CSV faltantes o filas inválidas sin colapsar; las facturas se generan en la carpeta `facturas`.

Si quieres, puedo:

- Añadir un `clientes.csv` de ejemplo realista.
- Ejecutar una prueba `DRY_RUN` desde aquí y pegar la salida.
- Limpiar archivos o duplicados en la carpeta del proyecto.

