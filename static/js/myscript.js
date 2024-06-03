const btn_classify = document.getElementById('btn-classify')
const selected_model_el = document.getElementById('select-model')
const news_content_el = document.getElementById('news-content')

btn_classify.addEventListener('click', async (e) => {
    e.preventDefault()

    // alert('Yippee!')
    let model = selected_model_el.value
    let news = news_content_el.value

    const data = {model, news}

    const response = await fetch('/classify-news', {
        method: 'POST',
        headers: {
            "Content-Type": 'application/json'
        },
        body: JSON.stringify(data)
    })

    if (response.ok){
        const result = await response.json()
        console.log('Returned:')
        console.log(result)
    } else {
        console.log(`error: ${response.status}`)
    }
})