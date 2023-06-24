<html>
<head>
    <title>Resultado del juego</title>
</head>
<body>
    <h1>Resultado del juego</h1>
    <h2>Jugadores:</h2>
    <ul>
        % for jugador in jugadores:
            <li>{{ jugador }}</li>
        % end
    </ul>
    <h2>Jugadas:</h2>
    <table>
        <tr>
            <th>Jugador ID</th>
            <th>Valor de la jugada</th>
        </tr>
        % for jugada in jugadas:
            <tr>
                <td>{{ jugada['jugador_id'] }}</td>
                <td>{{ jugada['valor_jugada'] }}</td>
            </tr>
        % end
    </table>
    <h2>Jugador ganador:</h2>
    <p>{{ jugador_ganador }}</p>
    <h2>Puntaje acumulado:</h2>
    <ul>
        % for jugador, puntaje in puntaje_acumulado.items():
            <li>{{ jugador }}: {{ puntaje }}</li>
        % end
    </ul>
</body>
</html>
