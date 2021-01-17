$(document).ready(function () {
  submitFormPressed();

  // *TODO: Check which radio button is selected,
  // *TODO: Hide num tweets and past days input if live tweets selected
  // $("#isLive").prop("checked", true);
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
