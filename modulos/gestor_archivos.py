import csv
from datetime import datetime, date
from pathlib import Path


def leer_clientes(path='clientes.csv'):
    """Lee un CSV simple y devuelve lista de dicts.

    Cada fila entrega: Nombre, Telefono, MontoDeuda, FechaVencimiento (YYYY-MM-DD).
    Fechas inválidas se convierten en `None` y montos inválidos en 0.0.
    """
    clientes = []
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            nombre = (row.get('Nombre') or '').strip()
            telefono = (row.get('Telefono') or '').strip()
            try:
                monto = float((row.get('MontoDeuda') or '0').strip())
            except Exception:
                monto = 0.0
            fecha_txt = (row.get('FechaVencimiento') or '').strip()
            try:
                fecha = datetime.strptime(fecha_txt, '%Y-%m-%d').date()
            except Exception:
                fecha = None
            clientes.append({
                'Nombre': nombre,
                'Telefono': telefono,
                'MontoDeuda': monto,
                'FechaVencimiento': fecha,
            })
    return clientes


def clientes_vencidos(clientes, referencia=None):
    """Devuelve clientes con `MontoDeuda` > 0 y `FechaVencimiento` anterior a `referencia`."""
    if referencia is None:
        referencia = date.today()
    return [c for c in clientes if c.get('MontoDeuda', 0) > 0 and c.get('FechaVencimiento') and c['FechaVencimiento'] < referencia]


def generar_factura(cliente, output_dir='facturas'):
    """Genera un TXT sencillo con la factura y devuelve la ruta como string."""
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    nombre = cliente.get('Nombre') or 'cliente'
    safe = ''.join(ch if ch.isalnum() else '_' for ch in nombre).strip('_') or 'cliente'
    archivo = out / f'factura_{safe}.txt'
    texto = (
        '===== FACTURA =====\n'
        f"Cliente: {cliente.get('Nombre')}\n"
        f"Telefono: {cliente.get('Telefono')}\n"
        f"Fecha vencimiento: {cliente.get('FechaVencimiento') or ''}\n"
        f"Monto adeudado: ${cliente.get('MontoDeuda'):.2f}\n"
        '===================\n'
    )
    archivo.write_text(texto, encoding='utf-8')
    return str(archivo)
import csv
from datetime import datetime
from pathlib import Path

def leer_clientes_csv(ruta_csv: str):
    """
    Lee clientes.csv y retorna una lista de dicts:
    [{Nombre, Telefono, MontoDeuda, FechaVencimiento}, ...]
    """
    clientes = []
    with open(ruta_csv, newline="", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        esperadas = ["Nombre", "Telefono", "MontoDeuda", "FechaVencimiento"]
        if lector.fieldnames is None or list(lector.fieldnames) != esperadas:
            raise ValueError(f"Estructura CSV inválida. Debe ser exactamente: {', '.join(esperadas)}")

        for fila in lector:
            try:
                clientes.append({
                    "Nombre": fila["Nombre"].strip(),
                    "Telefono": fila["Telefono"].strip(),
                    "MontoDeuda": float(fila["MontoDeuda"]),
                    "FechaVencimiento": datetime.strptime(fila["FechaVencimiento"].strip(), "%Y-%m-%d").date(),
                })
            except Exception as e:
                print(f"[WARN] Fila inválida: {fila} Motivo: {e}")
                continue
    return clientes

def filtrar_deudores_vencidos(clientes):
    """
    Retorna clientes con MontoDeuda > 0 y FechaVencimiento < hoy.
    """
    hoy = datetime.today().date()
    return [c for c in clientes if c["MontoDeuda"] > 0 and c["FechaVencimiento"] < hoy]

def generar_facturas_txt(deudores):
    """
    Genera factura_[Nombre].txt con formato legible, dentro de la carpeta 'facturas'.
    """
    carpeta = Path("facturas")
    import csv
    from datetime import datetime, date
    from pathlib import Path


    def leer_clientes(path='clientes.csv'):
        """Lee el CSV y devuelve una lista de dicts simples.

        Cada fila produce: {'Nombre','Telefono','MontoDeuda','FechaVencimiento'}.
        Fecha esperada: YYYY-MM-DD (si falla, se guarda None).
        """
        clientes = []
        with open(path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                nombre = (row.get('Nombre') or '').strip()
                telefono = (row.get('Telefono') or '').strip()
                try:
                    monto = float((row.get('MontoDeuda') or '0').strip())
                except Exception:
                    monto = 0.0
                fecha_text = (row.get('FechaVencimiento') or '').strip()
                try:
                    fecha = datetime.strptime(fecha_text, '%Y-%m-%d').date()
                except Exception:
                    fecha = None
                clientes.append({
                    'Nombre': nombre,
                    'Telefono': telefono,
                    'MontoDeuda': monto,
                    'FechaVencimiento': fecha,
                })
        return clientes


    def clientes_vencidos(clientes, referencia=None):
        """Devuelve los clientes con monto>0 y fecha de vencimiento pasada."""
        if referencia is None:
            referencia = date.today()
        return [c for c in clientes if c.get('MontoDeuda', 0) > 0 and c.get('FechaVencimiento') and c['FechaVencimiento'] < referencia]


    def _sanitize_name(nombre: str) -> str:
        if not nombre:
            return 'cliente'
        return ''.join(ch if ch.isalnum() else '_' for ch in nombre).strip('_') or 'cliente'


    def generar_factura(cliente, output_dir='facturas'):
        """Crea un archivo TXT sencillo con la factura y devuelve la ruta (string)."""
        out = Path(output_dir)
        out.mkdir(parents=True, exist_ok=True)
        nombre_arch = f"factura_{_sanitize_name(cliente.get('Nombre'))}.txt"
        ruta = out / nombre_arch
        lines = [
            '===== FACTURA =====',
            f"Cliente: {cliente.get('Nombre')}",
            f"Telefono: {cliente.get('Telefono')}",
            f"Fecha vencimiento: {cliente.get('FechaVencimiento') or ''}",
            f"Monto adeudado: ${cliente.get('MontoDeuda'):.2f}",
            '===================',
        ]
        ruta.write_text('\n'.join(lines), encoding='utf-8')
        return str(ruta)
