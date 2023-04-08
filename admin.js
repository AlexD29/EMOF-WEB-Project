function deleteForm(resp) {
    if (resp == null) {
        document.getElementById("confirm-delete-dialog").style.visibility = 'visible'
    }
    else {
        document.getElementById("confirm-delete-dialog").style.visibility = 'hidden'
        if (resp =='Yes'){
            alert("Form has been deleted!")
        }
    }
}