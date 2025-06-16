const { app, BrowserWindow } = require('electron');
const path = require('path');

function createWindow() {
  win = new BrowserWindow({
    width: 800,
    height: 600,
    frame: false,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false,
    },
  });

  win.loadFile(path.join(__dirname, 'index.html'));

  win.webContents.on('did-finish-load', () => {
    // Envia estado inicial da janela
    win.webContents.send('window-maximized', win.isMaximized());
  });

  win.on('maximize', () => {
    win.webContents.send('window-maximized', true);
  });

  win.on('unmaximize', () => {
    win.webContents.send('window-maximized', false);
  });
}


app.whenReady().then(createWindow);

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  if (BrowserWindow.getAllWindows().length === 0) {
    createWindow();
  }
});

const { ipcMain } = require('electron');
const { exec } = require('child_process');
ipcMain.on('window-control', (event, action) => {
  const win = BrowserWindow.fromWebContents(event.sender);
  if (action === 'minimize') win.minimize();
  else if (action === 'maximize') {
    if (win.isMaximized()) win.unmaximize();
    else win.maximize();
  }
  else if (action === 'close') win.close();
});

ipcMain.handle('run-python-script', async () => {
  return new Promise((resolve, reject) => {
    exec('python D:\\dev\\estatistica\\backend.py', (error, stdout, stderr) => {
      if (error) {
        reject(`Erro: ${stderr}`);
      } else {
        resolve(stdout);
      }
    });
  });
});
