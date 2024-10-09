function createStar(score, container) {
    console.log('score')
    container.innerHTML = '';

    const fullStar = '<i class="fas fa-star"></i>';
    const halfStar = '<i class="fas fa-star-half-alt"></i>';
    const emptyStar = '<i class="far fa-star"></i>';


    score = score || 0;

    const fullStars = Math.floor(score);
    const hasHalfStar = score - fullStars >= 0.5;
    const emptyStars = 5 - fullStars - (hasHalfStar ? 1 : 0);

    for (let i = 0; i < fullStars; i++) {
        container.innerHTML += fullStar;
    }

    if (hasHalfStar) {
        container.innerHTML += halfStar;
    }

    for (let i = 0; i < emptyStars; i++) {
        container.innerHTML += emptyStar;
    }

}

