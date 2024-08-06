// Define base API call parameters
let port = '5050';
let url = `http://127.0.0.1:${port}/api/search`;

// Define the main function
async function main() {
  // Add event listener for form submission. On button click, runs handleSubmit()
  document.getElementById('eASForm').addEventListener('submit', handleSubmit);
}

// Handle form submission
async function handleSubmit(event) {
  event.preventDefault(); // Prevent the form from submitting normally
    
  // Show loading indicator
  document.getElementById('loading').style.display = 'block';
  
  // Clear previous results
  document.getElementById("price").innerHTML = "";
  document.getElementById("description").innerHTML = "";
  
  // Get input from form
  const input = document.getElementById('userInput').value;
  
  try {
      // Get data from backend
      const eASObject = await getData(url, input);
      updateOutput(eASObject);
  } catch (error) {
      console.error('Error:', error);
      // Display error message to user
      document.getElementById("description").innerHTML = "An error occurred. Please try again.";
  } finally {
      // Hide loading indicator
      document.getElementById('loading').style.display = 'none';
  }
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
  let k = 1;
  let response = await fetch(`${url}?query=${encodeURIComponent(input)}&k=${k}`);
  return response.json();
}

// Update output field
function updateOutput(eASObject) {
    // Set price field
    document.getElementById("price").innerHTML = `${"$"}${eASObject.price.toFixed(2)}`;
    // Set description field
    document.getElementById("description").innerHTML = eASObject.itemDescription;
}

// Call main when the page loads
window.onload = main;