const search_input = document.getElementById("search-query");

function search() {
    query = search_input.value;
    window.location.href = "http://" + window.location.host + `/search?query=${query}`;
}