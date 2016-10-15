//function to hide my email address from spambots
var mail = function(){
  var parts = ["&#108;&#105;&#110;&#101;&#99;&#114;&#115;&#111;&#117;&#122;&#97;", "gmail", "com", "&#46;", "&#64;", "//formspree.io/"];
  var url = parts[5] + parts[0] + parts[4] + parts[1] + parts[3] + parts[2];
  return(decodeHtmlEntity(url));
}

//function to decode html special chars
var decodeHtmlEntity = function(str) {
  return str.replace(/&#(\d+);/g, function(match, dec) {
    return String.fromCharCode(dec);
  });
};

//ajax function to submit the form to the formspree server and give feedback to the user
var $contactForm = $('#contact-form');
$contactForm.submit(function(e) {
	e.preventDefault();
	$.ajax({
		url: mail(),
		method: 'POST',
		data: $(this).serialize(),
		dataType: 'json',
		beforeSend: function() {
			$contactForm.append('<div class="alert alert--loading">Sending message…</div>');
		},
		success: function(data) {
			$contactForm.find('.alert--loading').hide();
			$contactForm.append('<div class="alert alert--success">Message sent!</div>');
		},
		error: function(err) {
			$contactForm.find('.alert--loading').hide();
			$contactForm.append('<div class="alert alert--error">Ops, there was an error.</div>');
		}
	});
});




