import React from "react";

function OutputText() {

    fetch('https://...')
     .then(function(response) {
        if (response.status!== 200) {
          return Promise.reject(new Error(response.statusText));
        }
        return response.json();
      })
     .then(function(data) {
        const sentence0 = data['sentence0'];
        const conclusion0 = data['conclusion0'];
        const neutral_p0 = data['neutral_p0'];
        const joy_p0 = data['joy_p0'];
        const sadness_p0 = data['sadness_p0'];
        const surprise_p0 = data['surprise_p0'];
        const fear_p0 = data['fear_p0'];
        const anger_p0 = data['anger_p0'];
        const sentence1 = data['sentence1'];
        const conclusion1 = data['conclusion1'];
        const neutral_p1 = data['neutral_p1'];
        const joy_p1 = data['joy_p1'];
        const sadness_p1 = data['sadness_p1'];
        const surprise_p1 = data['surprise_p1'];
        const fear_p1 = data['fear_p1'];
        const anger_p1 = data['anger_p1'];
        const sentence2 = data['sentence2'];
        const conclusion2 = data['conclusion2'];
        const neutral_p2 = data['neutral_p2'];
        const joy_p2 = data['joy_p2'];
        const sadness_p2 = data['sadness_p2'];
        const surprise_p2 = data['surprise_p2'];
        const fear_p2 = data['fear_p2'];
        const anger_p2 = data['anger_p2'];
        const total_neutral_p = data['total_neutral_p'];
        const total_joy_p = data['total_joy_p'];
        const total_sadness_p = data['total_sadness_p'];
        const total_surprise_p = data['total_surprise_p'];
        const total_fear_p = data['total_fear_p'];
        const total_anger_p = data['total_anger_p'];
      })
     .catch(function(error) {
        console.log('error', error);
    });

    return (
            <div>
                {data.map((item, index) => (
                <span key={index} className={item[1] + ' output-text'}>{item[0]} </span>
            ))
            }
            </div>
            
    );
}




export default OutputText;