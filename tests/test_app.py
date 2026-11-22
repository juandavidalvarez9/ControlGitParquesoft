from app.main import app


def test_la_pagina_principal_carga_el_juego():
    respuesta = app.test_client().get("/")

    assert respuesta.status_code == 200
    assert b"startGame()" in respuesta.data


def test_una_ruta_desconocida_responde_404():
    assert app.test_client().get("/no-existe").status_code == 404
