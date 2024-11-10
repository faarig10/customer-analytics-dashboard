const apiBaseUrl = "http://127.0.0.1:8000/api";

// Function to fetch customer data
async function fetchCustomerData() {
  const response = await fetch(`${apiBaseUrl}/customers/`);
  const data = await response.json();
  const tableBody = document
    .getElementById("customer-table")
    .querySelector("tbody");
  tableBody.innerHTML = "";

  data.forEach((customer) => {
    const row = document.createElement("tr");
    row.innerHTML = `
            <td>${customer.id}</td>
            <td>${customer.customer_name}</td>
            <td>${customer.cost_of_the_product}</td>
            <td>${customer.prior_purchases}</td>
            <td>${customer.customer_rating}</td>
            <td>${customer.discount_offered}</td>
        `;
    tableBody.appendChild(row);
  });
}

// Function to fetch segmentation data
async function fetchSegmentationData() {
  const response = await fetch(`${apiBaseUrl}/segmentation/`);
  const data = await response.json();
  const tableBody = document
    .getElementById("segmentation-table")
    .querySelector("tbody");
  tableBody.innerHTML = "";

  data.forEach((segment) => {
    const row = document.createElement("tr");
    row.innerHTML = `
            <td>${segment.id}</td>
            <td>${segment.segment}</td>
        `;
    tableBody.appendChild(row);
  });
}
