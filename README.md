Assistant Pascal
Description du projet
L'assistant Pascal est un programme qui utilise l'API de génération de texte de OpenAI pour créer un chatbot qui peut répondre à des questions posées par l'utilisateur. Il peut également reconnaître la voix de l'utilisateur et lui répondre verbalement.

-Installation
Cloner le dépôt Git en utilisant git clone https://github.com/username/assistant-pascal.git.
Installer les dépendances avec la commande pipenv install.
Configurer les clés API OpenAI en créant un fichier .env avec les informations suivantes :
OPENAI_API_KEY=YOUR_API_KEY_HERE
MODEL_ENGINE=YOUR_MODEL_ENGINE_HERE

Exécuter le programme avec la commande pipenv run python main.py.

-Utilisation
L'utilisateur peut poser des questions à l'assistant en tapant directement dans la console ou en parlant dans le microphone. L'assistant répondra à chaque question avec une réponse générée par l'API de OpenAI. Pour parler à l'assistant, il suffit de dire "Bonjour Pascal" ou de taper "Bonjour Pascal" dans la console.

-Configuration
L'assistant Pascal nécessite une configuration initiale pour fonctionner correctement. Les clés API OpenAI doivent être configurées dans le fichier .env, comme indiqué dans la section d'installation. Le modèle utilisé pour générer les réponses peut également être configuré en modifiant la variable MODEL_ENGINE dans le fichier .env.

-Contribution
Les contributions à ce projet sont les bienvenues. Pour contribuer, veuillez suivre les étapes suivantes :

Forker le dépôt.
Créer une nouvelle branche pour votre contribution (git checkout -b my-new-feature).
Faire les modifications nécessaires et les tester localement.
Pousser les modifications vers votre fork (git push origin my-new-feature).
Créer une demande de fusion vers le dépôt d'origine.
-Licence
Ce projet est sous licence MIT. Voir le fichier LICENCE pour plus d'informations.
