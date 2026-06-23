import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

with open('cards_output.html', 'r', encoding='utf-8') as f:
    cards = f.read()

with open('modals_output.html', 'r', encoding='utf-8') as f:
    modals = f.read()

# 1. Replace Section 4
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

# 2. Replace Modals
# Find the start of modals (<!-- Modal Rinoplastia -->) and the end (swiper script)
modals_start_marker = "<!-- Modal Rinoplastia -->"
modals_end_marker = '<script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>'

# It's possible the first modal isn't Rinoplastia if things change, but we know it's there currently.
if modals_start_marker in content and modals_end_marker in content:
    content = re.sub(f'{re.escape(modals_start_marker)}.*?{re.escape(modals_end_marker)}', f'{modals}\n    {modals_end_marker}', content, flags=re.DOTALL)
else:
    print("Could not find modals markers, appending before swiper script if possible.")
    content = content.replace(modals_end_marker, f'{modals}\n    {modals_end_marker}')


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("index.html injected successfully with proper replacement!")
