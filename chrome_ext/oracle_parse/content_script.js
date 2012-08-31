var BACKGROUND_COLOR = 'rgb(173, 216, 230)';

$(document).click(function(event){
	//alert("Injection of content script worked!");
	var target = $(event.target);
	
	// basic error check
	if (typeof target.data('previous_bg') === 'undefined') {
		target.data('previous_bg', null);
	}
	
	var cur_color = target.css('background-color');
	
	// Undo the color change
	console.log('Cur color: '+cur_color+'; previous_bg: '+target.data('previous_bg'));
	
	if (cur_color == BACKGROUND_COLOR) {
		target.css('background-color', target.data('previous_bg'));
		target.data('previous_bg', null);
		console.log("Reset color");
	} else {
		target.data('previous_bg', cur_color);
		target.css('background-color', BACKGROUND_COLOR);
	}

	console.log('[click]: '+event.target+', '+target.css('background-color'));
	return event;
});

