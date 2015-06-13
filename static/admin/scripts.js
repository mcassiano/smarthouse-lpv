$(document).ready(function() {
    registerColorPicker();
    getTemp();
    getLEDState(8);
    getLEDState(12);
    getLEDState(13);

});

function registerColorPicker() {
	$("#colorpicker").spectrum({
	    color: "#f00",
	    change: function (color) {
	    	var red = Math.floor(color._r);
	    	var green = Math.floor(color._g);
	    	var blue = Math.floor(color._b);

	    	setRGB(red, blue, green);

	    }
	});
}

function setRGB(red1, blue1, green1) {
	$.get("http://lpv.hakai.in/setRGB", {red: red1, blue: blue1, green: green1}).done(function(data) {
    	console.log(data);
    });
}

function toggleLED(led1) {
	$.get("http://lpv.hakai.in/toggleLed", {led: led1}).done(function(data) {
    	getLEDState(led1);
    });
}

function getTemp() {
	$.get("http://lpv.hakai.in/getTemp").done(function(data) {
	data = JSON.parse(data);
    	var temp = data.temperature;
    	console.log(data);
      	$("#temp").html(Math.floor(temp));
    });
}

function getLEDState(led1) {
	$.get("http://lpv.hakai.in/getLEDState", {led: led1}).done(function(data) {
	var ledContainer = $("#led"+led1);
	var led = ledContainer.find('i');
	data = JSON.parse(data);
	state = data.state;
	console.log(ledContainer);

    	if (state == "off") {
    		led.attr('class', 'fa fa-toggle-off');
		ledContainer.find('span').html('Liga');
	}
    	else {
    		led.attr('class', 'fa fa-toggle-on');
		ledContainer.find('span').html('Desliga');
	}
    });
}
