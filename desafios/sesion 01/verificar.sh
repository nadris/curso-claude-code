#!/usr/bin/env bash
# Verificación ejecutable del contrato de la sesión 01 (ver contrato.md).
# El cambio real vive en desafios/sesion 02 (ver evidencia.md para el porqué).
set -euo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")/../sesion 02"

docker compose up --abort-on-container-exit --exit-code-from tests
docker compose down -v
