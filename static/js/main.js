
$(document).ready(function() {
  $("#submit-button").click(function(){
    var people = [];
    var csrftoken = $.cookie('csrftoken');
    $.each($("input[name='check']:checked"), function(){
      people.push($(this).parent().siblings("#SIN").text());
    });
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
          xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    });
    $.ajax({
      url: "/simpleMilitary/adminOperations", // the endpoint
      type: "POST", // http method
      data: {selected: people}
      success: function(json) {
        $.each($("input[name='check']:checked"), function(){
          $(this).parent().parent().remove();
        });
        $.each(json, function(key, value) {
              $("#result").html(value);
              $("#result").addClass("alert alert-primary");
        });
      },
      error: function() {
        console.log("ERROR");
      }
    });
  });
});
