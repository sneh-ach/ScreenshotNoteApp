const { app, BrowserWindow, globalShortcut } = require('electron');
const path = require('path');
const axios = require('axios');

function createWindow() {
    const win = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            preload: path.join(__dirname, 'preload.js'),
            contextIsolation: true,
        },
    });
    win.loadFile('index.html');

    globalShortcut.register('Ctrl+Shift+S', async () => {
        await axios.get('http://127.0.0.1:5000/screenshot');
        win.webContents.send('screenshot-taken');
    });
}

app.whenReady().then(createWindow);

app.on('will-quit', () => {
    globalShortcut.unregisterAll();
});
