import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

with open('cards_output.html', 'r', encoding='utf-8') as f:
    cards = f.read()

with open('modals_output.html', 'r', encoding='utf-8') as f:
    modals = f.read()

# 1. Inject Swiper CSS
if 'swiper-bundle.min.css' not in content:
    content = content.replace('</head>', '    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css" />\n</head>')

# 2. Inject Swiper JS and Modals HTML before </body>
if 'swiper-bundle.min.js' not in content:
    js_and_modals = modals + '\n    <script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>\n</body>'
    content = content.replace('</body>', js_and_modals)

# 3. Replace Section 4
# Find <!-- Sessão 4: Especialidades em Grid Visual --> to <!-- Sessão 5: Estrutura de Procedimentos Completos (Accordion Refinado) -->
start_marker = "<!-- Sessão 4: Especialidades em Grid Visual -->"
end_marker = "<!-- Sessão 5: Estrutura de Procedimentos Completos (Accordion Refinado) -->"

new_section_4 = f"""{start_marker}
    <section id="especialidades" class="py-1">
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-1 px-1">
{cards}
        </div>
    </section>

    """

content = re.sub(f'{re.escape(start_marker)}.*?{re.escape(end_marker)}', f'{new_section_4}{end_marker}', content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("index.html injected successfully!")
