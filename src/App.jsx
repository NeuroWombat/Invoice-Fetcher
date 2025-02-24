import React from 'react';
import ReactDOM from "react-dom/client";
import './App.css'

function App() {
  return (
    <>
      <div id='banner'>
          <h2>Invoice-Fetcher</h2>
      </div>
      <div id='opcja1'>
        <form>
            <label>E-mail</label><input type='text'></input>
            <label>Password</label><input type='password'></input>
            <div className="remember-me">
                <input type="checkbox" id="remember"/>
                <label htmlFor="remember">Remember me</label>
            </div>
            <button onclick={() => console.log("testing")}>Log in</button>
        </form>
      </div>

      <div id='opcja2'>
        <form>
            <label>Time period</label><select></select>
            <label>Start date</label>
            <label>End date</label>

            <label>Choose directory for invoices:</label><input type="file" webkitdirectory directory onChange={(e) => console.log(e.target.files)} />
            <label>Do you want to print invoices?</label><input type='checkbox'></input>

            <button>Download invoices</button>
        </form>
      </div>
    </>
  )
}

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
export default App