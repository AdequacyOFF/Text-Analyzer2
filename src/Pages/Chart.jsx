import React from 'react';
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js';
import { Pie } from 'react-chartjs-2';

ChartJS.register(ArcElement, Tooltip, Legend);

export function Mychart(array) {
  console.log("Chart array: ", array);
  const data = {
  labels: ["joy_percent",
      "sadness_percent",
      "surprise_percent",
      "fear_percent",
      "anger_percent"],
  datasets: [
    {
      label: "Text analysis based on emotions",
      data: [array["array"]["joy_percent"],
          array["array"]["sadness_percent"],
          array["array"]["surprise_percent"],
          array["array"]["fear_percent"],
          array["array"]["anger_percent"]],
      backgroundColor: [
        "rgb(173, 173, 173)",
          "rgb(245, 213, 63)",
          "rgb(99, 111, 189)",
          "rgb(8, 232, 222)",
          "rgb(134, 219, 74)",
          "rgb(222, 44, 44)"
      ],
      borderColor: [
        "rgba(173, 173, 173,0.7)",
          "rgba(245, 213, 63,0.7)",
          "rgba(99, 111, 189,0.7)",
          "rgba(8, 232, 222,0.7)",
          "rgba(134, 219, 74,0.5)",
          "rgba(222, 44, 44,0.5)"
      ],
      borderWidth: 1,
    },
  ],
};
  return <Pie data={data} 
              width={200}
              height={200}
              options={{ maintainAspectRatio: false }}/>;
}
