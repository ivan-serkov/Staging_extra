import Menu from "./menu";
import axios from "axios";
import {useState} from "react";

const API_URL = 'http://127.0.0.1:8000/api/meal/'

function
App() {
    const [Meals, setMeals] = useState([])

    async function getMeals() {
        const response = await axios.get(API_URL)
        setMeals(response.data)
    }

    return (
        <div className="App">
            <button onClick={getMeals}>Обновить</button>
            <h1>Помыть деда</h1>
            <h2>Обильно тёплой водой</h2>
            <Menu meals={Meals}/>
        </div>

    );
}

export default App;
