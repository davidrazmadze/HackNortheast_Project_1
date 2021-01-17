var isLive = true;

$(document).ready(function () {
  submitFormPressed();
  displayAdditionalInputs();
});

//* Helper functions

function submitFormPressed() {
  $("#form").on("submit", function (e) {
    var stockName = $("#stockInput").val();
    var numTweetsInput = $("#numTweetsInput").val();
    var numDaysInput = $("#numDaysInput").val();

    e.preventDefault();
    $.ajax({
      url: "http://127.0.0.1:5000/square/",
      data: {
        text: stockName,
        isLive: isLive,
        numTweetsInput: numTweetsInput,
        numDaysInput: numDaysInput,
      },
      method: "POST",
      success: function (data) {
        $("#stockInput").val("");
        var message =
          "If percentage is 0-45,; Consider selling \
          If percentage is 45-55%, Consider holding\
          If stock is 55-100%, Consider Buying";
        percentageMessage = "Percentage: " + data["percentage"] + "%";
        $("#square").html(message);
        $("#percentage").html(percentageMessage);
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
