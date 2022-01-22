<div align="center">
  <img src="https://zatca.gov.sa/ar/E-Invoicing/PublishingImages/header_logo.svg">
  <h1>ZATCA (Fatoora) QR-Code Implementation</h1>
  <p>An <strong>unofficial package</strong> help developers to implement ZATCA (Fatoora) QR code easily which required for e-invoicing</p>
  <a href="https://pypi.org/project/fatoora/">
    <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/fatoora?color=9cf">
  </a>
  <a href="https://pypi.org/project/fatoora/">
    <img alt="PyPI" src="https://img.shields.io/pypi/v/fatoora?color=9cf">
  </a>
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/pypi/l/fatoora?color=9cf&label=License" alt="License">
  </a>
  <br>
  <a href="https://github.com/TheAwiteb/fatoora/actions/workflows/python-app.yml">
    <img alt="test-fatoora" src="https://github.com/TheAwiteb/fatoora/actions/workflows/python-app.yml/badge.svg">
  </a>
  <a href="https://github.com/TheAwiteb/fatoora/actions/workflows/release.yml">
    <img alt="Upload Python Package" src="https://github.com/TheAwiteb/fatoora/actions/workflows/release.yml/badge.svg">
  </a>
  <br>
  <a href="https://github.com/psf/black">
    <img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg">
  </a>
</div>

<details open>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#Requirements">Requirements</a>
    </li>
    <li>
      <a href="#Installation">Installation</a>
      <ul>
        <li><a href="#PyPi">With PyPi</a></li>
        <li><a href="#GitHub">With GitHub</a></li>
      </ul>
    </li>
    <li>
        <a href="#Usage">Usage</a>
        <ul>
            <li><a href="#Variables">variables</a></li>
            <li><a href="#Generate-Base64">Generate Base64</a></li>
            <li>
                <a href="#Render-A-QR-Code-Image">Render A QR Code Image</a>
                <ul>
                    <li><a href="#The-content-is-the-base64-of-the-invoice">The content is the base64 of the invoice</a></li>
                    <li><a href="#The-content-is-the-invoice-url">The content is the invoice url</a></li>
                </ul>
            </li>
            <li><a href="#Generate-hash-(sha256)">Generate hash (sha256)</a></li>
            <li><a href="#Read-qr-code">Read qr code</a></li>
            <li><a href="#Extra-Methods">Extra Methods</a></li>
            <li><a href="#Extra-Functions">Extra Functions</a></li>
        </ul>
    </li>
    <li><a href="#Discussions">Discussions</a></li>
    <li><a href="#Issues">Issues</a></li>
    <li><a href="#Security">Security</a></li>
    <li><a href="#Donating">Donating</a></li>
    <li><a href="#Project-use-this-package">Project use this package</a></li>
    <li><a href="#License">License</a></li>
  </ol>
</details>


## Requirements

