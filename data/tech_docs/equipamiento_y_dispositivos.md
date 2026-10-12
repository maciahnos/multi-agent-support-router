# Equipamiento y Dispositivos en Nimbus Cloud

Este documento describe qué equipamiento recibe cada persona en Nimbus Cloud, cómo se solicita, cómo se repone y qué responsabilidades implica. Cubre a la oficina de Buenos Aires y a las personas remotas de LATAM (Argentina, Chile, Uruguay, Colombia y México). El inventario completo se gestiona con la herramienta interna **AssetTrack** y el parque de dispositivos se administra con el MDM **Jamf Pro** para macOS y **Microsoft Intune** para Windows (ambos ficticios en esta base).

## 1. Laptops estándar

Nimbus Cloud define tres perfiles de laptop. Cada rol tiene un perfil por defecto, aunque un manager puede justificar un cambio por ticket.

| Perfil | Modelo de referencia | Especificaciones | Roles típicos |
|---|---|---|---|
| Estándar | Laptop 14" "NimbusBook Air" (MacBook Air M3) | 16 GB RAM, 512 GB SSD | Ventas, Soporte, People, Finanzas, Marketing |
| Desarrollo | Laptop 14" "NimbusBook Pro" (MacBook Pro M3 Pro) | 32 GB RAM, 1 TB SSD | Ingeniería, Datos, DevOps |
| Windows | ThinkPad T14 Gen 5 | 16 GB RAM, 512 GB SSD, Windows 11 Pro | Finanzas con ERP legado, Legales, quienes lo pidan con justificación |

El ciclo de vida es de **36 meses** para el perfil Estándar y Windows, y **30 meses** para el perfil Desarrollo. Al vencer, el equipo entra en la cola de renovación. Soporte avisa 60 días antes por correo y se coordina el recambio sin que la persona pierda días de trabajo.

Cada laptop se entrega con: cargador original (USB-C de 70 W), funda protectora, etiqueta de inventario con código `NC-LAP-XXXXX` y el sistema ya enrolado en el MDM.

## 2. Solicitud de equipo

Hay tres situaciones: ingreso, recambio por ciclo de vida y necesidad especial.

Pasos para pedir equipamiento nuevo:

1. Entrá a Nimbus Helpdesk (`helpdesk.nimbuscloud.example`) y elegí la categoría *Equipamiento > Solicitud nueva*.
2. Indicá qué necesitás, el motivo y la fecha en la que lo necesitás.
3. Tu manager recibe una aprobación automática por correo; tiene 2 días hábiles para aprobar.
4. Una vez aprobado, Soporte verifica stock en AssetTrack.
5. Si hay stock en Buenos Aires, la entrega se hace en 1 a 2 días hábiles. Si no hay stock, se compra al proveedor.

Plazos de entrega orientativos:

- **Buenos Aires**: retiro en el Depósito IT (piso 14, sector Soporte) o entrega en el puesto: 2 días hábiles con stock, 10 días hábiles sin stock.
- **Resto de Argentina**: envío por courier con seguimiento, 4 a 6 días hábiles.
- **Chile, Uruguay**: 7 a 10 días hábiles, incluyendo trámite aduanero a cargo de Compras.
- **Colombia y México**: 10 a 15 días hábiles. Se prefiere comprar localmente a través del proveedor regional para evitar aduanas.

Para ingresos, la solicitud debe cargarse al menos **10 días hábiles** antes de la fecha de ingreso. Si llega con menos anticipación, se entrega un equipo de contingencia del pool (10 unidades reservadas) y se hace el recambio cuando llega el definitivo.

## 3. Reposición por falla

Si tu equipo falla, el procedimiento es el siguiente:

1. Abrí un ticket en *Equipamiento > Falla de hardware*. Si no podés trabajar, marcalo como P2 (ver archivo de mesa de ayuda).
2. Un técnico hace diagnóstico remoto en un plazo máximo de 2 horas hábiles para P2 y 8 horas para P3.
3. Si el problema es de software, se resuelve remotamente o con una reinstalación de imagen (ver sección de imágenes).
4. Si es de hardware y está en garantía, se abre el caso con el fabricante y se entrega un equipo de reemplazo temporal del pool.
5. Si está fuera de garantía y la reparación supera el 40 % del valor de reposición, se reemplaza el equipo.

Fallas frecuentes y su tratamiento:

- Batería hinchada o con ciclos superiores a 1000: reemplazo de batería, 3 días hábiles. Si la batería está hinchada, dejá de usar el equipo y no lo cargues.
- Pantalla rota por golpe: se evalúa si fue uso razonable. Primera vez sin cargo; reincidencias se analizan con el manager.
- Teclado con teclas fallando: reparación en 3 a 5 días hábiles; se entrega un equipo temporal.
- Equipo que no enciende: P2, con reemplazo temporal el mismo día para Buenos Aires.

