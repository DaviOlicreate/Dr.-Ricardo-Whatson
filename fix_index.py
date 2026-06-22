import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix Ortognatica folder names
content = content.replace('Ortogna%CC%81tica%20Dr.%20Ricardo%20Whatson', 'Ortognatica%20Dr.%20Ricardo%20Whatson')
content = content.replace('Ortognática Dr. Ricardo Whatson', 'Ortognatica Dr. Ricardo Whatson')

# 2. Remove 'controls' from video tags and ensure 'autoplay' is there
# We want: <video class="..." autoplay playsinline loop muted data-src="...">
content = content.replace(' controls playsinline loop muted', ' autoplay playsinline loop muted')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("index.html updated successfully!")
