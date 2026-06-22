import json

data = {
    "Cirurgia de Terceiros Molares e Índices de Dificuldade": [
        {"title": "Pernambuco index: predictability of the complexity of surgery", "url": "https://www.sciencedirect.com/science/article/abs/pii/S0901502717315527"},
        {"title": "Assessment of Factors Associated With Surgical Difficulty (Maxillary)", "url": "https://www.joms.org/article/S0278-2391(13)00006-2/abstract"},
        {"title": "Is Overweight a Risk Factor for Adverse Events?", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC4274830/"},
        {"title": "High weight standard and removal of third molars (Prospective study)", "url": "https://www.sciencedirect.com/science/article/pii/S2212440314014151"},
        {"title": "Evaluation of the muscle relaxant cyclobenzaprine", "url": "https://www.researchgate.net/publication/51686816_Evaluation_of_the_muscle_relaxant_cyclobenzaprine_after_third-molar_extraction"},
        {"title": "Effects of dexamethasone and nimesulide on pain and swelling", "url": "https://www.researchgate.net/publication/310471216_Effects_of_co-administered_dexamethasone_and_nimesulide_on_pain_swelling_and_trismus_following_third_molar_surgery"}
    ],
    "Casos Clínicos e Patologia Oral": [
        {"title": "Guided surgery in unusual palatal torus", "url": "https://pubmed.ncbi.nlm.nih.gov/22446429/"},
        {"title": "Tooth embedded in tongue following firearm trauma", "url": "https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1600-9657.2011.00994.x"},
        {"title": "Mastoid osteoma: Report of a rare case", "url": "https://www.sciencedirect.com/science/article/pii/S2090074015000092"},
        {"title": "Ameloblastic fibro-odontoma in children", "url": "https://pubmed.ncbi.nlm.nih.gov/22126932/"},
        {"title": "Lipomas da Região Oral e Maxilofacial (Estudo de 16 anos)", "url": "https://www.researchgate.net/publication/257678093_Lipomas_da_Regiao_Oral_e_Maxilofacial_Estudo_Retrospectivo_de_16_Anos_no_Brasil"},
        {"title": "Granuloma piogênico oral (Estudo de 191 casos)", "url": "https://www.researchgate.net/publication/26585385_Granuloma_piogenico_oral_Um_estudo_epidemiologico_de_191_casos"},
        {"title": "Cisto dentígero (Estudo de 192 casos)", "url": "https://pesquisa.bvsalud.org/portal/resource/pt/lil-655282"},
        {"title": "Lesões fibro-ósseas benignas dos maxilares", "url": "https://pesquisa.bvsalud.org/portal/resource/pt/lil-482668"},
        {"title": "Diagnosis of Calcifying Odontogenic Cyst (2023)", "url": "https://www.researchgate.net/publication/371980338_DIAGNOSIS_AND_SURGICAL_TREATMENT_OF_CALCIFYING_ODONTOGENIC_CYST_REPORT_IN_A_PEDIATRIC_PATIENT"},
        {"title": "Unicystic Mural Ameloblastoma in the Maxilla (2022)", "url": "https://www.researchgate.net/publication/362739735_UNICYSTIC_MURAL_AMELOBLASTOMA_IN_THE_MAXILLA_REPORT_IN_A_PEDIATRIC_PATIENT"}
    ],
    "Ansiedade e Comportamento em Odontologia": [
        {"title": "Prevalence and Predictive Factors of Dental Anxiety", "url": "https://pubmed.ncbi.nlm.nih.gov/23595244/"},
        {"title": "Dental anxiety: relationship with oral health behavior", "url": "https://www.omicsonline.org/author-profile/belmiro-cavalcanti-do-egito-vasconcelos-280625/"}
    ],
    "Outros Estudos e Revisões": [
        {"title": "Knowledge and usage of the mouth guard", "url": "http://revodonto.bvsalud.org/scielo.php?script=sci_abstract&pid=S1808-52102013000300008"},
        {"title": "Most suitable local anaesthetic (Network meta-analysis)", "url": "https://www.researchgate.net/publication/341691283_Which_is_the_most_suitable_local_anaesthetic_when_inferior_nerve_blocks_are_used_for_impacted_mandibular_third_molar_extraction_A_network_meta-analysis"},
        {"title": "Toxicidade sistêmica por anestésicos locais (2025)", "url": "https://www.researchgate.net/publication/398016133_Toxicidade_sistemica_por_anestesicos_locais_implicacoes_clinicas_e_estrategias_de_controle"},
        {"title": "Imagem corporal e saúde mental em câncer de cabeça e pescoço (2024)", "url": "https://www.researchgate.net/publication/396742214_A_relacao_entre_imagem_corporal_e_saude_mental_em_pacientes_com_cancer_de_cabeca_e_pescoco_estrategias_psicologicas_para_o_enfrentamento"}
    ]
}

html = """
    <!-- Produção Científica -->
    <section id="publicacoes" class="py-24 bg-brand-dark marble-bg relative overflow-hidden">
        <div class="absolute inset-0 bg-brand-dark/95 z-0"></div>
        <div class="container mx-auto px-6 lg:px-12 relative z-10">
            <div class="text-center mb-16">
                <h2 class="text-3xl md:text-5xl font-heading mb-6 font-light leading-snug text-brand-gold">Produção Científica</h2>
                <p class="text-brand-light/80 max-w-2xl mx-auto font-light text-sm md:text-base">
                    Com dezenas de publicações em periódicos nacionais e internacionais de alto impacto, o Dr. Ricardo Wathson contribui ativamente para o avanço da cirurgia e odontologia.
                </p>
                <div class="w-24 h-px bg-brand-gold mx-auto mt-8 opacity-50"></div>
            </div>

            <div class="max-w-4xl mx-auto space-y-4">
"""

for category, articles in data.items():
    html += f"""
                <details class="group border border-white/10 bg-black/20 rounded-sm">
                    <summary class="flex justify-between items-center font-medium cursor-pointer list-none p-6 text-brand-gold hover:bg-white/5 transition-colors duration-300">
                        <span class="text-lg md:text-xl font-heading font-light tracking-wide">{category}</span>
                        <span class="transition group-open:rotate-180">
                            <svg fill="none" height="24" shape-rendering="geometricPrecision" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewBox="0 0 24 24" width="24"><path d="M6 9l6 6 6-6"></path>
                            </svg>
                        </span>
                    </summary>
                    <div class="text-brand-light/80 px-6 pb-6 pt-2 text-sm flex flex-col gap-4 border-t border-white/5 bg-black/40">
"""
    for article in articles:
        html += f"""
                        <a href="{article['url']}" target="_blank" rel="noopener noreferrer" class="group/link flex justify-between items-center p-4 hover:bg-white/5 border border-transparent hover:border-white/10 rounded-sm transition-all duration-300">
                            <span class="font-light pr-4">{article['title']}</span>
                            <span class="text-brand-gold text-[10px] uppercase tracking-widest whitespace-nowrap flex items-center gap-2 group-hover/link:translate-x-1 transition-transform">
                                Ler Artigo 
                                <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
                            </span>
                        </a>
"""
    html += """
                    </div>
                </details>
"""

html += """
            </div>
        </div>
    </section>
"""

with open('articles.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Generated articles.html successfully.")

# Now let's inject it into index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# find <section id="contato"
if '<section id="contato"' in content:
    idx = content.find('<section id="contato"')
    new_content = content[:idx] + html + '\n' + content[idx:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Injected into index.html successfully.")
else:
    print("Could not find <section id=\"contato\" in index.html")
