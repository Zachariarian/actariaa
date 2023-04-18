// Function to show/hide loan amount input field

function showLoanAmount() {

  let loanType = document.getElementById("loan-type").value;

  let loanAmount = document.getElementById("loan-amount");

  if (loanType === "personal") {

    loanAmount.style.display = "none";

  } else {

    loanAmount.style.display = "block";

  }

}

// Add event listener to loan type select element

let loanTypeSelect = document.getElementById("loan-type");

loanTypeSelect.addEventListener("change", showLoanAmount);

