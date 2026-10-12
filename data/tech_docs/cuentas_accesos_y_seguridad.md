# Cuentas, Accesos y Seguridad en Nimbus Cloud

Esta guía es la referencia interna del equipo de Soporte IT de Nimbus Cloud para todo lo relacionado con identidades digitales, autenticación y seguridad de la información. Aplica a los aproximadamente 300 empleados de la empresa, tanto a quienes trabajan en la sede de Buenos Aires (Av. Corrientes, piso 14) como al equipo remoto distribuido en Argentina, Chile, Uruguay, Colombia y México. Si algo de lo que figura acá no coincide con lo que ves en pantalla, abrí un ticket en Nimbus Helpdesk y avisanos: esta base se revisa el primer lunes de cada mes.

## 1. Alta de cuentas (onboarding)

Toda persona que ingresa a Nimbus Cloud recibe su identidad digital antes del primer día de trabajo. El proceso lo dispara People & Culture (RR.HH.) cargando el alta en el sistema BambooHR interno, y Soporte IT lo ejecuta con un SLA de 3 días hábiles previos a la fecha de ingreso.

Pasos del alta:

1. People & Culture completa el formulario "Alta de colaborador" con nombre legal, país, rol, área, manager y fecha de ingreso. Si falta el manager, el alta queda en estado `PENDIENTE_DATOS` y no avanza.
2. El workflow `onboarding-sync` crea el usuario en Okta con el formato `nombre.apellido@nimbuscloud.example`. En caso de homónimos se agrega la inicial del segundo nombre (por ejemplo `ana.m.perez`).
3. Okta asigna automáticamente los grupos base según el rol: `grp-all-staff`, `grp-<area>` y, si corresponde, `grp-eng-<squad>`.
4. Soporte IT crea el buzón de Google Workspace, la cuenta de Slack y el usuario de Jira. Las cuentas de GitHub se aprueban aparte (ver sección de permisos).
5. La persona recibe en su correo personal un enlace de activación con vigencia de 72 horas. Si vence, se reenvía desde Okta Admin con la opción *Directory > People > Reset activation*.
6. Durante el primer ingreso se enrolan obligatoriamente el MFA y el gestor de contraseñas. Sin MFA enrolado, la cuenta queda limitada y solo accede al portal de autoservicio.

El equipo de Soporte coordina con el manager una sesión de bienvenida técnica de 30 minutos el primer día, donde se verifica que la laptop, el correo, Slack y la VPN funcionen.

## 2. Baja de cuentas (offboarding)

La baja es un proceso crítico de seguridad. Se dispara desde People & Culture y tiene dos modalidades:

- **Baja programada** (renuncia con preaviso o fin de contrato): la cuenta se desactiva a las 18:00 hs (hora de Buenos Aires) del último día laboral.
- **Baja inmediata** (desvinculación sin preaviso o incidente de seguridad): la cuenta se suspende en un máximo de 30 minutos desde que RR.HH. o Seguridad lo solicita por el canal #it-urgente o llamando a la guardia.

Checklist que ejecuta Soporte IT:

1. Suspender el usuario en Okta (`Deactivate`), lo que corta el acceso por SSO a todas las aplicaciones federadas.
2. Revocar sesiones activas en Google Workspace (Admin Console > Usuarios > Seguridad > *Cerrar sesión*), y revocar tokens OAuth.
3. Quitar la pertenencia a organizaciones de GitHub y a los equipos de Jira.
4. Transferir la propiedad de documentos de Drive al manager (retención de 30 días antes de borrado definitivo).
5. Configurar reenvío del correo al manager por 30 días y respuesta automática.
6. Deshabilitar el certificado de VPN y borrar la entrada del dispositivo en el MDM.
7. Coordinar la devolución del equipamiento (ver archivo de equipamiento y dispositivos).

El buzón se conserva en estado archivado durante 90 días y luego se elimina, salvo retención legal solicitada por el área Legal.

## 3. Inicio de sesión único (SSO) con Okta

Nimbus Cloud usa **Okta** (tenant ficticio `nimbuscloud.okta.example`) como proveedor de identidad central. Con una sola autenticación se accede a Google Workspace, Slack, Jira, Confluence, GitHub Enterprise, Zoom y al portal Nimbus Helpdesk.

Cómo ingresar:

1. Abrí `https://nimbuscloud.okta.example` o el panel de aplicaciones desde el navegador corporativo.
2. Ingresá tu usuario completo y tu contraseña.
3. Aprobá el segundo factor (ver sección de MFA).
4. Hacé clic en el ícono de la aplicación que necesitás.

