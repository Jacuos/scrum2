$(function() {
    var scheme = window.location.protocol == 'https:' ? 'wss' : 'ws';
    var chatsock = new WebSocket(
        scheme + '://' + window.location.host + '/' + window.location.pathname);

    chatsock.onmessage = function(message) {
        var chat = $('#chat-messages')
        var content = JSON.parse(message.data)
        chat.append('<b>' + content.author + '</b> ' + content.message + '<br>')
    };

    $('#chat-form').on('submit', function(event) {
        chatsock.send($('#chat-input').val());
        $('#chat-input').val('');
        return false;
    });
});
