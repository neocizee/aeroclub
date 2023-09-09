const carousel = document.querySelector('.carousel');
const indicators = document.querySelectorAll('.indicator');
const numSlides = document.querySelectorAll('.carousel-section').length;

let currentSlide = 0;

function goToSlide(slideIndex) {
    currentSlide = slideIndex;
    const translateValue = -currentSlide * 100;
    carousel.style.transform = `translateY(${translateValue}vh)`;
    updateIndicators();
}

function updateIndicators() {
    indicators.forEach((indicator, index) => {
        if (index === currentSlide) {
            indicator.classList.add('selected');
        } else {
            indicator.classList.remove('selected');
        }
    });
}

window.addEventListener('wheel', (e) => {
    if (e.deltaY > 0 && currentSlide < numSlides - 1) {
        goToSlide(currentSlide + 1);
    } else if (e.deltaY < 0 && currentSlide > 0) {
        goToSlide(currentSlide - 1);
    }
});

indicators.forEach((indicator, index) => {
    indicator.addEventListener('click', () => {
        goToSlide(index);
    });
});

updateIndicators();