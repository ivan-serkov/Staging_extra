import React from "react";
import Meal from "./meal";

const Menu = (Meals) => {
    if (!Meals.length) {
        return <h1>Ничего нет</h1>
    }
    return (
        <div>
            {Meals.map(meal => <Meal Meal={meal} key={meal.id}/> )}
        </div>
    );
};

export default Menu