La sesión de Okta dura 12 horas en dispositivos gestionados y 4 horas en dispositivos no gestionados. Pasado ese tiempo se vuelve a pedir autenticación. Las aplicaciones sensibles (consola de AWS, panel de facturación y GitHub con permisos de administración) piden reautenticación cada 60 minutos.

Códigos de error frecuentes de SSO:

- **OKTA-401**: credenciales incorrectas o cuenta bloqueada. Esperar 15 minutos o resetear la contraseña.
- **OKTA-403-DEV**: el dispositivo no cumple la política (sin cifrado de disco o sistema operativo desactualizado). Resolver con el checklist de la sección de equipamiento.
- **SAML-512**: desfase de hora mayor a 5 minutos entre el equipo y el servidor. Activar sincronización automática de hora.
- **SSO-AppNotAssigned**: no tenés asignada la aplicación; pedila por ticket con aprobación de tu manager.

## 4. Autenticación multifactor (MFA)

El MFA es obligatorio para todo el personal sin excepciones. Los factores aceptados, en orden de preferencia:

1. **Okta Verify con push y número** (recomendado): llega una notificación y hay que escribir el número de dos dígitos que aparece en pantalla.
2. **Llave de seguridad FIDO2** (YubiKey 5 NFC): obligatoria para administradores de sistemas y para el equipo de Finanzas con acceso bancario.
3. **Código TOTP** de Okta Verify, para cuando no hay conexión de datos.
4. **Códigos de recuperación**: diez códigos de un solo uso, generados al enrolar. Guardarlos en el gestor de contraseñas.

El SMS no está permitido como factor, salvo en el período de transición de 24 horas ante pérdida del teléfono, autorizado por Soporte tras validar identidad.

Pasos para enrolar Okta Verify:

1. Instalá Okta Verify desde App Store o Google Play.
2. En Okta, entrá a *Configuración > Métodos de autenticación > Okta Verify > Configurar*.
3. Escaneá el código QR con la app.
4. Verificá con una notificación de prueba.
5. Descargá los códigos de recuperación y guardalos.

Si cambiaste de celular, no borres el anterior hasta transferir el factor. Si ya lo perdiste, abrí un ticket P2 desde otro medio (por ejemplo el correo de un compañero con copia a tu manager) o llamá a la mesa de ayuda; vamos a validar tu identidad por videollamada con cámara encendida y documento, y reseteamos el factor en un plazo de 2 horas hábiles.

## 5. Reseteo de contraseña

Hay dos caminos:

**Autoservicio (preferido, disponible 24/7):**

1. En la pantalla de login de Okta, hacé clic en *¿Necesitás ayuda para iniciar sesión?*.
2. Elegí *Olvidé mi contraseña*.
3. Verificá con Okta Verify o con el correo personal registrado.
4. Definí una nueva contraseña que cumpla la política.
5. Esperá hasta 5 minutos para que se sincronice con Google Workspace.

**Asistido por Soporte:** si no tenés acceso a ningún factor, abrí un ticket. El técnico valida identidad con una videollamada y genera una contraseña temporal de un solo uso que vence a los 30 minutos. Nunca vamos a pedirte tu contraseña por chat, correo o teléfono.

Tras 5 intentos fallidos consecutivos la cuenta se bloquea 15 minutos automáticamente. Tras 10 intentos en 24 horas se bloquea hasta intervención de Soporte y se genera una alerta en el SIEM.

## 6. Política de contraseñas

La política vigente (documento SEC-POL-004, versión 3.2) establece:

- Longitud mínima de **14 caracteres**; recomendamos frases de paso de 4 palabras o más.
- Prohibido reutilizar las últimas **12** contraseñas.
- No contener el nombre, el apellido ni el nombre de la empresa.
- Se verifica contra una lista de contraseñas filtradas conocidas; si aparece, se rechaza con el error `PWD-BREACHED`.
- No hay vencimiento periódico forzado, salvo sospecha de compromiso, en línea con las recomendaciones actuales de NIST. Se exige cambio inmediato ante cualquier incidente.
- Las contraseñas de cuentas de servicio tienen 32 caracteres generados y rotan cada 90 días mediante el vault.

Está prohibido compartir contraseñas, anotarlas en papel o enviarlas por Slack o correo.

## 7. VPN corporativa

Usamos **GlobalProtect** (ficticio) con gateway `vpn.nimbuscloud.example`. Es obligatoria para acceder a recursos internos: ambientes de staging, bases de datos de testing, Confluence interno y el repositorio de artefactos.

Para conectarte:

