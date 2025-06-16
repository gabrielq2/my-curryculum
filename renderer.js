const { ipcRenderer } = require('electron');

window.addEventListener('DOMContentLoaded', () => {
  // Botões da titlebar
  const btnMinimize = document.getElementById('minimize');
  const btnMaximize = document.getElementById('maximize');
  const btnClose = document.getElementById('close');

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

  // Botão para rodar script Python (se existir no HTML)
  const runPythonBtn = document.getElementById('runPython');
  if (runPythonBtn) {
    const { exec } = require('child_process');

    runPythonBtn.addEventListener('click', () => {
      exec('python D:\\dev\\estatistica\\seu_script.py', (error, stdout, stderr) => {
        if (error) {
          console.error(`Erro: ${error.message}`);
          alert(`Erro: ${error.message}`);
          return;
        }
        if (stderr) {
          console.error(`Stderr: ${stderr}`);
          alert(`Erro no script: ${stderr}`);
          return;
        }
        console.log(`Resultado: ${stdout}`);
        alert(`Resultado: ${stdout}`);
      });
    });
  }
});
