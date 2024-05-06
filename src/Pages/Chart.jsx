import React from "react";
import "chart.js/auto";
import { Chart } from "react-chartjs-2";
import { Pie } from "react-chartjs-2"; // Remove this line

const Chart = ({ array }) => {
  console.log("Chart array: ", array);
  const pieChartData = {
    labels: [
      "joy_percent",
      "sadness_percent",
      "surprise_percent",
      "fear_percent",
      "anger_percent",
    ],
    datasets: [
      {
        data: [
          array["joy_percent"],
          array["sadness_percent"],
          array["surprise_percent"],
          array["fear_percent"],
          array["anger_percent"],
        ],
        label: "Text analysis based on emotions",
        backgroundColor: [
          "rgb(173, 173, 173)",
          "rgb(245, 213, 63)",
          "rgb(99, 111, 189)",
          "rgb(8, 232, 222)",
          "rgb(134, 219, 74)",
          "rgb(222, 44, 44)",
        ],
        hoverBackgroundColor: [
          "rgba(173, 173, 173,0.7)",
          "rgba(245, 213, 63,0.7)",
          "rgba(99, 111, 189,0.7)",
          "rgba(8, 232, 222,0.7)",
          "rgba(134, 219, 74,0.5)",
          "rgba(222, 44, 44,0.5)",
        ],
      },
    ],
  };
  const pieChart = (
    <Pie
      type="pie"
      width={130}
      height={50}
      options={{
        title: {
          display: true,
        },
        legend: {
          display: true, //Is the legend shown?
          position: "top", //Position of the legend.
        },
      }}
      data={pieChartData}
    />
  );
  return pieChart;
};
export default ChartDiogram;
