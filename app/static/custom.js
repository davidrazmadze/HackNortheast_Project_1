var isLive = true;

$(document).ready(function () {
  submitFormPressed();
  displayAdditionalInputs();
});

//* Helper functions

function submitFormPressed() {
  $("#form").on("submit", function (e) {
    var stockName = $("#stockInput").val();
    console.log(stockName);
    e.preventDefault();
    $.ajax({
      url: "http://127.0.0.1:5000/square/",
      data: {
        text: stockName,
        isLive: isLive,
      },
      method: "POST",
      success: function (data) {
        $("#stockInput").val("");
        console.log(data);
        // $("#square").html("Square of " + number + " is " + data["square"]);
      },
    });
  });
}

function displayAdditionalInputs() {
  $("input[name='radio']").change(function () {
    // Hides the two inputs based on radio button selected
    if ($("#isLive").is(":checked")) {
      $("#numTweetsInput").hide();
      $("#numDaysInput").hide();
      isLive = true;
    } else {
      $("#numTweetsInput").show();
      $("#numDaysInput").show();
      isLive = false;
    }
  });
}
