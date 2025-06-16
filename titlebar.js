const { ipcRenderer } = require('electron');

window.addEventListener('DOMContentLoaded', () => {
  const btnMinimize = document.getElementById('minimize');
  const btnMaximize = document.getElementById('maximize');
  const btnClose = document.getElementById('close');

  if (btnMinimize && btnMaximize && btnClose) {
    btnMinimize.addEventListener('click', () => {
      ipcRenderer.send('window-control', 'minimize');
    });

    btnMaximize.addEventListener('click', () => {
      ipcRenderer.send('window-control', 'maximize');
    });

    btnClose.addEventListener('click', () => {
      ipcRenderer.send('window-control', 'close');
    });

    ipcRenderer.on('window-maximized', (event, isMaximized) => {
      btnMaximize.textContent = isMaximized ? '🗗' : '☐';
    });
  }
});
