let current_item_name = '';

document.addEventListener('DOMContentLoaded', function() {
    console.info("Created with CurricuBook!");
});

function showDetails(item_name) {
    let elem = document.getElementById(item_name);
    if (elem) {
        document.getElementById('overlay').style.display = "block";
        elem.style.display = "block";
        current_item_name = item_name;

    } else {
        current_item_name = '';
    }
}

function closeDetails() {
    let elem = document.getElementById(current_item_name);
    if (elem) {
        elem.style.display = "none";
        document.getElementById('overlay').style.display = "none";

    } else {
        current_item_name = '';
    }
}
