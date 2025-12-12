import csv
from datetime import datetime, date
from pathlib import Path


def leer_clientes(path='clientes.csv'):
    """Lee un CSV simple y devuelve una lista de dicts.

    Cada fila debe tener: Nombre,Telefono,MontoDeuda,FechaVencimiento (YYYY-MM-DD).
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
    """Retorna clientes con monto>0 y fecha de vencimiento pasada."""
    if referencia is None:
        referencia = date.today()
    return [c for c in clientes if c.get('MontoDeuda', 0) > 0 and c.get('FechaVencimiento') and c['FechaVencimiento'] < referencia]


def generar_factura(cliente, output_dir='facturas'):
    """Genera un TXT sencillo con la factura y devuelve la ruta (string)."""
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
