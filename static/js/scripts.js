$(document).ready(function()){

    var searchBtn = $('#search-btn');
    var searchForm = $('#search-form');
=
    $(searchBtn).on('click' function(){
        searchForm.submit();

    });

}

// Janela do relatório
$('#exampleModal').on('show.bs.modal', function (event) {
  var button = $(event.relatedTarget) // Botão que desencadeou o modal
  var recipient = button.data('whatever') // Extrair informações dos atributos de dados*.
  // Se necessário, pode iniciar aqui um pedido de AJAX (e depois fazer a actualização numa callback).
  // Atualizar o conteúdo do modal. Utilizaremos aqui o jQuery, mas poderá utilizar uma biblioteca de ligação de dados ou outros métodos.
  var modal = $(this)
  modal.find('.modal-title').text('New message to ' + recipient)
  modal.find('.modal-body input').val(recipient)
})



<!-- JS usado apenas para nao permitir caracteres alem de numeros no input codigo_seguranca
		O segundo metodo calcula a parcela
 -->
< language='Java'>
function SomenteNumero(e){
    var tecla=(window.event)?event.keyCode:e.which;
    if((tecla>47 && tecla<58)) return true;
    else{
    	if (tecla==8 || tecla==0) return true;
	else  return false;
    }
}

function alimentarCampo() {
	var preco = {{produto.valor}}
	var quantd = {{quantidade}}
	var minhaLista = document.getElementById("parcelas");
	document.getElementById("valorparcela").value = (preco / minhaLista.options[minhaLista.selectedIndex].value).toFixed(2)*quantd;
}


