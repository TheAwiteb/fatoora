# ZATCA (Fatoora) QR-Code Implementation

An unofficial package help developers to implement ZATCA (Fatoora) QR code easily which required for e-invoicing

<p align="center">
  <a href="https://pypi.org/project/fatoora/">
    <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/fatoora?color=9cf">
  </a>
  <a href="https://pypi.org/project/fatoora/">
    <img alt="PyPI" src="https://img.shields.io/pypi/v/fatoora?color=9cf">
  </a>
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/pypi/l/fatoora?color=9cf&label=License" alt="License">
  </a>
  <a href="https://github.com/psf/black">
    <img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg">
  </a>
  <a href="https://github.com/TheAwiteb/fatoora/actions/workflows/python-app.yml">
    <img alt="test-fatoora" src="https://github.com/TheAwiteb/fatoora/actions/workflows/python-app.yml/badge.svg">
  </a>
  <a href="https://github.com/TheAwiteb/fatoora/actions/workflows/release.yml">
    <img alt="Upload Python Package" src="https://github.com/TheAwiteb/fatoora/actions/workflows/release.yml/badge.svg">
  </a>
</p>


## Requirements

* python >= 3.8
* zbar-tools

## Installation

You can install the package via pypi (pip):

```bash
$ pip3 install fatoora
```

or via github (git):

```bash
$ git clone https://github.com/TheAwiteb/fatoora/
$ cd fatoora
$ python3 setup.py install
```

## Usage

## variables

**Here the features of the variables of the Fatoora class will be explained**

| Name         | Feature | How will it be in the tag| How will it be when you call|
|--------------|:-----:|:-----:|:-----:|
| seller_name  | saved directly without processing |  No changes will be made to it  |  No changes will be made to it  |
|  tax_number  |  receives the tax number as a text and a number as well, and save it as string |  number as string  |    number as string|
| invoice_date | receives the date as timestamp number or string or float and saving it as float in string with 4 decimal digits| string of timestamp with 4 decimal digits |  datetime object  |
| total_amount |  receives the tax number as a text and a number as well, It will be converted to a number with two decimal digits |  It is of type str and has two decimal digits  |    It is of type str and has two decimal digits|
| tax_amount   |  same total_amount |  same total_amount  |  same total_amount|


<!-- | name here | feature here| -->


<br>

### Generate Base64

```python
from fatoora import Fatoora

fatoora_obj = Fatoora(
    seller_name="Awiteb",
    tax_number=1234567891, # or "1234567891"
    invoice_date=1635872693.3186214, # Timestamp
    total_amount=100, # or 100.0, 100.00, "100.0", "100.00"
    tax_amount=15, # or 15.0, 15.00, "15.0", "15.00"
)

print(fatoora_obj.base64)
# AQZBd2l0ZWICCjEyMzQ1Njc4OTEDDzE2MzU4NzI2OTMuMzE4NgQGMTAwLjAwBQUxNS4wMA==
```

### Render A QR Code Image

You can render the tags as QR code image easily


```python
from fatoora import Fatoora

fatoora_obj = Fatoora(
    seller_name="Awiteb",
    tax_number=1234567891,
    invoice_date=1635872693.3186214,
    total_amount=100,
    tax_amount=15,
)

fatoora_obj.qrcode("qr_code.png")
```

### Generate hash (sha256)

```python
from fatoora import Fatoora

fatoora_obj = Fatoora(
    seller_name="Awiteb",
    tax_number=1234567891, 
    invoice_date=1635872693.3186214,
    total_amount=100, 
    tax_amount=15, 
)

print(fatoora_obj.hash)
# 0863de708b8bfb02541e3662c327f7a6a22173b635690960ad5a1ba506096522
```

### Read qr code

```python
from fatoora import Fatoora

fatoora_obj = Fatoora(
    seller_name="Awiteb",
    tax_number=1234567891, 
    invoice_date=1635872693.3186214,
    total_amount=100, 
    tax_amount=15, 
)

fatoora_obj.qrcode("qr_code.png")

print(Fatoora.read_qrcode("qr_code.png", dct=True))
# {'seller_name': 'Awiteb', 'tax_number': '1234567891', 'invoice_date': '1635872693.3186', 'total_amount': '100.00', 'tax_amount': '15.00'}

print(Fatoora.read_qrcode("qr_code.png", dct=False))
# AQZBd2l0ZWICCjEyMzQ1Njc4OTEDDzE2MzU4NzI2OTMuMzE4NgQGMTAwLjAwBQUxNS4wMA==

```

### Extra Methods

```python
fatoora_obj = Fatoora(
    seller_name="Awiteb",
    tax_number=1234567891, 
    invoice_date=1635872693.3186214,
    total_amount=100, 
    tax_amount=15, 
)

print(fatoora_obj.invoice_date.year)
# 2021

print(fatoora_obj.invoice_date.isoformat())
# 2021-11-02T20:04:53.318600

print(fatoora_obj.invoice_date.timestamp())
# 1635872693.3186

print(fatoora_obj.json())
# '{"seller_name": "Awiteb", "tax_number": "1234567891", "invoice_date": "1635872693.3186", "total_amount": "100.00", "tax_amount": "15.00"}'

print(fatoora_obj.dict())
# {'seller_name': 'Awiteb', 'tax_number': '1234567891', 'invoice_date': '1635872693.3186', 'total_amount': '100.00', 'tax_amount': '15.00'}

# Use class to get fatoora details by base64

print(Fatoora.base2dict(fatoora_obj.base64))
# {'seller_name': 'Awiteb', 'tax_number': '1234567891', 'invoice_date': '1635872693.3186', 'total_amount': '100.00', 'tax_amount': '15.00'}

```

## Discussions
Question, feature request, discuss about fatoora [here](https://github.com/TheAwiteb/fatoora/discussions)

## Issues
You can report a bug [here](https://github.com/TheAwiteb/fatoora/issues)

## Security

If you discover any security related issues.

## License

The MIT License (MIT). Please see [License File](LICENSE.md) for more information.