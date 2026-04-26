# Commit Bot

Bot automático que realiza commits diarios de manera realista en el archivo de logs.

## Características

- **Variabilidad**: 1-8 commits aleatorios por ejecución
- **Naturalidad**: Salta días aleatoriamente (~30% de probabilidad)
- **Sin patrones**: Mensajes variados y horarios múltiples
- **GitHub Actions**: Se ejecuta automáticamente sin requiere servidor

## Configuración

1. Conecta este repositorio a GitHub:
```bash
git remote add origin https://github.com/TU_USUARIO/bot-commit.git
git branch -M main
git push -u origin main
```

2. El workflow se ejecutará automáticamente según el cronograma configurado en `.github/workflows/commit-bot.yml`

## Logs

El archivo `logs/activity.log` se modifica con cada ejecución del bot con entradas como:
```
[2026-04-25T10:15:30.123456] operation successful
[2026-04-25T10:15:35.654321] check passed
```

## Personalización

Edita `scripts/commit_bot.py` para cambiar:
- `MESSAGES`: Mensajes de commit más realistas según tu contexto
- `skip_day()`: Probabilidad de saltar un día
- `num_commits()`: Distribución de commits
