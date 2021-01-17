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
        percentageMessage = "Percentage: " + data["percentage"] + "%";
        $("#percentage").html(percentageMessage);

        var percentageDouble = parseFloat(data["percentage"]);

        console.log(percentageDouble);

        if (percentageDouble >= 0 && percentageDouble < 45.0) {
          $("#percentResults").css("background-color", "red");
          $("#square").html("You should sell based on Twitter data.");
        } else if (percentageDouble < 55.0) {
          $("#percentResults").css("background-color", "gray");
          $("#square").html("You should hold based on Twitter data.");
        } else {
          $("#percentResults").css("background-color", "green");
          $("#square").html("You should buy based on Twitter data.");
        }
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
