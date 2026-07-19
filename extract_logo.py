import re
import base64

with open('logo-transparent.svg', 'r') as f:
    svg_data = f.read()

match = re.search(r'data:image/png;base64,([^"]+)', svg_data)
if match:
    b64_string = match.group(1)
    png_data = base64.b64decode(b64_string)
    with open('logo-clean.png', 'wb') as out_f:
        out_f.write(png_data)
    print("Extracted successfully!")
else:
    print("Could not find base64 data")
