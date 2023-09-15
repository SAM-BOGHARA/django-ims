window.addEventListener('DOMContentLoaded', event => {
    // Amount Number Validation 
    const amountInput = document.getElementById('amount');

    amountInput.addEventListener('input', function (event) {
        const inputValue = event.target.value;
        const validAmount = /^\d+(\.\d{1,2})?$/.test(inputValue);

        if (!validAmount) {
            event.target.value = '';
        }
    });


    // (START Date -> END Date) DatePicker Linkage 

    const startDateInput = document.getElementById('start-date');
    const endDateInput = document.getElementById('end-date');

    // Today's Date
    var today = new Date().toISOString().split('T')[0];

    // start date --> minimum -- no limit ,, maximum -- today
    document.getElementById('start-date').setAttribute('max', today);


    // Disable the end date (It will be disabled until start date is selected.)
    document.getElementById("end-date").disabled = true;



    // Start Date ->> Event Listener 
    // When start date is selected, end date will be enabled.
    // If Start date is cleared, end date will be disabled again.
    startDateInput.addEventListener('input', function (event) {
        const startDate = event.target.value;

        // End Date --> minimum -- start date ,, maximum -- today
        endDateInput.min = startDate;
        endDateInput.max = today;

        if (startDate) {
            document.getElementById("end-date").disabled = false; // When start date is selected, end date will be enabled.
        } else {
            document.getElementById("end-date").value = "";
            document.getElementById("end-date").disabled = true; // If Start date is cleared, end date will be cleared and disabled again.
        }
    });



    // Using inspect element , developer minded user can change the behavoir of dates by inspecting in the browser,
    // so ON FORM SUBMISSION , we will check if both the (startdate,endate) are not changed into future dates.
    document.getElementById('ltc').addEventListener('submit', function (event) {
        // event.preventDefault(); // Prevent form submission

        const form = document.getElementById('ltc');
        const start = new Date(document.getElementById('start-date').value);
        const end = new Date(document.getElementById('end-date').value);
        const today = new Date();

        if (start > today || end > today) {
            document.getElementById('start-date').setAttribute('max', today);
            document.getElementById('end-date').setAttribute('min', start);
            document.getElementById('end-date').setAttribute('max', today);
            alert('Invalid date. Future dates are not allowed.');
        } else {
            // Proceed with form submission
            // this.submit();
        }
    });




    // Pdf size limit
    const input = document.getElementById('billing_documents');
    const errorMsg = document.getElementById('file-error-msg');

    input.addEventListener('change', (event) => {
        const target = event.target;
        if (target.files && target.files[0]) {

            /*Maximum allowed size in bytes
            5MB Example * 1024 * 1024
            Change first operand(multiplier) for your needs*/
            const maxAllowedSize = 5 * 1024 * 1024; // Maximum allowed size in bytes (5MB)

            if (target.files[0].size > maxAllowedSize) {
                target.value = '';
                errorMsg.style.display = 'block'; // Display the error message
            } else {
                errorMsg.style.display = 'none'; // Hide the error message if the file size is valid
            }
        }
    });

});