## 4. Robo o pérdida

El robo o la pérdida de un dispositivo es un incidente de seguridad clasificado como SEC-2 (o SEC-1 si contenía datos de clientes sin cifrar). Actuá así:

1. **Avisá de inmediato** llamando a la guardia de IT (+54 11 5555-0199) o enviando un correo a seguridad@nimbuscloud.example. Si es fuera del horario hábil, la guardia atiende las 24 horas.
2. Soporte ejecuta el **borrado remoto** desde el MDM (`Wipe Device`) y bloquea el equipo con el mensaje de recuperación. Se revoca la sesión de Okta y los tokens de Google.
3. Hacé la denuncia policial dentro de las 48 horas (en Argentina, en cualquier comisaría o en línea con la plataforma de denuncias del Ministerio de Seguridad). El número de la denuncia se adjunta al ticket.
4. Con la denuncia, Soporte tramita el reemplazo. El reemplazo se entrega en 1 a 3 días hábiles en Buenos Aires.
5. Como el disco está cifrado con FileVault o BitLocker, el riesgo de exposición de datos es bajo, pero se evalúa igualmente.

Si el robo ocurrió por negligencia comprobada (equipo olvidado a la vista en un vehículo, por ejemplo), RR.HH. y el manager evalúan la situación. No se descuenta nada por el primer incidente documentado.

## 5. BYOD (traiga su propio dispositivo)

Nimbus Cloud permite BYOD de forma limitada. Las reglas:

- **Celulares**: permitido para correo, Slack, Okta Verify y calendario, con perfil de trabajo administrado. Se instala la app Intune Company Portal, que crea un contenedor corporativo separado del contenido personal. La empresa nunca ve fotos, mensajes personales ni la ubicación.
- **Tablets**: mismas reglas que celulares.
- **Laptops personales**: **no permitidas** para trabajar con código fuente, datos de clientes o información financiera. Solo se admite acceso web a Google Workspace y Slack, mediante el navegador, sin descargas (la política de acceso condicional bloquea la descarga en dispositivos no gestionados).

Requisitos mínimos para un celular BYOD: iOS 17 o superior, o Android 13 o superior; bloqueo de pantalla con PIN de al menos 6 dígitos o biometría; cifrado activo; sin jailbreak ni root (el control de integridad lo detecta y bloquea el acceso con el error `MDM-CMP-207`).

Pasos para enrolar un celular:

1. Descargá Intune Company Portal.
2. Iniciá sesión con tu usuario de Nimbus.
3. Aceptá el perfil de trabajo.
4. Esperá la verificación de cumplimiento (unos 5 minutos).
5. Instalá las apps aprobadas desde la tienda corporativa.

Se otorga un subsidio mensual de ARS 15.000 (o su equivalente regional) para la conectividad móvil del personal que usa BYOD, previa solicitud en People & Culture.

## 6. Periféricos

Cada persona tiene derecho a un kit básico, y puede pedir periféricos adicionales por ticket.

Kit estándar para la oficina:

- Monitor de 27" (Dell P2723QE o equivalente), 1 por persona.
- Teclado y mouse inalámbricos Logitech MX Keys Mini y MX Anywhere.
- Docking station USB-C con soporte para dos monitores.
- Auriculares con micrófono (Jabra Evolve2 65).

Kit remoto (una sola vez, dentro de los primeros 30 días): un monitor de 27", teclado, mouse, auriculares y un subsidio de ARS 180.000 (o su equivalente regional en USD ~150) para silla o escritorio, con rendición de factura.

Periféricos adicionales (webcam, segundo monitor, soporte de laptop, hub USB) se piden en *Equipamiento > Periféricos*. Se aprueban sin mayor trámite si el costo es inferior a USD 100; entre USD 100 y 400 requieren aprobación del manager; por encima de USD 400 requiere la del Director del área. Los periféricos se reponen por desgaste cada 24 meses.

## 7. Imágenes de sistema operativo

Todas las laptops se despliegan con una imagen estándar mantenida por el equipo de Soporte, para garantizar consistencia y seguridad.

- **macOS**: imagen `NC-MAC-2025.3` basada en macOS Sequoia 15.x, desplegada con Jamf Pro y Apple Business Manager (enrolamiento automático al encender el equipo, DEP).
- **Windows**: imagen `NC-WIN-2025.2` basada en Windows 11 Pro 24H2, desplegada con Windows Autopilot.

