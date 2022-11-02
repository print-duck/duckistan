function blu(my_id) {
    document.getElementById(my_id).style="background-color: blue";
}


function red(my_id) {
    document.getElementById(my_id).style="background-color: red";
}

function col_swap(my_id) {

    if (document.getElementById(my_id).style.backgroundColor=='red') {
        blu(my_id)
    }
    else {
        red(my_id)
    }
}