import * as vscode from 'vscode';
import * as fs from 'fs';
import * as path from 'path';

export function activate(context: vscode.ExtensionContext) {
  let disposable = vscode.commands.registerCommand('photon.createProject', async () => {
    // Demander à l'utilisateur de fournir un chemin pour le projet
    const projectPath = await vscode.window.showInputBox({ prompt: "Enter the path for the new Photon project" });
    
    if (projectPath) {
      // Créer le dossier du projet
      if (!fs.existsSync(projectPath)) {
        fs.mkdirSync(projectPath, { recursive: true });
      }

      // Ajouter un fichier main.photon
      const mainPhotonPath = path.join(projectPath, 'main.photon');
      fs.writeFileSync(mainPhotonPath, '// Your Photon code here\n');

      // Copier le dossier PhotonIDE
      const photonIDESource = path.join(context.extensionPath, 'PhotonIDE');
      copyDirectory(photonIDESource, projectPath);

      // Ouvrir le dossier du projet dans VS Code
      const uri = vscode.Uri.file(projectPath);
      vscode.commands.executeCommand('vscode.openFolder', uri);
    }
  });

  context.subscriptions.push(disposable);
}

function copyDirectory(src: string, dest: string) {
	// Vérifier si la destination est le dossier PhotonIDE lui-même
	const lastFolderName = path.basename(src);
	const finalDestination = dest.endsWith(lastFolderName) ? dest : path.join(dest, lastFolderName);
  
	// Créer le dossier de destination s'il n'existe pas
	if (!fs.existsSync(finalDestination)) {
	  fs.mkdirSync(finalDestination, { recursive: true });
	}
  
	// Copier le contenu du dossier source dans le dossier de destination
	fs.readdirSync(src, { withFileTypes: true }).forEach(dirent => {
	  const source = path.join(src, dirent.name);
	  const destination = path.join(finalDestination, dirent.name);
  
	  if (dirent.isDirectory()) {
		copyDirectory(source, destination);
	  } else {
		fs.copyFileSync(source, destination);
	  }
	});
  }
  

export function deactivate() {}
