$(document).ready(function() {
  $("#submit-button").click(function(){
    var people = [];
    $.each($("input[name='check']:checked"), function(){
      people.push($(this).parent().siblings("#SIN").text());
    });
    $.ajax({
      url: "/simpleMilitary/adminOperations", // the endpoint
      type: "POST", // http method
      data: {selected: people},
      success: function(json) {
        $.each($("input[name='check']:checked"), function(){
          $(this).parent().parent().remove();
        });
      },
      error: function() {
        console.log("ERROR");
      }
    });
  });
});