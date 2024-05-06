import React from "react";
// import { Chart } from "react-chartjs-2";
import Chart from './Chart';

function OutputText({array}) {
  console.log(array);
      return (
        <div>
          {array.slice(0, array.length-1).map((item, index) => (
            <span key={index} className={item["conclusion"] + " output-text"}>
              {item["text"]}
              {item["array"] && (
                <div className="Diogram">
                  <Chart array={item["array"]}
                    width={400} // Set the width of the chart to 400 pixels
                    height={200} // Set the height of the chart to 200 pixels
                  />
                </div>)}
            </span>
          ))}
        </div>
      );
}

export default OutputText;