import React, { useEffect, useState } from 'react';
import ReactDOM from "react-dom/client";
import './App.css'

function App() {
    const [checked, setChecked] = useState(false);
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [output, setOutput] = useState("");


    const loginScript = () => {
        if (window.electronAPI) {
            window.electronAPI.runPythonScript(email, password);
        }else {
            console.error("window.electronAPI is not available!");
        }
    };

    React.useEffect(() => {
        if (window.electronAPI) {
            window.electronAPI.onScriptOutput((data) => {
                setOutput(data);
            });
        }
    }, []);


    return (
    <>
      <div id='banner'>
          <h2>Invoice-Fetcher</h2>
      </div>
      <div id='opcja1'>
        <form>
            <label>E-mail</label><input type='text' value={email} onChange={(e) => setEmail(e.target.value)}></input>
            <label>Password</label><input type='password' value={password} onChange={(e) => setPassword(e.target.value)}></input>
            <div className="remember-me">
                <input type="checkbox" id="remember" onChange={(e) => setChecked(e.target.checked)}/>
                <label htmlFor="remember">Remember me</label>
            </div>
            <button onClick={loginScript}>Log in</button>
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

      <p>Output: {output}</p>
    </>
  )
}

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
export default App