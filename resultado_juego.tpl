<h1>Resultado del Juego</h1>

<ul>
% for jugador, jugada in zip(jugadores, jugadas):
    <li>Jugador: {{jugador}} - Jugada: {{jugada}}</li>
% end
</ul>

<p>Jugador Ganador: {{jugador_ganador}}</p>

<h3>Puntajes acumulados:</h3>
<ul>
% for jugador, puntaje in puntajes.items():
    <li>Jugador: {{jugador}} - Puntaje: {{puntaje}}</li>
% end
</ul>
