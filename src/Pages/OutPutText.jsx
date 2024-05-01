import React from "react";

function OutputText() {
  fetch("http://127.0.0.1:8080/filesUpload")
    .then((response) => {
      if (response.status !== 200) {
        return Promise.reject(new Error(response.statusText));
      }
      return response.json();
    })
    .then((data) => {
      const parsedData = JSON.parse(data);

      return (
        <div>
          {parsedData.map((item, index) => (
            <span key={index} className={item[1] + " output-text"}>
              {item[0]}{" "}
            </span>
          ))}
        </div>
      );
    });
}

export default OutputText;
