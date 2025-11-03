import { Bar } from 'react-chartjs-2';
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Tooltip, Legend } from 'chart.js';
ChartJS.register(CategoryScale, LinearScale, BarElement, Tooltip, Legend);

const BarChart = ({ temas }) => {
  const labels = Object.keys(temas);
  const values = Object.values(temas);

  const chartData = {
    labels,
    datasets: [{
      label: 'Frecuencia por tema',
      data: values,
      backgroundColor: '#0d6efd',
    }]
  };

  return <Bar data={chartData} />;
};

export default BarChart;
