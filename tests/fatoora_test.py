from fatoora import Fatoora
from json import loads
import os

qrcode_filename = "qr_code.png"
qrcode_filename_with_url = "qr_code_url.png"

fatoora_obj = Fatoora(
    seller_name="Awiteb",
    tax_number=1234567891,  # or "1234567891"
    invoice_date=1635872693.3186214,  # timestamp
    total_amount=100,  # or 100.0, 100.00, "100.0", "100.00"
    tax_amount=15,  # or 15.0, 15.00, "15.0", "15.00"
)

fatoora_obj_with_url = Fatoora(
    seller_name="Awiteb",
    tax_number=1234567891,  # or "1234567891"
    invoice_date=1635872693.3186214,  # timestamp
    total_amount=100,  # or 100.0, 100.00, "100.0", "100.00"
    tax_amount=15,  # or 15.0, 15.00, "15.0", "15.00"
    qrcode_url="https://example.com",
)

fatoora_details = {
    "seller_name": "Awiteb",
    "tax_number": "1234567891",
    "invoice_date": "1635872693.3186",
    "total_amount": "100.00",
    "tax_amount": "15.00",
}


def test_seller_name():
    for obj in [fatoora_obj, fatoora_obj_with_url]:
        assert obj.seller_name == fatoora_details.get("seller_name")


def test_tax_number():
    for obj in [fatoora_obj, fatoora_obj_with_url]:
        assert obj.tax_number == fatoora_details.get("tax_number")


def test_invoice_date():
    for obj in [fatoora_obj, fatoora_obj_with_url]:
        assert obj.tags[3] == fatoora_details.get("invoice_date")


def test_total_amount():
    for obj in [fatoora_obj, fatoora_obj_with_url]:
        assert obj.total_amount == fatoora_details.get("total_amount")


def test_tax_amount():
    for obj in [fatoora_obj, fatoora_obj_with_url]:
        assert obj.tax_amount == fatoora_details.get("tax_amount")


def test_dict():
    for obj in [fatoora_obj, fatoora_obj_with_url]:
        assert obj.dict() == fatoora_details


def test_json():
    json = fatoora_obj.json()
    json_with_url = fatoora_obj_with_url.json()
    json_dict_with_url = loads(json_with_url)
    json_dict = loads(json)

    for dct in [json_dict, json_dict_with_url]:
        assert dct.get("seller_name") == fatoora_details.get("seller_name")
        assert dct.get("tax_number") == fatoora_details.get("tax_number")
        assert dct.get("invoice_date") == fatoora_details.get("invoice_date")
        assert dct.get("total_amount") == fatoora_details.get("total_amount")
        assert dct.get("tax_amount") == fatoora_details.get("tax_amount")


def test_qrcode():
    fatoora_obj.qrcode(qrcode_filename)
    fatoora_obj_with_url.qrcode(qrcode_filename_with_url)
    for filename in [qrcode_filename, qrcode_filename_with_url]:
        assert os.path.lexists(filename)


def test_read_qrcode():
    dct = Fatoora.read_qrcode(qrcode_filename, dct=True)
    base = Fatoora.read_qrcode(qrcode_filename, dct=False)

    url = Fatoora.read_qrcode(qrcode_filename_with_url, dct=False)

    assert url == fatoora_obj_with_url.qrcode_url
    assert base == fatoora_obj_with_url.base64

    assert dct == fatoora_details
    assert base == fatoora_obj.base64


def test_base2dict():
    for obj in [fatoora_obj, fatoora_obj_with_url]:
        assert Fatoora.base2dict(obj.base64) == fatoora_details
