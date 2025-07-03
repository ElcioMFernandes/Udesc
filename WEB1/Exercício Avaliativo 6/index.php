<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    header('Content-Type: application/json');

    $dataFile = 'usuarios.json';

    function getUsuarios($file) {
        if (!file_exists($file)) {
            return [];
        }
        $json_data = file_get_contents($file);
        return json_decode($json_data, true) ?: [];
    }

    function saveUsuarios($file, $data) {
        $json_data = json_encode($data, JSON_PRETTY_PRINT);
        file_put_contents($file, $json_data);
    }

    $action = $_POST['action'] ?? '';
    $login = $_POST['login'] ?? '';
    $senha = $_POST['senha'] ?? '';

    if (empty($action) || empty($login) || empty($senha)) {
        echo json_encode(['success' => false, 'message' => 'Todos os campos são obrigatórios.']);
        exit;
    }

    $usuarios = getUsuarios($dataFile);

    switch ($action) {
        case 'criar':
            if (isset($usuarios[$login])) {
                echo json_encode(['success' => false, 'message' => 'Erro: Login já existente.']);
            } else {
                $hashSenha = password_hash($senha, PASSWORD_DEFAULT);
                $usuarios[$login] = ['senha' => $hashSenha];
                saveUsuarios($dataFile, $usuarios);
                echo json_encode(['success' => true, 'message' => 'Usuário criado com sucesso!']);
            }
            break;

        case 'verificar':
            if (isset($usuarios[$login]) && password_verify($senha, $usuarios[$login]['senha'])) {
                echo json_encode(['success' => true, 'message' => 'Login e senha corretos!']);
            } else {
                echo json_encode(['success' => false, 'message' => 'Login ou senha inválidos.']);
            }
            break;

        default:
            echo json_encode(['success' => false, 'message' => 'Ação desconhecida.']);
            break;
    }
    exit;
}
?>
<!DOCTYPE html>
<html lang="pt-br">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Sistema de Login</title>
  </head>
  <body>
    <div class="login-container">
      <h1>Autenticação</h1>
      <form id="loginForm" onsubmit="return false;">
        <div class="input-group">
          <label for="login">Login:</label>
          <input type="text" id="login" name="login" placeholder="Seu login aqui" required />
        </div>
        <div class="input-group">
          <label for="senha">Senha:</label>
          <input type="password" id="senha" name="senha" placeholder="Sua senha aqui" required />
        </div>
        <div class="button-group">
          <button type="button" id="btnCriar">CRIAR</button>
          <button type="button" id="btnVerificar">VERIFICAR</button>
        </div>
      </form>
      <div id="responseMessage" class="message"></div>
    </div>

    <script>
      document.addEventListener("DOMContentLoaded", () => {
        const btnCriar = document.getElementById("btnCriar");
        const btnVerificar = document.getElementById("btnVerificar");
        const responseMessage = document.getElementById("responseMessage");

        const handleRequest = async (action) => {
          const login = document.getElementById("login").value;
          const senha = document.getElementById("senha").value;

          responseMessage.textContent = "";
          responseMessage.className = "message";

          if (!login || !senha) {
            displayMessage("Por favor, preencha o login e a senha.", "error");
            return;
          }

          const formData = new FormData();
          formData.append("action", action);
          formData.append("login", login);
          formData.append("senha", senha);

          try {
            const response = await fetch("index.php", {
              method: "POST",
              body: formData,
            });

            const result = await response.json();

            if (result.success) {
              displayMessage(result.message, "success");
            } else {
              displayMessage(result.message, "error");
            }
          } catch (error) {
            console.error("Erro na requisição:", error);
            displayMessage("Ocorreu um erro de comunicação com o servidor.", "error");
          }
        };

        const displayMessage = (message, type) => {
          responseMessage.textContent = message;
          responseMessage.className = `message ${type}`;
        };

        btnCriar.addEventListener("click", () => handleRequest("criar"));
        btnVerificar.addEventListener("click", () => handleRequest("verificar"));
      });
    </script>
  </body>
</html>