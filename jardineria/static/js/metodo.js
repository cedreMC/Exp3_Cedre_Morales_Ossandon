
//función que valida un formulario a través de JqueryValidate
$(function(){
    $("#mi-formulario").validate({
        rules:{
            nom:{
                required:true
            },
            correo:{
                required:true,
                email:true
            },
            pass:{
                required:true
            },
            fono:{
                required:true,
                number:true
            },
            fecha:{
                required:true
            },
            pass2:{
                required:true,
                equalTo:pass
            }

        },//rules
        messages:{
            nom:{
                required: 'Ingrese nombre de usuario',
                minlength: 'Caracteres insuficientes (3)'
            },
            correo:{
                required: 'Ingrese correo de usuario',
                email: 'Formato de correo inválido'
            },
            pass:{
                required: 'Ingrese contraseña',
                minlength: 'Caracteres insuficientes (8)'
            },
            fono:{
                required: 'Ingrese teléfono',
                minlength: 'Cantidad de digitos insuficientes (9)'
            },
            fecha:{
                required: 'Seleccione una fecha válida',
                min: 'Fecha no corresponde'
            },
            pass2:{
                required: 'Ingrese una contraseña',
                minlength: 'Caracteres insuficientes (8)',
                equalTo: 'Contraseñas no coinciden'
            },
        },//messages
    })//validate

})//function