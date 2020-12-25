function onClickedLoanPredict() {
    console.log("Estimate price button clicked");
    // Simple values
    var appincome = document.getElementById('AppIncome').value;
    var coappincome = document.getElementById('CoAppIncome').value;
    var loanamount = document.getElementById('LoanAmount').value;
    var loanterm = document.getElementById('LoanTerm').value;
    // get radio's values
    var gender = document.querySelector('input[name="Gender"]:checked').value;
    var married = document.querySelector('input[name="Married"]:checked').value;
    var education = document.querySelector('input[name="Education"]:checked').value;
    var self_employed = document.querySelector('input[name="SelfEmployed"]:checked').value;

    // get select's values
    var dependents = document.getElementById("Dependents").value;
    var credit_history = document.getElementById("CreditHistory").value;
    var property_area = document.getElementById('PropertyArea').value;

    //result
    var result = document.getElementById('result')

    // url model
    var url = "/predict_loan"; 
    console.log(appincome);
    console.log(coappincome);
    console.log(loanamount);
    console.log(loanterm);
    console.log(gender);
    console.log(married);
    console.log(education);
    console.log(self_employed);
    console.log(dependents);
    console.log(credit_history);
    console.log(property_area);

  
    $.post(
      url,
      {
        appincome : appincome,
        coappincome : coappincome,
        loanamount : loanamount,
        loanterm : loanterm,
        gender : gender,
        married : married,
        education : education,
        self_employed : self_employed,
        dependents : dependents,
        credit_history : credit_history,
        property_area : property_area
      },
      function (data, status) {
        console.log(data.result);
        result.innerHTML =
          "<h2>" + data.result.toString() + "</h2>";
          result.classList.add(data.alert);
          if ( result.classList.contains(data.alert)){
            result.classList.toggle(data.alert);

          }


        
        console.log(status);
      }
    );
  }