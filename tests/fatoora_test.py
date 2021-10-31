from fatoora import Fatoora

fatoora_obj = Fatoora(
    seller_name="Awiteb",
    tax_number=1234567891,  # or "1234567891"
    invoice_date="2021-07-12T14:25:09+00:00",  # ISO8601 @see https://en.wikipedia.org/wiki/ISO_8601
    total_amount=100,  # or 100.0, 100.00, "100.0", "100.00"
    tax_amount=15,  # or 15.0, 15.00, "15.0", "15.00"
)

fatoora_details = {
    "seller_name": "Awiteb",
    "tax_number": "1234567891",
    "invoice_date": "2021-07-12T14:25:09+00:00",
    "total_amount": "100.00",
    "tax_amount": "15.00",
}


def test_seller_name():
    assert fatoora_obj.seller_name == fatoora_details.get("seller_name")


def test_tax_number():
    assert fatoora_obj.tax_number == fatoora_details.get("tax_number")


def test_invoice_date():
    assert fatoora_obj.invoice_date.isoformat() == fatoora_details.get("invoice_date")


def test_total_amount():
    assert fatoora_obj.total_amount == fatoora_details.get("total_amount")


def test_tax_amount():
    assert fatoora_obj.tax_amount == fatoora_details.get("tax_amount")


def test_dict():
    assert fatoora_obj.dict() == fatoora_details


def test_qrcode():
    fatoora_obj.qrcode("qr_code.png")


def test_read_qrcode():
    dct = Fatoora.read_qrcode("qr_code.png", dct=True)
    base = Fatoora.read_qrcode("qr_code.png", dct=False)
    assert dct == fatoora_details
    assert base == fatoora_obj.base64


def test_base2dict():
    assert Fatoora.base2dict(fatoora_obj.base64) == fatoora_details
