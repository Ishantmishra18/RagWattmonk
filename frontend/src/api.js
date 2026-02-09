const BASE_URL = "http://localhost:8000";

export async function askQuestion(query) {
  const response = await fetch(
    `${BASE_URL}/ask?query=${encodeURIComponent(query)}`
  );
  return response.json();
}
