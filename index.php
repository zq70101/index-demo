<!DOCTYPE html>
<?php header("Access-Control-Allow-Origin: *"); ?>
<html>
<head>
	<meta charset="utf-8" />
	<link rel="stylesheet" type="text/css" href="css/bootstrap.min.css" />
	<script src="js/jquery-2.0.3.min.js" ></script>
	<script type="text/javascript">
	$(function(){
		$('form').submit(false);
		$('#run').click(function(){
			var server=$('#server').val().trim();
			//var version=$('#version').val().trim();
            //if (!version){
           //     alert("version can't null");
            //    return 0;
           // }
			$('#run').prop("disabled", true);
			$('#content').html("doing now....");
			$.ajax({
				'url': "http://10.10.10.10/xx.php",
				'data':{"type":1,"server":server},
				'dataType':'text',
				'success':function(data){
					$("#content").html("suc");
                    $('#run').prop("disabled", false);
				},
				'error':function(data){
					$("#content").html("err");
					$('#run').prop("disabled", false);
				}
			});
		});
	});
	</script>
</head>
<body>
<div class="container">
	<h2>test</h2>
	<form class="form_inline">
		<div class="form_group">
			<label>t</label>
			<select id="server" class="form-control" style="width: 200px;">
			<option value ="1234">1234</option>
			</select>
		</div>
		<button id="run" type="submit" class="btn btn-default" >run</button>
	</form>
	<br/>
<div id="content"></div>
<br/>
<br/>
</div>
</body>
</html>
