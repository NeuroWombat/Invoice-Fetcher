const { app, BrowserWindow } = require('electron');
const path = require('path');

let win;

const createWindow = () => {
    const win = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            nodeIntegration: true,
        },
    })

    win.loadFile(path.resolve(__dirname, "dist/index.html"));
}

app.whenReady().then(() => {
  createWindow();
})