* [Python](https://Python.org/) >= 3.8
* [zbar-tools](http://zbar.sourceforge.net/)

## Installation

### PyPi

```bash
$ pip3 install fatoora
```

### GitHub

```bash
$ git clone https://github.com/TheAwiteb/fatoora/
$ cd fatoora
$ python3 setup.py install
```

## Usage

### Variables

**Here the features of the variables of the Fatoora class will be explained**

- Seller’s name.
- Seller’ tax number, which is the VAT registration number.
- Invoice date, which is the timestamp of the electronic invoice.
- Invoice total amount, which is the electronic invoice total **with VAT**.
- Tax amount, which is the VAT total.


| Name         | Feature | How will it be in the tag| How will it be when you call|
|--------------|:-----:|:-----:|:-----:|
| seller_name  | saved directly without processing |  No changes will be made to it  |  No changes will be made to it  |
|  tax_number  |  receives the tax number as a text and a number as well, and save it as string |  number as string  |    number as string|
| invoice_date | receives the date as timestamp or datetime object, or string ISO 8601 Zulu format| string of date as ISO 8601 Zulu format |  datetime object  |
| total_amount |  receives the tax number as a text and a number as well |  It is of type str as float |    It is of type float|
| tax_amount   |  same total_amount + **Accept `None` value to get VAT auto from `total_amount`** |  same total_amount  |  same total_amount|


> Note: The `tax_amount` is rounded to the nearest two decimal places, if it is greater than that ( if `tax_amount` == `15` its will be `15.0`)

> Note: If you set `tax_amount` to `None` the `vat_rates` == `0.15` you can change it in `Fatoora` object


<br>

### Generate Base64

```python
from fatoora import Fatoora

fatoora_obj = Fatoora(
    seller_name="Awiteb",
    tax_number=1234567891, # or "1234567891"
    invoice_date=1635872693.3186214, # timestamp or datetime object, or string ISO 8601 Zulu format
    total_amount=100, # or 100.0, 100.00, "100.0", "100.00"
    tax_amount=15, # or 15.0, 15.00, "15.0", "15.00"
)

print(fatoora_obj.base64)
# AQZBd2l0ZWICCjEyMzQ1Njc4OTEDFDIwMjEtMTEtMDJUMTc6MDQ6NTNaBAUxMDAuMAUEMTUuMA==
```

### Render A QR Code Image

You can render the tags as QR code image easily

#### The content is the base64 of the invoice

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
<div align="center">
<img src="https://i.suar.me/dWOB7/t" alt="qr_code.png">
</div>

#### The content is the invoice url

```python
from fatoora import Fatoora

fatoora_obj = Fatoora(
    seller_name="Awiteb",
    tax_number=1234567891,
    invoice_date=1635872693.3186214,
    total_amount=100,
    tax_amount=15,
    qrcode_url="https://example.com"
)

fatoora_obj.qrcode("qr_code_with_url.png")
```

<div align="center">
<img src="https://i.suar.me/OLJ3G/t" alt="qr_code_with_url.png">
</div>

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
# 20b8ddb6ed9cb98be3d8535a1f4f28e35888842c1b0aed0e90c3e7fb51080dd9
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
# {'seller_name': 'Awiteb', 'tax_number': '1234567891', 'invoice_date': '2021-11-02T17:04:53Z', 'total_amount': '100.0', 'tax_amount': '15.0'}

print(Fatoora.read_qrcode("qr_code.png", dct=False))
# AQZBd2l0ZWICCjEyMzQ1Njc4OTEDFDIwMjEtMTEtMDJUMTc6MDQ6NTNaBAUxMDAuMAUEMTUuMA==

```

### Extra Methods

```python
from fatoora import Fatoora
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
# 2021-11-02T17:04:53

print(fatoora_obj.invoice_date.timestamp())
# 1635861893.0

print(fatoora_obj.json())
# '{"seller_name": "Awiteb", "tax_number": "1234567891", "invoice_date": "2021-11-02T17:04:53Z", "total_amount": "100.0", "tax_amount": "15.0"}'

print(fatoora_obj.dict())
# {'seller_name': 'Awiteb', 'tax_number': '1234567891', 'invoice_date': '2021-11-02T17:04:53Z', 'total_amount': '100.0', 'tax_amount': '15.0'}

# Use class to get fatoora details by base64

print(Fatoora.base2dict(fatoora_obj.base64))
# {'seller_name': 'Awiteb', 'tax_number': '1234567891', 'invoice_date': '2021-11-02T17:04:53Z', 'total_amount': '100.0', 'tax_amount': '15.0'}


```

### Extra Functions
```python
import fatoora

print(fatoora.is_valid_iso8601_zulu_format("invalid date"))
# False

print(fatoora.is_valid_iso8601_zulu_format("2021-11-02T17:04:53Z"))
# True

```

## Discussions
Question, feature request, discuss about fatoora [here](https://github.com/TheAwiteb/fatoora/discussions)

## Issues
You can report a bug from [here](https://github.com/TheAwiteb/fatoora/issues/new?assignees=&labels=bug&template=bug.md)

## Security

If you discover any security related issues.

## Donating
> Note: This address for BEP20 tokens

|    Currency          |                Address                          |
| ---------------------|------------------------------------------------ |
| Binance **BNB**| ```0x4ab0974c7dfcdcdf24d8323a93b061d41e9cf3f0```|
| Binance USD **BUSD**  | ```0x4ab0974c7dfcdcdf24d8323a93b061d41e9cf3f0```|
| Tether **USDT** | ```0x4ab0974c7dfcdcdf24d8323a93b061d41e9cf3f0``` |
| Bitcoin **BTC**  | ```0x4ab0974c7dfcdcdf24d8323a93b061d41e9cf3f0```|
| Bitcoin Cash **BCH**| ```0x4ab0974c7dfcdcdf24d8323a93b061d41e9cf3f0```|

## Project use this package
RAQ ERP - [raqss.co](https://raqss.co)

**If you are interested in adding your project to the list, you can make a PR and add it**
<!-- 

Addition terms:

   For open source projects:
       <project name> - <developer name> - <project url>
        example:
            Awiteb project - [Awiteb](https://github.com/theAwiteb) - [super-project](https://github.com/theAwiteb/super-project)

   For closed source projects:
       <project name> - <website url>
        example:
            Awiteb project - [example.com](https://example.com)

 -->

## License

The MIT License (MIT). Please see [License File](LICENSE) for more information.
