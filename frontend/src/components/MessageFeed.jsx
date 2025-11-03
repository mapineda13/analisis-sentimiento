import { Card } from 'react-bootstrap';

const MessageFeed = ({ mensajes }) => (
  <div className="d-grid gap-3">
    {mensajes.map((msg) => (
      <Card key={msg._id}>
        <Card.Body>
          <Card.Text><strong>Mensaje:</strong> {msg.texto_mensaje}</Card.Text>
          <Card.Text><strong>Sentimiento:</strong> {msg.sentimiento}</Card.Text>
          <Card.Text><strong>Tema:</strong> {msg.tema}</Card.Text>
        </Card.Body>
      </Card>
    ))}
  </div>
);

export default MessageFeed;
