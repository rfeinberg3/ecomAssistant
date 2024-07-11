// Define base API call parameters
let port = '5001';
let url = `http://localhost:${port}/api/search`;

// Define the main function
async function main() {
  // Add event listener for form submission. On button click, runs handleSubmit()
  document.getElementById('eASForm').addEventListener('submit', handleSubmit);
}

// Handle form submission
async function handleSubmit(event) {

    event.preventDefault(); // Prevent the form from submitting normally

    input = document.getElementById('input').innerHTML;

    // Get data from backend
    const eASObject = await getData(url, input);
    updateOutput(eASObject.topk);
}

// Fetch data from backend
async function getData(url, input) {
  /*
  :arg url: base url for API calls
  :atype: string
  :arg input: text to be used for eAS search
  :atype: string
  :return: JSON eAS object from search on input
  :rtype: JSON object
  */
  let response = await fetch(`${url}/${model}?input=${encodeURIComponent(input)}`);
  return response.json();
}

// Update output field
function updateOutput(topTokens) {
    const output = `Top Tokens: [${topTokens[0]}, ${topTokens[1]}, ${topTokens[2]}]`;
    document.getElementById("output").innerHTML = output;
}

// Call main when the page loads
window.onload = main;