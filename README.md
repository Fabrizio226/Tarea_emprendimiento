# Lumenia

## Publicar en GitHub Pages

El workflow de GitHub Actions genera el sitio estático y lo publica cuando se actualiza el repositorio. En GitHub, abre **Settings → Pages** y selecciona **GitHub Actions** como origen de publicación. También puedes iniciar el workflow manualmente desde la pestaña **Actions**.

La exportación incluye las páginas públicas y sus recursos estáticos. No incluye `formularios.db` ni la página de registros en el sitio publicado. Si el repositorio será público, comprueba además que los archivos versionados no contengan datos personales: el contenido del repositorio puede descargarse aunque no forme parte de Pages.

### Limitación de las solicitudes

GitHub Pages solo aloja archivos estáticos: no ejecuta Flask ni SQLite. Por eso, los formularios publicados informan que no se envían ni se guardan. Para habilitar reservas y cancelaciones, hay que conectar un backend alojado por separado. La aplicación Flask original sigue disponible para ejecutarse localmente.

Para generar el sitio en tu equipo:

```powershell
python scripts\build_pages.py
```

El resultado queda en `_site`.
