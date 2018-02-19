<!DOCTYPE html>
<html>
<head>
	<title></title>
	<link rel="stylesheet" type="text/css" href="/static/style.css">
</head>
<body>

	% for i in data['results']:
	<div class="main">
		<h3>{{i['eventDateName']}}</h3>
		<h3>{{i['eventHallName']}}</h3>
		<h3>{{i['dateOfShow']}}</h3>
		<img src="{{i['imageSource']}}">
	</div>

	% end



</body>
</html>