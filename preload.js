const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('electronAPI', {
  runPythonScript: (email, password) => {
      console.log("Sending request to Electron with:", email, password);
      ipcRenderer.send('loginScript', { email, password });
  },
  onScriptOutput: (callback) => {
      ipcRenderer.on('scriptOutput', (_event, data) => {
          console.log("Received script output:", data);
          callback(data);
      });
  }
});