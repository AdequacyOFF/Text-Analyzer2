

function OutputText({ data }) {

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