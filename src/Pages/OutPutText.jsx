import React from "react";
// import { Chart } from "react-chartjs-2";
import Chart from './Chart';

function OutputText({array}) {
  console.log(array);
  const data = {
    joy_percent: 20,
    sadness_percent: 30,
    surprise_percent: 15,
    fear_percent: 25,
    anger_percent: 10,
  };
      return (
        <div>
          {array.slice(0, array.length-1).map((item, index) => (
            <span key={index} className={item["conclusion"] + " output-text"}>
              {item["text"]}
              {item["array"] && (
                <div className="Diogram">
                  <Chart array={data}/>
                </div>)}
            </span>
          ))}
        </div>
      );
}

export default OutputText;