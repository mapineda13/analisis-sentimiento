import { useEffect, useState } from 'react';
import axios from 'axios';
import PieChart from '../components/PieChart';
import BarChart from '../components/BarChart';
import MessageFeed from '../components/MessageFeed';
import { Container, Row, Col } from 'react-bootstrap';

const Dashboard = () => {
  const [resumen, setResumen] = useState({ positivo: 0, negativo: 0, neutro: 0 });
  const [temas, setTemas] = useState({});
  const [mensajes, setMensajes] = useState([]);

  useEffect(() => {
    axios.get(`${process.env.REACT_APP_API_URL}/sentimientos`).then(res => {
      const data = res.data;
      const temasContados = {};
      console.log('data: ', data);

      // Asignar directamente el resumen
      setResumen({
        positivo: data.positivo || 0,
        negativo: data.negativo || 0,
        neutro: data.neutro || 0
      });
      setTemas(temasContados);
      //setMensajes(data.slice(-10).reverse());
    });
      // Obtener frecuencia de temas
      axios.get(`${process.env.REACT_APP_API_URL}/temas`).then(res => {
        const temasData = res.data;
        setTemas(temasData);
      });

      // Obtener mensajes recientes
      axios.get(`${process.env.REACT_APP_API_URL}/mensajes`).then(res => {
        const mensajesData = res.data;
        setMensajes(mensajesData.slice(-10).reverse());
      });
  }, []);

  return (
    <Container className="py-4">
      <h1 className="mb-4">Dashboard de Sentimientos</h1>
      <Row className="mb-4">
        <Col md={6}><PieChart data={resumen} /></Col>
        <Col md={6}><BarChart temas={temas} /></Col>
      </Row>
      <h2 className="mb-3">Mensajes Recientes</h2>
      <MessageFeed mensajes={mensajes} />
    </Container>
  );
};

export default Dashboard;
