function counterRefresh (count) {
  $("#user-counter").val(count);
}

function appendMessage (userid, message) {
  $("#message-box").append("<div class='message'><span class='user-id'>" + userid + ":</span> " + message + "</div>");
}

function setUserName() {
  my_name = $("#welcome-message").html().slice(0, -2).slice(4);
}

$("#send-push-button").click(function(event) {
  $.post('/wakeup', { in: "wakeup" }, function(ret) {
    if (ret == "wakeup") { // もう起きてる
      $("#send-push-button").attr('disabled',true);
      $("#send-push-button").html("起きたらしい");
      alert("起きたらしい")
    } else {
      var data = JSON.stringify({ userid: my_name, text: "起きろ!!" });
      ws.send(data)
    }
  });
});

var myid;
var my_name;

var ws = new WebSocket(location.origin.replace(/^http/, 'ws'));

ws.onmessage = function(msg) {
  var data = JSON.parse(msg.data);
  if (data.you) { myid = data.you; }
  else if (data.text) {
    var id = my_name;
    appendMessage(id, data.text);
  }
  else if (data.count) { counterRefresh(data.count); }
}
