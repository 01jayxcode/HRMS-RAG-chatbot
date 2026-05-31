// src/components/ChatWindow.jsx

import { useState, useEffect, useRef } from "react";
import Message from "./Message";
import ChatInput from "./ChatInput";
import { createSession, askQuestion } from "../services/api";

const ChatWindow = () => {
  const [messages, setMessages] = useState([]);
  const [sessionId, setSessionId] = useState(null);
  const [loading, setLoading] = useState(false);
  const bottomRef = useRef(null);

  useEffect(() => {
    const initSession = async () => {
      const id = await createSession();
      setSessionId(id);
    };
    initSession();
  }, []);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const handleSend = async (question) => {
    if (!sessionId) return;

    const userMessage = { role: "user", content: question };
    setMessages((prev) => [...prev, userMessage]);
    setLoading(true);

    try {
      const data = await askQuestion(question, sessionId);
      const botMessage = { role: "assistant", content: data.answer };
      setMessages((prev) => [...prev, botMessage]);
    } catch (error) {
      const errorMessage = {
        role: "assistant",
        content: "Something went wrong. Please try again.",
      };
      setMessages((prev) => [...prev, errorMessage]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="chat-window">
      <div className="chat-header">
        <div className="chat-header-left">
          <div className="chat-header-avatar">🤖</div>
          <div>
            <h2>HRMS Assistant</h2>
            <div className="chat-header-subtitle">Powered by RAG + Gemma</div>
          </div>
        </div>
        <span className={`status ${sessionId ? "online" : "offline"}`}>
          {sessionId ? "● Online" : "● Connecting"}
        </span>
      </div>

      <div className="chat-messages">
        {messages.length === 0 && (
          <div className="empty-state">
            <div className="empty-state-icon">💬</div>
            Ask me anything about HR policies.
            <br />
            Leave, attendance, payroll & more.
          </div>
        )}
        {messages.map((msg, index) => (
          <Message key={index} role={msg.role} content={msg.content} />
        ))}
        {loading && (
          <div className="message bot-message">
            <div className="message-role">HRMS Bot</div>
            <div className="message-content typing">Thinking...</div>
          </div>
        )}
        <div ref={bottomRef} />
      </div>

      <ChatInput onSend={handleSend} disabled={loading} />
    </div>
  );
};

export default ChatWindow;
