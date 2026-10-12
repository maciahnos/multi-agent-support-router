# Software y Herramientas en Nimbus Cloud

Esta guía reúne el catálogo de software aprobado en Nimbus Cloud, las reglas de uso de las herramientas centrales de trabajo y el proceso para pedir licencias. Está pensada para los aproximadamente 300 empleados de Buenos Aires y LATAM. El inventario oficial de aplicaciones y licencias lo mantiene el equipo de Soporte IT junto a Compras en el sistema **SaaSLedger** (ficticio), y se revisa en forma trimestral.

## 1. Catálogo de software aprobado

Todo el software que se usa en la empresa tiene que estar en el catálogo. Se divide en tres categorías según el nivel de revisión que tuvo:

- **Categoría A (estándar)**: instalado por defecto o disponible en Nimbus Self Service sin aprobación. Ejemplos: Google Chrome gestionado, Slack, Zoom, Google Drive para escritorio, 1Password, Okta Verify, Visual Studio Code, Notion Calendar no, pero sí Google Calendar.
- **Categoría B (con aprobación del manager)**: se instala tras aprobación. Ejemplos: Figma, Adobe Creative Cloud, Postman Team, DataGrip, Tableau Desktop, Miro.
- **Categoría C (con revisión de seguridad)**: requiere evaluación de SecOps y Legal por tratar datos sensibles o tener integraciones. Ejemplos: herramientas de IA generativa externas, nuevos SaaS que se conecten a Google Workspace, extensiones de navegador con permisos amplios.

Herramientas principales por función:

| Función | Herramienta | Responsable |
|---|---|---|
| Comunicación | Slack Enterprise Grid | IT |
| Correo, calendario, documentos | Google Workspace Business Plus | IT |
| Gestión de proyectos | Jira Software Cloud + Confluence | PMO |
| Código | GitHub Enterprise Cloud | Ingeniería |
| Reuniones | Zoom Workplace | IT |
| Diseño | Figma Organization | Diseño |
| CRM | Salesforce-like interno "NimbusCRM" | Ventas Ops |
| Monitoreo | Grafana Cloud + PagerDuty | SRE |
| Gestor de contraseñas | 1Password Business | SecOps |

Para ver qué hay disponible, abrí **Nimbus Self Service** desde el dock (macOS) o desde el menú Inicio (Windows). Para descubrir una herramienta que no está en la lista, consultá antes de comprarla o registrarte con tu correo corporativo: las "cuentas en la sombra" (shadow IT) son un riesgo de seguridad y de fuga de datos.

## 2. Slack

Slack es el canal principal de comunicación interna. Reglas y convenciones:

- Los canales públicos siguen el prefijo por función: `#eq-` para equipos (`#eq-ingenieria`), `#proy-` para proyectos, `#it-` para soporte técnico (`#it-ayuda`, `#it-urgente`), `#inc-` para incidentes y `#soc-` para temas sociales.
- `#it-ayuda` es para consultas rápidas no urgentes. Respondemos en horario de 9:00 a 18:00 (hora de Buenos Aires). Para incidentes con impacto, usá el ticket o `#it-urgente`.
- Los mensajes directos y los canales privados no deben contener contraseñas, claves de API, números de tarjeta ni datos personales de clientes. Si pasó, borralo y avisá a SecOps.
- La retención de mensajes es de 2 años; los mensajes directos se retienen por 1 año. Los canales de incidentes se archivan, no se borran.
- Las integraciones y bots (como el bot de Jira o el de PagerDuty) se solicitan por ticket y requieren revisión de SecOps (categoría C).

Atajos útiles: `/remind` para recordatorios, `/huddle` para llamadas rápidas dentro de Slack, y el flujo **Pedir ayuda IT** en `/helpdesk` que abre un ticket sin salir de Slack.

## 3. Google Workspace

Nimbus usa Google Workspace Business Plus con dominio `nimbuscloud.example`. Incluye Gmail, Calendar, Drive, Docs, Sheets, Slides, Meet y Chat (este último deshabilitado, ya que se usa Slack).

Reglas principales:

