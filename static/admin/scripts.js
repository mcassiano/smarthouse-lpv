$(document).ready(function() {
    registerColorPicker();

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

function setRGB(red, blue, green) {
	$.get("http://lpv.hakai.in/setRGB", {red: red, blue: blue, green: green}).done(function(data) {
    	console.log(data);
    });
}

function toggleLED(led) {
	$.get("http://lpv.hakai.in/toggleLED", {led: led}).done(function(data) {
    	getLEDState(led);
    });
}

function getTemp() {
	$.get("http://lpv.hakai.in/getTemp", function(data) {
    	var temp = data.temperature;
    	console.log(data);
      	$("#temp").html(temp);
    });
}

function getLEDState(led) {
	$.get("http://lpv.hakai.in/getLEDState", {led: led}).done(function(data) {
    	var state = data.state;

    	if (state == 'off')
    		$("#led"+led).attr('class', 'fa fa-toggle-off');
    	else
    		$("#led"+led).attr('class', 'fa fa-toggle-on');
    });
}