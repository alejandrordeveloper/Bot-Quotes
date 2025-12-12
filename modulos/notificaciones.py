import time


def hay_internet(host='8.8.8.8', port=53, timeout=3):
    """Verifica conexión simple a Internet (intento rápido con socket)."""
    import socket
    try:
        socket.setdefaulttimeout(timeout)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.close()
        return True
    except Exception:
        return False


def enviar_whatsapp_a_deudores(deudores):
    """Envía mensajes por WhatsApp usando solo `pywhatkit`.

    No usa `os` ni abre navegadores manualmente; `pywhatkit` gestionará la apertura.
    """
    try:
        import pywhatkit
    except Exception as e:
        raise RuntimeError('pywhatkit no está instalado o no se puede importar: ' + str(e))

    for c in deudores:
        telefono = c.get('Telefono')
        mensaje = f"Hola {c.get('Nombre')}, tu factura ya fue generada. Debes: ${c.get('MontoDeuda'):.2f}"
        try:
            # sendwhatmsg_instantly abrirá WhatsApp Web y enviará el mensaje
            pywhatkit.sendwhatmsg_instantly(telefono, mensaje, wait_time=15, tab_close=True)
            print(f"[OK] Enviado a {c.get('Nombre')} ({telefono})")
            time.sleep(2)
        except Exception as e:
            print(f"[WARN] No se pudo enviar a {c.get('Nombre')} ({telefono}): {e}")
            continue
import time
import socket
import webbrowser

def hay_internet(host="8.8.8.8", port=53, timeout=3):
    """
    Verifica conectividad abriendo un socket al DNS de Google.
    """
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except Exception:
        return False

def enviar_whatsapp_a_deudores(deudores):
    """
    Envía mensajes por WhatsApp Web usando pywhatkit.
    """
    try:
        import pywhatkit
    except Exception as e:
        raise RuntimeError(f"pywhatkit no disponible: {e}")

    # Abrir WhatsApp Web una vez
    webbrowser.open("https://web.whatsapp.com")
    time.sleep(5)

    for c in deudores:
        telefono = c["Telefono"]
        mensaje = f"Hola {c['Nombre']}, tu factura ya fue generada. Debes: ${c['MontoDeuda']:.2f}"
        try:
            pywhatkit.sendwhatmsg_instantly(
                phone_no=telefono,
                message=mensaje,
                wait_time=20,
                tab_close=True,
                close_time=3
            )
            print(f"[OK] WhatsApp enviado a {c['Nombre']} ({telefono}).")
            time.sleep(2)
        except Exception as e:
            print(f"[WARN] No se pudo enviar a {c['Nombre']} ({telefono}). Motivo: {e}")
            continue
