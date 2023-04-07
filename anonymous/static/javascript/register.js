const input = document.getElementById('id_username').placeholder = 'Anonymous'
const password1 = document.getElementById('id_password1').placeholder = '********'
const password2 = document.getElementById('id_password2').placeholder = '********'
const password2Label = document.getElementById('id_password2').innerHTML

function findLableForControl() {
    var idVal = "id_password2"
    labels = document.getElementsByTagName('label');
    for( var i = 0; i < labels.length; i++ ) {
        console.log(labels[i].htmlFor)
       if (labels[i].htmlFor === idVal)
            console.log(labels[i])
            console.log(labels[i].innerHTML)
            if(labels[i].innerHTML === 'Password confirmation:'){
                labels[i].innerHTML = 'Confirm Password:'
            }
    }
 }

 findLableForControl()
