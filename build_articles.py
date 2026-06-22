import re
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
    <section id="publicacoes" class="py-24 bg-brand-light relative overflow-hidden">
        <div class="container mx-auto px-6 lg:px-12 relative z-10">
            <div class="flex flex-col lg:flex-row gap-16 items-start">
                
                <!-- Coluna Imagem -->
                <div class="w-full lg:w-5/12 lg:sticky top-32">
                    <div class="relative aspect-[3/4] overflow-hidden rounded-sm shadow-2xl">
                        <!-- Caso não haja a imagem drricardo-academic.jpg, uma bela imagem de fallback será mostrada -->
                        <img src="./drricardo-academic.jpg" onerror="this.src='https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80'" alt="Produção Científica" class="w-full h-full object-cover">
                        <div class="absolute inset-0 bg-gradient-to-t from-brand-dark/90 via-transparent to-transparent"></div>
                        <div class="absolute bottom-0 left-0 p-8 w-full">
                            <h2 class="text-3xl md:text-5xl font-heading mb-4 font-light leading-snug text-white">Produção<br/><span class="text-brand-gold italic">Científica</span></h2>
                            <p class="text-white/90 font-light text-sm max-w-sm">
                                Contribuição ativa para o avanço da cirurgia maxilofacial e odontologia com dezenas de publicações internacionais de alto impacto.
                            </p>
                        </div>
                    </div>
                </div>

                <!-- Coluna Artigos -->
                <div class="w-full lg:w-7/12 space-y-4 pt-4">
"""

for category, articles in data.items():
    html += f"""
                    <details class="group border border-gray-200 bg-white rounded-sm shadow-sm hover:shadow-md transition-shadow">
                        <summary class="flex justify-between items-center font-medium cursor-pointer list-none p-6 text-brand-dark hover:text-brand-gold transition-colors duration-300">
                            <span class="text-lg md:text-xl font-heading font-light tracking-wide">{category}</span>
                            <span class="transition group-open:rotate-180 text-brand-gold">
                                <svg fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewBox="0 0 24 24" width="24"><path d="M6 9l6 6 6-6"></path></svg>
                            </span>
                        </summary>
                        <div class="text-brand-dark/70 px-6 pb-6 pt-2 text-sm flex flex-col gap-3 border-t border-gray-100 bg-gray-50/50">
"""
    for article in articles:
        html += f"""
                            <a href="{article['url']}" target="_blank" rel="noopener noreferrer" class="group/link flex justify-between items-center p-4 bg-white hover:bg-gray-50 border border-gray-100 hover:border-brand-gold/30 rounded-sm transition-all duration-300 shadow-sm">
                                <span class="font-light pr-4 text-brand-dark group-hover/link:text-brand-gold transition-colors">{article['title']}</span>
                                <span class="text-brand-gold text-[10px] uppercase tracking-widest whitespace-nowrap flex items-center gap-2 group-hover/link:translate-x-1 transition-transform">
                                    Acessar 
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
        </div>
    </section>
"""

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Substituir a antiga seção publicacoes inteira
# Encontraremos onde começa <section id="publicacoes" e onde ela termina.
# Sabemos que termina logo antes de <section id="contato"

start_idx = content.find('<section id="publicacoes"')
end_idx = content.find('<section id="contato"', start_idx)

if start_idx != -1 and end_idx != -1:
    new_content = content[:start_idx] + html + content[end_idx:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Atualizado com sucesso com o novo design claro e side-by-side!")
else:
    print("Não achou")
