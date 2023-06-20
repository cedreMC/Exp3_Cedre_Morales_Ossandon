function Enviar(){
    let nom = concepto.getElementById("nom").value;
    let ape = concepto.getElementById("ape").value;
    let fono = concepto.getElementById("fono").value;
    let correo = concepto.getElementById("correo").value;
    let fecha = concepto.getElementById("fecha").value;
    let pass = concepto.getElementById("pass").value;
    let radios = document.getElementsByName("programar");
    let valorRadio = "";

    for(let a = 0; a < redios.length; a++){
        if(radios[a].checked) {
            valorRadio = radios[a].value;
        }
    }

    console.log("Nombre:"+nom+"\n Apellido" + ape +"\n telefono"+fono+"\n Correo"+correo+"\n es mayor de edad"+valorRadio);
}


function Enviar(){
    alert("Los datos se han guardao, gracias pro confiar en nosotros y gracias por unirte a nosotros.");
}
 

