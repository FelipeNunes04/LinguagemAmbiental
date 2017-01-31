window.onload = function () {
	getAno();
}

function getAno() {
	var data = new Date();
	ano = data.getFullYear();
	var p = document.getElementById('ano');
	p.innerHTML = "Copyright &copy; Linguagem Ambiental "+ano;
}