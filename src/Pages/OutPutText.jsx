import React from "react";
import { Mychart } from "./Chart.jsx";

function OutputText({ array }) {
  console.log(array);

  return (
    <div>
      {array.slice(0, array.length - 1).map((item, index) => (
        <span key={index} className={item["conclusion"] + " output-text"}>
          {item["text"]}
          {
            <div className="Diogram">
              <Mychart array={item} />
            </div>
          }
          {item["profanity_flag"] && (
            <div className="profanity_flag_block">
              <span className="profanity_flag"><span className="profanity_flag_attention">Внимание:</span>Текст содержит ненормативную лексику</span>
            </div>
          )}
        </span>
      ))}
      {array[1] && (
        <div className="Diogram">
          <TotalChart array={array[array.length - 1]} />
        </div>
      )}
    </div>
  );
}

export default OutputText;
