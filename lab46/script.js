
const modal = document.getElementById("modal");
const modalImg = document.getElementById("modal-img");
const closeBtn = document.querySelector(".close");
const nextBtn = document.getElementById("next-btn");
const prevBtn = document.getElementById("prev-btn");

const imageUrls = [
    "pic1.jpg",
    "pic2.jpg",
    "pic3.jpg",
    "pic4.jpg",
    "pic5.jpg"
];

const gallery = document.getElementById("gallery");
let currentIndex = 0;

function generateGallery() {
    imageUrls.forEach((url, index) => {
        const img = document.createElement("img");
        img.src = url;
        img.classList.add("gallery-item");
        img.alt = `Image ${index + 1}`;
        gallery.appendChild(img);

        img.addEventListener("click", function() {
            modal.style.display = "flex";
            modal.classList.add("show");
            modalImg.src = url;
            currentIndex = index;

            localStorage.setItem('lastViewedImage', url);
        });
    });
}

generateGallery();

closeBtn.addEventListener("click", function() {
    modal.classList.remove("show");
    setTimeout(() => modal.style.display = "none", 500);
});

nextBtn.addEventListener("click", function() {
    currentIndex = (currentIndex + 1) % imageUrls.length;
    modalImg.src = imageUrls[currentIndex];
    animateTransition();
});

prevBtn.addEventListener("click", function() {
    currentIndex = (currentIndex - 1 + imageUrls.length) % imageUrls.length;
    modalImg.src = imageUrls[currentIndex];
    animateTransition();
});

function animateTransition() {
    modalImg.classList.add("zoom-in");
    setTimeout(() => {
        modalImg.classList.remove("zoom-in");
    }, 300);
}

window.addEventListener("click", function(event) {
    if (event.target === modal) {
        modal.classList.remove("show");
        setTimeout(() => modal.style.display = "none", 500);
    }
});

window.addEventListener("load", function() {
    const lastViewedImage = localStorage.getItem('lastViewedImage');
    if (lastViewedImage) {
        const index = imageUrls.indexOf(lastViewedImage);
        if (index !== -1) {
            modal.style.display = "flex";
            modal.classList.add("show");
            modalImg.src = lastViewedImage;
            currentIndex = index;
        }
    }
});
