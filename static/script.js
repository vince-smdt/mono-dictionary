// Dom elements
const LOOKUP_BUTTON = document.getElementById("lookup")
const WORD_DATA = document.getElementById("word-data")
const WORD_INPUT = document.getElementById("word-input")

// Submit word in text field
function submit_word(event) {
    if (event.keyCode == 13)
        get_word()
}

// Get word data through fetch
function get_word() {
    const word = WORD_INPUT.value
    const form_data = new FormData()

    form_data.append("word", word)

    fetch(WORD_DEF_URL, {
        method: "POST",
        body: form_data
    })
    .then(response => response.json())
    .then(data => {
        WORD_DATA.innerText = JSON.stringify(data)
    })
}

window.onload = () => {
    // Set event listeners
    WORD_INPUT.addEventListener("keydown", submit_word, false)
    LOOKUP_BUTTON.addEventListener("click", get_word, false)
}