La imagen incluye: agente del MDM, EDR (CrowdStrike Falcon), GlobalProtect, Okta Verify, 1Password, Google Chrome gestionado, Slack, Zoom, Google Drive para escritorio y herramientas de cifrado habilitadas. Las herramientas de desarrollo (Homebrew, Docker Desktop, IDEs) se instalan desde el portal de autoservicio **Nimbus Self Service**.

Reinstalación de imagen (reimaging): se hace ante corrupción del sistema, malware o cambio de dueño del equipo. Tarda unas 90 minutos y la persona debe tener sus archivos en Drive porque el contenido local se pierde. Antes de iniciar, verificá que tu trabajo esté sincronizado: *Google Drive > icono de la barra > Sincronizado*.

Los usuarios no tienen permisos de administrador local por defecto. Si necesitás instalar algo que no figura en Self Service, pedí elevación temporal (60 minutos) mediante la herramienta **Privileges** del dock, que registra el motivo.

## 8. Cifrado de disco

El cifrado de disco completo es obligatorio en todos los equipos corporativos y se verifica a diario.

- **macOS**: FileVault 2. La clave de recuperación se deposita en Jamf (escrow). Verificación: *Ajustes del Sistema > Privacidad y seguridad > FileVault*.
- **Windows**: BitLocker con TPM 2.0 y PIN de prearranque en los perfiles de riesgo alto. La clave se guarda en Entra ID. Verificación: *Panel de control > Cifrado de unidad BitLocker*.

Un equipo sin cifrado queda marcado como no conforme y, tras 48 horas, pierde el acceso a SSO con el error `OKTA-403-DEV`. Si el equipo te pide la clave de recuperación de BitLocker (código `BL-0x1FF`, 48 dígitos), llamá a Soporte; la validamos tras confirmar tu identidad y te la damos de forma segura. No guardes nunca esta clave en el mismo equipo.

Los pendrives USB están bloqueados por política para escritura. Si necesitás transferir datos, usá Drive. En casos justificados se entrega un pendrive cifrado IronKey previa aprobación de SecOps.

## 9. Devolución al offboarding

Cuando alguien se desvincula, debe devolver todo el equipamiento dentro de los **5 días hábiles** posteriores a su último día (o el mismo día, si la baja es inmediata).

Pasos de la devolución:

1. People & Culture notifica a Soporte la fecha de baja y se abre automáticamente la tarea *Devolución de equipo* en AssetTrack.
2. **En oficina**: entregá el equipo en el Depósito IT y firmá el acta de devolución. Se verifica que estén cargador, funda y periféricos.
3. **Remoto**: Soporte envía un kit de devolución prepago (caja con protección y etiqueta de courier, a cargo de la empresa). Embalá el equipo y entregalo al courier dentro de los 5 días hábiles.
4. Al recibirlo, Soporte inspecciona, borra de forma segura (`Erase All Content and Settings` en Mac o *Reset this PC* con borrado completo en Windows), actualiza AssetTrack y lo reasigna o lo da de baja.
5. El estado del equipo se informa a RR.HH. para el cierre del legajo.

Si el equipo no se devuelve, RR.HH. y Legales intiman a la devolución por escrito luego de 15 días; el equipo se bloquea remotamente desde el primer día. Los dispositivos con más de 4 años se donan a ONGs de reciclado tecnológico, previa certificación de borrado.

## 10. Garantías

Todos los equipos se compran con garantía del fabricante y cobertura extendida:

- Laptops Apple: AppleCare+ for Enterprise por 36 meses (cubre dos incidentes de daño accidental por año).
- Laptops Lenovo: garantía Premier Support por 36 meses, con servicio on-site en Buenos Aires.
- Monitores y docks: 36 meses del proveedor, con reemplazo directo.
- Periféricos Logitech y Jabra: 24 meses.

Para reclamar una garantía:

1. Abrí el ticket de falla de hardware; Soporte revisa el número de serie en AssetTrack y verifica la vigencia.
2. Soporte abre el caso con el fabricante (Apple Business Support o Lenovo Premier) y adjunta el diagnóstico.
3. El fabricante resuelve en 3 a 10 días hábiles según el país. Mientras tanto se entrega equipo del pool.
4. Cuando vuelve el equipo reparado, Soporte lo prueba y lo reasigna.

La garantía no cubre daños por líquidos con evidencia de mal uso, modificaciones no autorizadas ni desgaste normal de baterías con más de 1000 ciclos. Para consultas sobre un caso en curso, citá siempre el número de ticket (por ejemplo `HD-48213`) en it-help@nimbuscloud.example.
