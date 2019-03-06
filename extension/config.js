$(document).ready(function(){

    $('#btnSearch').on('click',function(e){
        e.preventDefault();
        var item_id = $('#search_word_id').val();
        var item_name = $('#search_word').val();
        $('#search_word_id').val('');
        $('#search_word').val('');
        if (confirm("You are searching for " +item_id + " " +item_name)) {
            data={'data': item_name}
            $.ajax({
                url: 'http://localhost:5000/'+item_id,
                data:   data,
                dataType:   'json',
                method: "PUT",
                success:function(response){
                    var strItem = "<li>"+ response.id + " " +response.name +"</li>";
                    $('#results-list').append(strItem);
                },
                failure: function(response){
                    
                },
                error: function(response){
                    
                }
            });
        }
    });
  });