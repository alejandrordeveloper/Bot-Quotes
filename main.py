"""Programa principal del sistema de cobranza.
Este archivo es intencionalmente simple y legible para un desarrollador junior.
"""
from modulos.gestor_archivos import leer_clientes, clientes_vencidos, generar_factura
from modulos.notificaciones import hay_internet, enviar_whatsapp_a_deudores


def main(ruta_csv='clientes.csv'):
    # 1) Leer CSV
    try:
        clientes = leer_clientes(ruta_csv)
    except FileNotFoundError:
        print(f"[ERROR] No se encontró el archivo: {ruta_csv}")
        return
    except Exception as e:
        print(f"[ERROR] Error leyendo CSV: {e}")
        return

    # 2) Filtrar deudores vencidos
    deudores = clientes_vencidos(clientes)
    if not deudores:
        print("[INFO] No hay clientes con deudas vencidas.")
        return

    # 3) Generar facturas (un archivo por cliente)
    generadas = 0
    for c in deudores:
        try:
            ruta = generar_factura(c)
            generadas += 1
            print(f"[OK] Factura generada: {ruta}")
        except Exception as e:
            print(f"[ERROR] No se pudo generar factura para {c.get('Nombre')}: {e}")

    # 4) Enviar notificaciones si hay internet
    if not hay_internet():
        print("[WARN] Sin conexión a internet. No se enviarán mensajes de WhatsApp.")
        return

    try:
        enviar_whatsapp_a_deudores(deudores)
        print("[OK] Notificaciones procesadas (ver consola para detalles).")
    except Exception as e:
        print(f"[WARN] Error al enviar notificaciones: {e}")


if __name__ == '__main__':
    main()
