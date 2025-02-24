const { app, BrowserWindow, ipcMain } = require('electron');
const { spawn } = require('child_process');
const path = require('path');

let win;

const createWindow = () => {
    const win = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            preload: path.join(__dirname, 'preload.js'),
            contextIsolation: true,
            enableRemoteModule: false,
            nodeIntegration: true,
        },
    })

    win.loadFile(path.resolve(__dirname, "dist/index.html"));
}

app.whenReady().then(() => {
  createWindow();
})


ipcMain.on('loginScript', (event, args) => {
    const pythonScript = spawn("python", [path.join(__dirname, "/scripts/main.py"), args.email, args.password]);

    pythonScript.stdout.on("data", (output) => {
        console.log(`Output: ${output}`);
        event.reply("scriptOutput", output.toString());
    });

    pythonScript.stderr.on("data", (error) => {
        console.error(`Error: ${error}`);
        event.reply("scriptOutput", `Error: ${error.toString()}`);
    });
});
