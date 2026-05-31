// src/components/Message.jsx

const Message = ({ role, content }) => {
  return (
    <div
      className={`message ${role === "user" ? "user-message" : "bot-message"}`}
    >
      <div className="message-role">{role === "user" ? "You" : "HRMS Bot"}</div>
      <div className="message-content">{content}</div>
    </div>
  );
};

export default Message;
