const btn_classify = document.getElementById('btn-classify')
const selected_model_el = document.getElementById('select-model')
const news_content_el = document.getElementById('news-content')

const error_div = document.getElementById('error')
const results_div = document.getElementById('results')

const pred_news_type_el = document.getElementById('predicted-news-type')
const confidence_el = document.getElementById('confidence')
const pred_val_el = document.getElementById('predicted-value')
const model_type_el = document.getElementById('model-type')
let errMsg = ''

btn_classify.addEventListener('click', async (e) => {
    e.preventDefault()

    errMsg = ''
    hideErrorElement()
    hideResultsElement()
    
    // alert('Yippee!')
    let model = selected_model_el.value
    let news = news_content_el.value

    const data = {model, news}
    
    try {

        const response = await fetch('/classify-news', {
            method: 'POST',
            headers: {
                "Content-Type": 'application/json'
            },
            body: JSON.stringify(data)
        })
    
        if (response.ok){
            const data = await response.json()
            console.log('Returned:')
            console.log(data)

            if(data?.error){
                showError(data.error)
            } else {
                showResults(data.results)
            }

        } else {
            console.log(`error: ${response.status}`)
            errorMsg = `Error processing request: ${response.statusText}`
            showError(errorMsg)
        }
        
    } catch (err) {
        errMsg = err.message
        showError(errMsg)
    }

})

const showError = (errorMessage) => {
    error_div.style.display = 'inline-block'
    error_div.innerText = errorMessage
}

const hideErrorElement = () => {
    error_div.innerText = ''
    error_div.style.display = 'none'
}

const showResults = (results) => {
    results_div.style.display = 'block'

    pred_news_type_el.className = results.predicted_value == 1 ? 'fake' : 'real'

    pred_news_type_el.innerHTML = `Prediction: <strong> <em> ${results.predicted_category} </em> </strong>`
    confidence_el.innerHTML = `Confidence: <strong> ${results.confidence} </strong>`
    pred_val_el.innerHTML = `Predicted Value: <strong> ${results.predicted_value} </strong>`
    model_type_el.innerHTML = `Model: <strong> ${results.model} </strong>`
}

const hideResultsElement = () => {
    pred_news_type_el.innerHTML = ''
    confidence_el.innerHTML = ''
    pred_val_el.innerHTML = ''
    model_type_el.innerHTML = ''

    results_div.style.display = 'none'
}