---
paths:
  - "tests/**/*.py"
---

# Reglas de pruebas

- Los tests de persistencia se ejecutan contra PostgreSQL, no SQLite.
- Antes de corregir una regresión, confirma que el test falla por el comportamiento ausente.