1. **Almacenamiento**: 5 TB por usuario en el Drive de la organización. Se avisa al 90 % de la cuota.
2. **Unidades compartidas**: todo documento de trabajo debe vivir en una unidad compartida del equipo (por ejemplo "Drive Ingeniería"), no en el Drive personal. Así el conocimiento no se pierde cuando alguien se va.
3. **Compartir con externos**: permitido solo con cuentas de dominios en la lista de dominios aprobados, o bajo el permiso "Solo ver" con vencimiento a 30 días. Para compartir por enlace público necesitás aprobación de SecOps.
4. **Gmail**: el tamaño máximo de adjunto es de 25 MB; para archivos más grandes se usa un enlace de Drive. Los correos con más de 5 destinatarios externos pasan por una advertencia de prevención de pérdida de datos (DLP).
5. **Calendar**: las reuniones deben tener enlace de Meet o Zoom, agenda breve y el horario de trabajo configurado. Las reuniones en LATAM consideran las zonas horarias de Buenos Aires (GMT-3), Santiago (GMT-3/-4 según estación), Bogotá (GMT-5) y Ciudad de México (GMT-6).
6. **Papelera**: los archivos borrados se pueden recuperar durante 30 días desde Drive > Papelera. Pasado ese plazo, Soporte puede restaurarlos hasta 25 días más desde Admin Console.

Si aparece el error "Se superó la cuota de transferencia" (`GWS-DRV-429`), esperá 24 horas o pedí a Soporte que revise el uso anómalo.

## 4. Jira y Confluence

Jira Software Cloud (instancia `nimbuscloud.atlassian.example`) es la herramienta de gestión de trabajo para Ingeniería, Producto y varios equipos operativos. Confluence aloja la documentación técnica y de procesos.

Estructura:

- Cada squad tiene un proyecto Jira con clave de 3 a 4 letras (`PLT` para Plataforma, `BIL` para Facturación, `MOB` para Mobile, `DAT` para Datos).
- Los tipos de issue son: Épica, Historia, Tarea, Bug y Spike. Los bugs deben incluir pasos para reproducir, ambiente y severidad (S1 a S4).
- Los flujos de trabajo estándar: `Backlog > Listo > En curso > En revisión > QA > Hecho`.
- Los sprints duran 2 semanas, de martes a lunes, con planning el primer martes.

Cómo pedir acceso: entrá a Nimbus Helpdesk > *Accesos > Jira/Confluence*, indicá el proyecto y el rol (Visualizador, Colaborador o Administrador de proyecto). Los administradores globales de Jira son solo 3 personas del equipo de PMO e IT.

Los pedidos de IT en sí mismos se gestionan en Nimbus Helpdesk, que es una instancia separada con Jira Service Management; no se deben abrir tickets de soporte en los proyectos de los squads.

## 5. GitHub

La organización `nimbus-cloud` está en GitHub Enterprise Cloud con SSO de Okta obligatorio. Reglas:

1. El acceso se solicita por ticket y se aprueba por el Engineering Manager. Se asigna a equipos (`team-plataforma`, `team-mobile`) y no a repos individuales.
2. Los commits deben estar firmados (GPG o SSH). Los repos principales exigen firma, 2 aprobaciones en el pull request y checks de CI en verde antes del merge.
3. Está prohibido commitear secretos. El escaneo de secretos (*secret scanning*) bloquea el push con el mensaje `GH-PUSH-SECRET-001`. Si te pasa, rotá la credencial de inmediato y avisá a SecOps; borrar el commit no alcanza.
4. Los repositorios públicos solo se crean con aprobación de Legal y Producto.
5. Los tokens personales (PAT) clásicos están deshabilitados; usá tokens de grano fino con vencimiento máximo de 90 días.
6. La autorización SSO de tu clave SSH se hace en *GitHub > Settings > SSH and GPG keys > Configure SSO > Authorize*. Si recibís `403 Resource protected by organization SAML enforcement`, es lo que falta.

Los pipelines corren en GitHub Actions con runners autoalojados en la VPC de staging y publican en el registry de artefactos interno.

## 6. Zoom

Zoom Workplace es la herramienta oficial para reuniones externas con clientes y para webinars. Para reuniones internas se admite Google Meet. Detalles:

- Licencia **Básica Corporativa**: reuniones de hasta 30 horas y 100 participantes, grabación en la nube por 90 días.
- Licencia **Webinar 500**: se asigna a Marketing y Customer Success, para eventos de hasta 500 asistentes.
- Todas las reuniones tienen código de acceso y sala de espera activada por defecto.
- Las grabaciones se almacenan en `Zoom > Grabaciones` y se eliminan automáticamente a los 90 días. Si necesitás conservarla, pasala a Drive.
- Antes de unirte, probá el audio en *Ajustes > Audio > Probar altavoz y micrófono*.

