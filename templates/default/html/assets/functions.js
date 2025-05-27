document.addEventListener('DOMContentLoaded', function() {
    console.info("Created with CurricuBook!");
});

function showDetails(item_name) {
    let elem = document.getElementById(item_name);
    console.log('showDetails', elem);
    if (elem) {
        document.getElementById('overlay').style.display = "block";
        elem.style.display = "block";
    }
}

function closeDetails(item_name) {
    let elem = document.getElementById(item_name);
    console.log('closeDetails', elem);
    if (elem) {
        elem.style.display = "none";
        document.getElementById('overlay').style.display = "none";
    }
}
