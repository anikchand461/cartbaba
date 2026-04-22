async function search() {
  const query = document.getElementById("query").value;

  const res = await fetch(`http://127.0.0.1:8000/search/?query=${query}`, {
    method: "POST",
  });

  const data = await res.json();

  const resultsDiv = document.getElementById("results");
  resultsDiv.innerHTML = "";

  data.results.forEach((p) => {
    const div = document.createElement("div");
    div.className = "card";

    div.innerHTML = `
        <h3>${p.name}</h3>
        <img src="${p.image}" width="150"/>
        <p>Price: ₹${p.price}</p>
        <p>Rating: ${p.rating}</p>
    `;

    resultsDiv.appendChild(div);
  });
}
