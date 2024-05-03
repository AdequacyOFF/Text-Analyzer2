import React from "react";

function OutputText({array}) {
  console.log(array);
      return (
        <div>
          {array.slice(0, array.length-1).map((item, index) => (
            <span key={index} className={item["conclusion"] + " output-text"}>
              {item["text"]}{" "}
            </span>
          ))}
        </div>
      );
}

export default OutputText;