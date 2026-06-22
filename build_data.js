const fs = require('fs');
const path = require('path');

const folders = [
    { name: 'Rinoplastia', dir: 'Rinoplastia Dr. Ricardo Whatson', desc: 'Cirurgia estética e funcional do nariz, buscando harmonia facial e melhora respiratória.' },
    { name: 'Mentoplastia', dir: 'Mentoplastia Dr. Ricardo Whatson', desc: 'Aperfeiçoamento do contorno do queixo, equilibrando as proporções faciais de forma definitiva.' },
    { name: 'Ortognática', dir: 'Ortognática Dr. Ricardo Whatson', desc: 'Correção de desarmonias ósseas faciais, aliando estética e função mastigatória.' },
    { name: 'Otoplastia', dir: 'Otoplastia Dr. Ricardo Whatson', desc: 'Correção de orelhas de abano e outras imperfeições, trazendo simetria e autoconfiança.' },
    { name: 'Lip Fit', dir: 'Lip fit Dr.Ricardo Whatson', desc: 'Encurtamento do lábio superior, rejuvenescendo o sorriso e a área perioral.' },
    { name: 'Lifting Facial', dir: 'Liftin Dr. Ricardo Whatson', desc: 'Reposicionamento profundo dos tecidos faciais (Deep Plane), combatendo a flacidez com extrema naturalidade.' },
    { name: 'Blefaroplastia', dir: 'Blefaroplastia Dr.Ricardo Whatson', desc: 'Remoção do excesso de pele e bolsas de gordura, devolvendo um olhar descansado e vibrante.' }
];

let cardsHtml = '';
let modalsHtml = '';

folders.forEach((folder, index) => {
    const dirPath = path.join(__dirname, folder.dir);
    if (!fs.existsSync(dirPath)) return;

    const files = fs.readdirSync(dirPath).filter(f => !f.startsWith('.'));
    
    let coverFile = files.find(f => f.toLowerCase().endsWith('.jpg') || f.toLowerCase().endsWith('.jpeg') || f.toLowerCase().endsWith('.png'));
    let coverUrl = coverFile ? `./${encodeURIComponent(folder.dir)}/${encodeURIComponent(coverFile)}` : 'https://placehold.co/800x600/222/C4A052?text=' + encodeURIComponent(folder.name);

    cardsHtml += `
            <!-- Card ${folder.name} -->
            <div class="relative h-[400px] md:h-[500px] overflow-hidden group cursor-pointer" onclick="openModal('modal-${index}')">
                <img src="${coverUrl}" alt="${folder.name}" class="w-full h-full object-cover transition-transform duration-1000 group-hover:scale-105">
                <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/40 to-transparent group-hover:from-black/80 transition-colors duration-500"></div>
                <div class="absolute inset-0 flex flex-col justify-end p-8 z-10">
                    <h3 class="text-2xl md:text-3xl font-heading text-white mb-3 font-light">${folder.name}</h3>
                    <p class="text-gray-300 font-light mb-6 opacity-0 translate-y-4 group-hover:opacity-100 group-hover:translate-y-0 transition-all duration-500 text-sm max-w-sm">
                        ${folder.desc}
                    </p>
                    <button class="inline-flex items-center text-brand-gold uppercase text-[10px] tracking-widest hover:text-white transition-colors">
                        <span>Ver Casos Reais</span>
                        <div class="h-[1px] w-6 bg-brand-gold ml-3"></div>
                    </button>
                </div>
            </div>`;

    modalsHtml += `
    <!-- Modal ${folder.name} -->
    <div id="modal-${index}" class="fixed inset-0 z-50 hidden bg-black/95 backdrop-blur-md flex items-center justify-center opacity-0 transition-opacity duration-300">
        <!-- Close button -->
        <button onclick="closeModal('modal-${index}')" class="absolute top-6 right-6 text-white hover:text-brand-gold z-[60] p-2 transition-colors">
            <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M6 18L18 6M6 6l12 12"></path></svg>
        </button>
        
        <div class="w-full max-w-5xl h-[90vh] px-4 flex flex-col justify-center relative">
            <div class="text-center mb-4 mt-8">
                <h3 class="text-3xl font-heading text-brand-gold">${folder.name}</h3>
                <p class="text-gray-400 text-sm tracking-widest uppercase mt-2 mb-2">Deslize para ver mais casos</p>
            </div>
            
            <!-- Swiper Container -->
            <div class="swiper swiper-${index} w-full h-[70vh] rounded-lg overflow-hidden">
                <div class="swiper-wrapper">`;

    files.forEach(file => {
        const ext = path.extname(file).toLowerCase();
        const fileUrl = `./${encodeURIComponent(folder.dir).replace(/%20/g, '+')}/${encodeURIComponent(file).replace(/%20/g, '+')}`;
        
        if (ext === '.mp4' || ext === '.mov') {
            modalsHtml += `
                    <div class="swiper-slide flex items-center justify-center bg-black">
                        <video class="w-full h-full object-contain lazy-video" controls playsinline loop muted data-src="${fileUrl}">
                        </video>
                    </div>`;
        } else if (ext === '.jpg' || ext === '.jpeg' || ext === '.png' || ext === '.webp') {
            modalsHtml += `
                    <div class="swiper-slide flex items-center justify-center bg-black">
                        <img loading="lazy" data-src="${fileUrl}" alt="${folder.name} Caso" class="w-full h-full object-contain swiper-lazy">
                        <div class="swiper-lazy-preloader swiper-lazy-preloader-white"></div>
                    </div>`;
        }
    });

    modalsHtml += `
                </div>
                <div class="swiper-button-next text-brand-gold"></div>
                <div class="swiper-button-prev text-brand-gold"></div>
                <div class="swiper-pagination"></div>
            </div>
        </div>
    </div>`;
});

fs.writeFileSync('cards_output.html', cardsHtml);
fs.writeFileSync('modals_output.html', modalsHtml);
console.log('HTML generated successfully!');
