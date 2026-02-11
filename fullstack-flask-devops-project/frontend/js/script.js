const movies = [
    "https://image.tmdb.org/t/p/w500/or06FN3Dka5tukK1e9sl16pB3iy.jpg",
    "https://image.tmdb.org/t/p/w500/uxzzxijgPIY7slzFvMotPv8wjKA.jpg",
    "https://image.tmdb.org/t/p/w500/2bXbqYdUdNVa8VIWXVfclP2ICtT.jpg",
    "https://image.tmdb.org/t/p/w500/mINJaa34MtknCYl5AjtNJzWj8cD.jpg",
    "https://image.tmdb.org/t/p/w500/9dKCd55IuTT5QRs989m9Qlb7d2B.jpg"
];

const movieRow = document.getElementById("movieRow");

movies.forEach(movie => {
    const card = document.createElement("div");
    card.classList.add("movie-card");

    card.innerHTML = `<img src="${movie}" alt="movie">`;

    movieRow.appendChild(card);
});

/* Search Feature */
const searchBox = document.querySelector(".search-box");

searchBox.addEventListener("keyup", function() {
    alert("Search feature coming soon 🔥");
});
