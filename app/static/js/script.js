console.log("Script loaded");

// Lista de papéis para o efeito de máquina de escrever

const roles = [
  "Software Engineer",
  "Back-End Developer",
  "Web Developer",
  "Web Designer",
  "UI/UX Designer",
  "Front-End Developer",
  "RPA Developer",
  "Mobile Developer"
];

let i = 0;
let j = 0;
let currentRole = "";
let isDeleting = false;
const speed = 100; // velocidade da digitação
const pause = 1500; // pausa entre palavras

function typeWriter() {
  const typewriter = document.getElementById("typewriter");

  if (i < roles.length) {
    if (!isDeleting && j <= roles[i].length) {
      currentRole = roles[i].substring(0, j++);
      typewriter.textContent = currentRole;
      setTimeout(typeWriter, speed);
    } else if (isDeleting && j >= 0) {
      currentRole = roles[i].substring(0, j--);
      typewriter.textContent = currentRole;
      setTimeout(typeWriter, speed / 2);
    } else if (!isDeleting && j > roles[i].length) {
      isDeleting = true;
      setTimeout(typeWriter, pause);
    } else if (isDeleting && j < 0) {
      isDeleting = false;
      i = (i + 1) % roles.length;
      setTimeout(typeWriter, speed);
    }
  }
}

document.addEventListener("DOMContentLoaded", typeWriter);

//carousel
const track = document.querySelector('.carousel-track');
const btnLeft = document.querySelector('.carousel-btn.left');
const btnRight = document.querySelector('.carousel-btn.right');

let position = 0;
const slideWidth = 140; // largura + gap

if (btnLeft && btnRight) {
    btnLeft.addEventListener('click', () => {
        position += slideWidth;
        if(position > 0) position = -(track.scrollWidth - track.clientWidth);
        track.style.transform = `translateX(${position}px)`;
    });

    btnRight.addEventListener('click', () => {
        position -= slideWidth;
        if(Math.abs(position) > track.scrollWidth - track.clientWidth) position = 0;
        track.style.transform = `translateX(${position}px)`;
    });
}


// Language Switcher
function changeLanguage(lang) {
    const elements = document.querySelectorAll('[data-translate]');
    elements.forEach(element => {
        const key = element.getAttribute('data-translate');
        if (translations[lang] && translations[lang][key]) {
            element.innerHTML = translations[lang][key];
        }
    });
    // Store the selected language in localStorage
    localStorage.setItem('selectedLanguage', lang);
}

document.addEventListener('DOMContentLoaded', () => {
  const languageSwitcher = document.getElementById('language-switcher');
  // Retrieve the selected language from localStorage, default to 'en'
  let currentLang = localStorage.getItem('selectedLanguage') || 'en';

  // Set initial language
  changeLanguage(currentLang);

  // Update flag active state based on currentLang
  if (languageSwitcher) {
    const flags = languageSwitcher.querySelectorAll('.flag');
    flags.forEach(flag => {
      if ((currentLang === 'en' && flag.alt === 'USA Flag') || (currentLang === 'pt-br' && flag.alt === 'Brazil Flag')) {
        flag.classList.add('active');
      } else {
        flag.classList.remove('active');
      }
    });

    languageSwitcher.addEventListener('click', () => {
      // Determine the new language
      if (currentLang === 'en') {
        currentLang = 'pt-br';
      } else {
        currentLang = 'en';
      }

      // Update flag active state based on the new currentLang
      flags.forEach(flag => {
        if ((currentLang === 'en' && flag.alt === 'USA Flag') || (currentLang === 'pt-br' && flag.alt === 'Brazil Flag')) {
          flag.classList.add('active');
        } else {
          flag.classList.remove('active');
        }
      });

      changeLanguage(currentLang);
    });
  }
});