Los problemas de video y audio se tratan en el archivo de red y troubleshooting (códigos Zoom `1001`, `3000`, `5003`).

## 7. Licencias: cómo pedirlas

Las licencias se administran de forma centralizada para evitar pagos duplicados y cumplir con los contratos. Procedimiento:

1. Revisá en Nimbus Self Service si ya está disponible (categoría A).
2. Si no, abrí un ticket en *Software > Solicitud de licencia*, indicando: nombre del producto, versión, motivo de negocio, duración (permanente, proyecto de X meses) y centro de costo.
3. Tu manager aprueba en un máximo de 2 días hábiles.
4. Si el costo anual supera USD 500 por licencia o USD 3.000 en total, interviene Finanzas (3 días hábiles más).
5. Si la herramienta no está en el catálogo, SecOps hace una revisión (hasta 10 días hábiles) que incluye cuestionario del proveedor, cumplimiento (SOC 2, ISO 27001) y ubicación de los datos.
6. Compras adquiere la licencia y Soporte la asigna a tu usuario. El tiempo total típico para categoría B es de 3 a 5 días hábiles.

Recuperación de licencias: si una licencia no se usa durante 60 días, SaaSLedger envía un aviso y, a los 90 días, se reasigna. Esto ahorra aproximadamente un 12 % del gasto anual en software. Si necesitás conservarla, respondé el aviso.

Las licencias de personas que se van se reclaman en el offboarding. Los costos aproximados por licencia mensual: Figma USD 15, Adobe Creative Cloud USD 55, JetBrains DataGrip USD 25, Zoom Webinar USD 79.

## 8. Software prohibido

Por razones de seguridad, licenciamiento o privacidad, está prohibido instalar o usar en equipos corporativos:

- Software pirata o cracks, keygens y activadores (violación de licencia y vector de malware).
- Servicios de almacenamiento personal para archivos de trabajo: Dropbox personal, WeTransfer, Mega, Google Drive personal.
- Mensajería personal para comunicaciones laborales con clientes: WhatsApp personal, Telegram. Se permite WhatsApp Business en la cuenta oficial de Ventas.
- Clientes de torrents (BitTorrent, qBittorrent).
- Herramientas de acceso remoto no aprobadas: AnyDesk, TeamViewer, Chrome Remote Desktop. La herramienta autorizada es la asistencia remota de Jamf/Intune, y la VPN para acceso.
- VPN personales o proxies anónimos en el equipo corporativo.
- Extensiones de navegador no gestionadas con permiso "Leer y cambiar todos los datos de los sitios".
- Herramientas de IA generativa no aprobadas para procesar código propietario o datos de clientes. La herramienta autorizada es el asistente interno "NimbusAI" (con retención cero) y las instancias empresariales aprobadas.
- Criptominería y herramientas de pentesting fuera del equipo de SecOps.

El EDR detecta el software prohibido y genera un ticket automático `SEC-3`. La primera vez se trata como una capacitación; la reincidencia se informa a RR.HH. Si necesitás una excepción, justificala por ticket con aprobación de SecOps.

## 9. Actualizaciones de software

Mantener todo actualizado es una de las medidas de seguridad más efectivas. Política:

- **Sistemas operativos**: las actualizaciones de seguridad se instalan dentro de los 7 días de su publicación (críticas: 72 horas). Las versiones mayores (por ejemplo, un nuevo macOS) se habilitan tras 30 días de pruebas del equipo de Soporte.
- **Navegadores**: Chrome se actualiza automáticamente; reiniciarlo semanalmente.
- **Aplicaciones corporativas**: se actualizan desde Self Service o de forma silenciosa por el MDM.
- **Reinicios**: el equipo muestra una notificación; podés postergar hasta 3 veces (24 horas en total). Luego se fuerza el reinicio fuera de reuniones.

Cuando aparece el aviso "Actualización requerida" (`MDM-UPD-110`):

1. Guardá tu trabajo.
2. Abrí Nimbus Self Service > *Actualizaciones pendientes*.
3. Hacé clic en *Instalar ahora* y mantené el equipo conectado a la corriente.
4. La instalación tarda entre 20 y 45 minutos.
5. Si falla, anotá el código y abrí un ticket P3.

Las ventanas de despliegue masivo se publican en el calendario "IT - Mantenimiento" y suelen realizarse los miércoles de 12:00 a 14:00 hs. Si pasaron más de 14 días sin actualizar, el acceso por SSO se limita (`OKTA-403-DEV`) hasta regularizar el equipo.
