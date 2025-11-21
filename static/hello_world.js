document.getElementById("helloBtn").addEventListener("click", sayHello)


function sayHello(greeting) {
	const name = document.getElementById('name').value
	alert('Hi '+ name)
	console.log("You clicked the button and called sayHello")
}