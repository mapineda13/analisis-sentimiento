import { Pie } from 'react-chartjs-2';
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js';
ChartJS.register(ArcElement, Tooltip, Legend);

const PieChart = ({ data }) => {
  const chartData = {
    labels: ['Positivo', 'Negativo', 'Neutro'],
    datasets: [{
      data: [data.positivo, data.negativo, data.neutro],
      backgroundColor: ['#198754', '#dc3545', '#ffc107'],
    }]
  };

  return <Pie data={chartData} />;
};

export default PieChart;
