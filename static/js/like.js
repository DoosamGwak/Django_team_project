const likeButton = document.querySelectorAll('.like-button')
likeButton.forEach(i =>{
    i.addEventListener('click', function(event){
        const productId = event.target.dataset.id
        const likeCount = document.querySelector(`.like-count-${productId}`)
        axios.defaults.xsrfCookieName = 'csrftoken'
        axios.defaults.xsrfHeaderName = 'X-CSRFToken'
        axios.post(`/products/like/${productId}/`)
        .then(response => {
            likeCount.innerText = response.data.count
            
            if(response.data.liked){
                event.target.className = 'fa-solid fa-heart like-button'
            } else{
                event.target.className = "fa-regular fa-heart like-button"
            }
        })
    })
})