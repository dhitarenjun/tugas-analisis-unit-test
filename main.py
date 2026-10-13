def hitung_diskon(total_belanja):
    if total_belanja >= 100000:
        return total_belanja * 0.9  # Diskon 10%
    return total_belanja

def cek_status(poin):
    if poin > 50:
        return "Member VIP"
    return "Member Reguler"

def login_user(username):
    return username == "ardhita"