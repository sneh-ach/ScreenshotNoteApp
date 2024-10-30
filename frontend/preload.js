const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('electronAPI', {
    onScreenshotTaken: (callback) => ipcRenderer.on('screenshot-taken', callback)
});
