import React from 'react';
import PieChart from './PieChart';

const Chart = ({ array }) => {
  console.log('Chart array: ', array);
  const pieChartData = [
    { label: 'joy_percent', value: array['joy_percent'] },
    { label: 'sadness_percent', value: array['sadness_percent'] },
    { label: 'surprise_percent', value: array['surprise_percent'] },
    { label: 'fear_percent', value: array['fear_percent'] },
    { label: 'anger_percent', value: array['anger_percent'] },
  ];

  return <PieChart data={pieChartData} />;
};

export default Chart;