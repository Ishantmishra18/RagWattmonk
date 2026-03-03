const BASE_URL = "http://127.0.0.1:8000";

export async function askQuestion(query) {
  const response = await fetch(
    `${BASE_URL}/ask?query=${encodeURIComponent(query)}`
  );
  return response.json();
}
export async function fetchData() {
  const response = await fetch(`${BASE_URL}/data`);
  return response.json();
}
