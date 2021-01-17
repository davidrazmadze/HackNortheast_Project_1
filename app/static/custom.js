$(document).ready(function () {
  submitFormPressed();
  listenForRadioEvents();
});

//* Helper functions

function submitFormPressed() {
  $("#form").on("submit", function (e) {
    var number = $("#num").val();
    e.preventDefault();
    $.ajax({
      url: "http://127.0.0.1:5000/square/",
      data: { number: number },
      method: "POST",
      success: function (data) {
        $("#num").val("");
        $("#square").html("Square of " + number + " is " + data["square"]);
      },
    });
  });
}

function listenForRadioEvents() {
  $("input[name='radio']").change(function () {
    if ($("#isLive").is(":checked")) {
      alert("Is live");
    } else {
      alert("Is past tweets");
    }
  });
}
