def calculate_telecom_tax(amount: float) -> float:
    """Belirtilen tutar üzerinden %18 telekomünikasyon vergisi hesaplar."""
    if amount < 0:
        raise ValueError("Tutar negatif olamaz.")
    return round(amount * 0.18, 2) 