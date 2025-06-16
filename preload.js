const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('api', {
  calcular: (data) => ipcRenderer.invoke('calcular', data)
});
