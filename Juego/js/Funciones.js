var x;
x=$(document);
x.ready(inicializarEventos);



function inicializarEventos()
{
  var x;
  x=$("#Parrafo");			
  x.click(changeParraph)
}

function changeParraph()		
{
  var x;
  x=$("#Parrafo");
  x.css("color","#BA4A00");
  x.css("background-color","black");
  x.css("font-family","Times");
  x.css("font-size","24px")
}