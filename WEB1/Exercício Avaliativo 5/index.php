<?php
function validarTelefone($telefone) {
    return preg_match('/^\(?\d{2}\)?\s?\d{4,5}-\d{4}$/', $telefone);
}

function validarURL($url) {
    return filter_var($url, FILTER_VALIDATE_URL);
}

function validarEmail($email) {
    return filter_var($email, FILTER_VALIDATE_EMAIL);
}

function validarData($data) {
    $partes = explode('/', $data);
    if (count($partes) == 3) {
        $dia = (int)$partes[0];
        $mes = (int)$partes[1];
        $ano = (int)$partes[2];
        return checkdate($mes, $dia, $ano);
    }
    return false;
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nome = $_POST['nome'] ?? '';
    $email = $_POST['email'] ?? '';
    $data_nascimento = $_POST['data_nascimento'] ?? '';
    $telefone = $_POST['telefone'] ?? '';
    $url = $_POST['url'] ?? '';
    $estado = $_POST['estado'] ?? '';

    $erros = [];

    if (empty($nome)) $erros[] = "O campo Nome é obrigatório.";
    if (empty($email) || !validarEmail($email)) $erros[] = "E-mail inválido.";
    if (empty($data_nascimento) || !validarData($data_nascimento)) $erros[] = "Data de nascimento inválida.";
    if (empty($telefone) || !validarTelefone($telefone)) $erros[] = "Telefone inválido.";
    if (empty($url) || !validarURL($url)) $erros[] = "URL inválida.";

    ?>
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <title>Resultado</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            ul { color: red; }
            a { text-decoration: none; color: blue; }
        </style>
    </head>
    <body>
    <?php
    if (count($erros) > 0) {
        echo "<h2>Erros encontrados:</h2><ul>";
        foreach ($erros as $erro) echo "<li>$erro</li>";
        echo "</ul><a href='".$_SERVER['PHP_SELF']."'>Voltar ao formulário</a>";
    } else {
        echo "<h2>Dados Recebidos:</h2>";
        echo "Nome: $nome <br>";
        echo "E-mail: $email <br>";
        echo "Data de Nascimento: $data_nascimento <br>";
        echo "Telefone: $telefone <br>";
        echo "URL: $url <br>";
        echo "Estado: $estado <br>";
    }
    ?>
    </body>
    </html>
    <?php
    exit;
}
?>

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Cadastro de Usuário</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        label {
            display: inline-block;
            width: 150px;
        }
        input[type="text"], input[type="email"] {
            width: 250px;
            padding: 5px;
        }
        input[type="submit"] {
            background-color: #3366CC;
            color: white;
            border: none;
            padding: 8px 16px;
            font-size: 14px;
            cursor: pointer;
        }
        input[type="submit"]:hover {
            background-color: #254e9b;
        }
        .campo {
            margin-bottom: 10px;
        }
        small {
            color: gray;
            margin-left: 5px;
        }
    </style>
</head>
<body>
    <form method="POST" action="">
        <div class="campo">
            <label>Nome completo: *</label>
            <input type="text" name="nome" placeholder="Seu nome aqui ...">
        </div>

        <div class="campo">
            <label>E-mail: *</label>
            <input type="text" name="email" placeholder="Seu e-mail aqui ...">
        </div>

        <div class="campo">
            <label>Data nascimento: *</label>
            <input type="text" name="data_nascimento" placeholder="dd/mm/aaaa">
            <small>(idade mínima 18 anos)</small>
        </div>

        <div class="campo">
            <label>Telefone: *</label>
            <input type="text" name="telefone" placeholder="(47)8181-6035">
        </div>

        <div class="campo">
            <label>URL página pessoal:</label>
            <input type="text" name="url">
        </div>

        <div class="campo">
            <label>Estado onde reside:</label>
            <input type="text" name="estado">
        </div>

        <input type="submit" value="Cadastrar-me">
    </form>
</body>
</html>
