$('#chat-box').hide()

$('#chat').click(function() {
  $(this).fadeOut(500)
  $('#chat-box').fadeIn(500)
})

$('.fa.fa-close').click(function() {
  $('#chat-box').fadeOut(500)
  $('#chat').fadeIn(500)
})

$('form#chat-form').submit(function(event) {
  event.preventDefault()
  var msg = $('#message').val()
  $('#message').val('')
  $('#messages').append($('<li>').html(msg))
  /* HTTP Request to Rasa Server */
  $.ajax({
    type: 'POST',
    url: 'http://localhost:5005/webhooks/rest/webhook',
    contentType: "application/json; charset=utf-8",
    data: JSON.stringify({'sender': 'rasa_bot','message': msg}),
    success: function(data, status){
      data.forEach(function(item, index){
        setTimeout(function(){
          $('#messages').append($("<li class='bot'>").html(item.text))
        },  1500);
      })
    }
  })
  $('#chat-messages').animate({
    scrollTop: $('#chat-messages').get(0).scrollHeight
  }, 250)
})