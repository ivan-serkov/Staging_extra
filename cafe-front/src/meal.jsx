import React from "react";

const Meal = (props) => {
    return(
        <div className="meal">
            <strong>{props.Meal}</strong>
            <p>{props.id}</p>
        </div>
    )
}

export default Meal;