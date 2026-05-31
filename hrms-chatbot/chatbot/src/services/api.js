const BASE_URL = "http://localhost:8000";

export const createSession = async () => {
  const response = await fetch(`${BASE_URL}/chat/session`, {
    method: "POST",
  });
  const data = await response.json();
  return data.session_id;
};

export const askQuestion = async (question, sessionId) => {
  const response = await fetch(`${BASE_URL}/chat/ask`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      question: question,
      session_id: sessionId,
    }),
  });
  const data = await response.json();
  return data;
};

export const getChatHistory = async (sessionId) => {
  const response = await fetch(`${BASE_URL}/chat/history/${sessionId}`);
  const data = await response.json();
  return data.messages;
};
