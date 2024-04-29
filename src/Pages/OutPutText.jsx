import React from "react";

function OutputText() {

    // fetch('https://...')
    //  .then(function(response) {
    //     if (response.status!== 200) {
    //       return Promise.reject(new Error(response.statusText));
    //     }
    //     return response.json();
    //   })
    //  .then(function(data) {
    //     const sentence = data['sentence0'];
    //     const conclusion = data['conclusion0'];
    //     const neutral_p = data['neutral_p0'];
    //     const joy_p = data['joy_p0'];
    //     const sadness_p = data['sadness_p0'];
    //     const surprise_p = data['surprise_p0'];
    //     const fear_p = data['fear_p0'];
    //     const anger_p = data['anger_p0'];
    //   })
    //  .catch(function(error) {
    //     console.log('error', error);
    // });

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