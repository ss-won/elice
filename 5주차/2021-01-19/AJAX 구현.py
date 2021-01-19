<!--index.html-->
<html >
<head >
    <script src = "https://code.jquery.com/jquery-latest.min.js" > </script >
</head >
<body >
    <p id = "example" > AJAX < /p >
    <input type = "text" id = "id1" placeholder = "id" >
    <input type = "text" id = "name1" placeholder = "name" >
    <input type = "text" id = "context1" placeholder = "context" >
    <input type = "button" id = "execute" value = "execute" >

    <script >
        $('#execute').click(function(){
            var id= $('#id1').val();
            var name= $('#name1').val();
            var context= $('#context1').val();

            var postdata={
                'id': id, 'name': name, 'context': context
            }
            $.ajax({
                type: 'POST',
                url: '{{url_for("ajax")}}',
                data: JSON.stringify(postdata),
                dataType: 'JSON',
                contentType: "application/json",
                success: function(data){
                    alert('성공! 데이터 값:' + data.result2['id']+" " +
                          data.result2['name'] + " " + data.result2['context'])
                },
                error: function(request, status, error){
                    alert('ajax 통신 실패')
                    alert(error); }
            })
        })
    </script >
    <table border = 1 width = "600" >
        <thead >
        <td > 목차 < /td >
		<td > 이름 < /td >
		<td > 내용 < /td >
		</thead >

    {% for row in rows % }
		<tr >
            <td>{{ loop.index }}</td>
			<td>{{ row['name'] }}</td>
			<td>{{ row['context'] }}</td>
		</tr>
	{% endfor %}
	</table>
    
</body>
</html>
