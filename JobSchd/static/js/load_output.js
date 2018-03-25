$(document).ready (function () {
	setInterval(function () {
		$.get( "function/test_local_process.php", function( data ) {
			$( "#result" ).html( '<pre>' + data + '</pre>' );
			console.log( "Load was performed." );
		});
	}, 1000)
});