1. Abrí el cliente GlobalProtect (ícono en la barra de menú o bandeja del sistema).
2. Verificá que el portal sea `vpn.nimbuscloud.example`.
3. Iniciá sesión con Okta; se aprueba el MFA.
4. Cuando el estado diga *Conectado*, ya podés usar los recursos internos.

La VPN usa túnel dividido (*split tunnel*): solo el tráfico hacia los rangos `10.20.0.0/16` y `10.30.0.0/16` pasa por el túnel. Cada sesión dura 10 horas y se cierra tras 30 minutos de inactividad. Para producción, el acceso adicional pasa por un bastión con grabación de sesión. Los problemas de conexión se tratan en el archivo de red y troubleshooting.

## 8. Gestor de contraseñas

El gestor corporativo es **1Password Business** (ficticio en esta base). Todo empleado recibe una bóveda personal y acceso a bóvedas compartidas por área. Se instala la extensión del navegador y la app de escritorio durante el onboarding.

Buenas prácticas:

1. Generá siempre contraseñas únicas de al menos 20 caracteres para sitios externos.
2. Compartí credenciales de equipo únicamente mediante bóvedas compartidas, nunca copiando el valor.
3. Guardá allí los códigos de recuperación del MFA.
4. La clave maestra y la Secret Key se guardan en el kit de emergencia impreso, en un lugar físico seguro.

Si olvidás la clave maestra, Soporte puede iniciar una recuperación con aprobación del manager; los datos de la bóveda personal se restauran con el kit de emergencia. Sin kit, los datos personales no pueden recuperarse.

## 9. Permisos por rol (RBAC)

El acceso se otorga por el principio de mínimo privilegio, mediante grupos de Okta. Resumen:

| Rol | Accesos estándar | Accesos que requieren aprobación |
|---|---|---|
| Ingeniería | GitHub (lectura/escritura en sus repos), Jira, Confluence, staging | Producción (aprobación del Engineering Manager y SecOps) |
| Producto y Diseño | Jira, Confluence, Figma, analítica | Datos de clientes anonimizados |
| Soporte al Cliente | CRM, Zendesk-like interno, Slack | Panel de administración de clientes (solo lectura) |
| Finanzas | ERP, planilla de conciliación | Banca online con FIDO2 |
| People & Culture | BambooHR, Drive de RR.HH. | Datos de nómina |
| Ventas | CRM, Zoom, Drive comercial | Descuentos especiales en el CRM |

Las solicitudes de acceso adicionales se piden por ticket en la categoría *Accesos > Nuevo permiso*, con aprobación del manager (SLA de aprobación: 1 día hábil) y del dueño del recurso. Cada trimestre se ejecuta una recertificación de accesos: los managers reciben una lista en Okta Access Governance y tienen 10 días hábiles para confirmar o revocar. Los accesos no confirmados se quitan automáticamente.

## 10. Phishing y reporte de incidentes

Phishing es el vector de ataque más frecuente. Señales de alerta: urgencia artificial, dominios parecidos (`nimbuscIoud.example` con "I" mayúscula en vez de "l"), pedidos de credenciales o de transferencias, adjuntos inesperados con macros y enlaces acortados.

Qué hacer ante un correo sospechoso:

1. No hagas clic ni abras adjuntos.
2. Usá el botón **Reportar phishing** en Gmail (menú de tres puntos > *Reportar phishing*) o el complemento de Nimbus "PhishAlert".
3. Si ya hiciste clic o ingresaste datos, avisá de inmediato: no hay sanción por reportar a tiempo, y cada minuto cuenta.
4. Cambiá la contraseña desde otro dispositivo de confianza y avisá a la guardia.

Clasificación de incidentes de seguridad:

- **SEC-1 (crítico)**: credenciales de administrador comprometidas, ransomware, fuga de datos de clientes. Se contacta a la guardia por teléfono al +54 11 5555-0199 y se abre un canal #inc-AAAAMMDD. Respuesta en 15 minutos.
- **SEC-2 (alto)**: cuenta de empleado comprometida, malware detectado por el EDR. Respuesta en 1 hora.
- **SEC-3 (medio)**: phishing recibido sin interacción, dispositivo extraviado sin datos sensibles. Respuesta en 4 horas.

El equipo de seguridad (SecOps) investiga con el EDR **CrowdStrike Falcon** (ficticio) y registra todo en el SIEM. Ante fuga de datos personales, Legal evalúa la notificación a las autoridades dentro de las 72 horas. Una vez por trimestre se realiza una campaña de phishing simulado; quienes caen reciben una microcapacitación de 15 minutos, sin sanción disciplinaria.

Para dudas generales escribí a it-help@nimbuscloud.example y para reportes de seguridad a seguridad@nimbuscloud.example.
