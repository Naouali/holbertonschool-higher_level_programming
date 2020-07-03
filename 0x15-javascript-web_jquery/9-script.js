$.getJSON('Write a Javascript script that fetches from https://fourtonfish.com/hellosalut/?lang=fr', function(data) {
	$('#hello').text(data.hello);
});
