import re


def barcode_validation(function_data):
    regex = r"@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+"

    for barcode in function_data:
        match = re.fullmatch(regex, barcode)

        if match:
            product_group = "".join(re.findall(r'\d', barcode))
            product_group = product_group if product_group else "00"
            print(f"Product group: {product_group}")
        else:
            print("Invalid barcode")


number = int(input())

data = [input() for iteration in range(number)]
barcode_validation(data)
