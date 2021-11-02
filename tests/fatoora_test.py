from fatoora import Fatoora
from json import loads

fatoora_obj = Fatoora(
    seller_name="Awiteb",
    tax_number=1234567891,  # or "1234567891"
    invoice_date=1635872693.3186214,  # timestamp
    total_amount=100,  # or 100.0, 100.00, "100.0", "100.00"
    tax_amount=15,  # or 15.0, 15.00, "15.0", "15.00"
)

fatoora_details = {
    "seller_name": "Awiteb",
    "tax_number": "1234567891",
    "invoice_date": "1635872693.3186",
    "total_amount": "100.00",
    "tax_amount": "15.00",
}


def test_seller_name():
    assert fatoora_obj.seller_name == fatoora_details.get("seller_name")


def test_tax_number():
    assert fatoora_obj.tax_number == fatoora_details.get("tax_number")


def test_invoice_date():
    assert fatoora_obj.tags[3] == fatoora_details.get("invoice_date")


def test_total_amount():
    assert fatoora_obj.total_amount == fatoora_details.get("total_amount")


def test_tax_amount():
    assert fatoora_obj.tax_amount == fatoora_details.get("tax_amount")


def test_dict():
    assert fatoora_obj.dict() == fatoora_details


def test_json():
    json = fatoora_obj.json()
    json_dict = loads(json)

    json_dict.get("seller_name") == fatoora_details.get("seller_name")
    json_dict.get("tax_number") == fatoora_details.get("tax_number")
    json_dict.get("invoice_date") == fatoora_details.get("invoice_date")
    json_dict.get("total_amount") == fatoora_details.get("total_amount")
    json_dict.get("tax_amount") == fatoora_details.get("tax_amount")


def test_qrcode():
    fatoora_obj.qrcode("qr_code.png")


def test_read_qrcode():
    dct = Fatoora.read_qrcode("qr_code.png", dct=True)
    base = Fatoora.read_qrcode("qr_code.png", dct=False)
    assert dct == fatoora_details
    assert base == fatoora_obj.base64


def test_base2dict():
    assert Fatoora.base2dict(fatoora_obj.base64) == fatoora_details
