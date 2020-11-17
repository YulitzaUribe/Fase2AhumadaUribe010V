$( document ).ready(function() {
$(‘#register’).submit(function(e) {
e.preventDefault();
}).validate({
debug: false,
rules: {
«User»: {
required:true,
minlenght:8,
maxlenght:20
},
«email»: {
required:true,
maxlenght:50,
email:true
},
«confirmEmail»: {
required:true,
maxlenght:50,
email:true
},
«Password»: {
required:true,
minlenght:8,
maxlenght:20
},
«confirmPassword»: {
required:true,

}
},
messages: {
«User»: {
required: «Introduce un usuario»,
minlenght:«Usuario debe de contener 8 caracteres minimo»,
maxlenght:«Usuario debe de contener 20 caracteres como maximo»
},
«email»: {
required: «Correo Electronico obligatorio.»,
maxlenght:«Correo Electronico debe de contener 50 caracteres maximo»,
email:«Formato de correo no valido»
},
«confirmEmail»: {
required: «Ingrese correo electronico nuevamente.»,
maxlenght:«El correo electronico debe de contener 50 caracteres maximo»,
email:«Formato de confirmacion de correo electronico no valido»
},
«Password»: {
required: «Introduce una contraseña.»,
minlength: «Contraseña debe de contener minimo 8 Caracteres»,
maxlenght: «Contraseña debe de tener maximo 20 caracteres»
},
«confirmPassword»: {
required: «Introduce tu contraseña nuevamente.»
}
}

});
});