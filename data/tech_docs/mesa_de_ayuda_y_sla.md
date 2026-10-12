# Mesa de Ayuda y SLA de Nimbus Cloud

Este documento explica cómo contactar a Soporte IT, cómo se priorizan los pedidos, qué tiempos de respuesta y resolución se comprometen, cómo funcionan las guardias y qué ocurre ante mantenimientos, caídas y recuperación de datos. Aplica a todo el personal de Nimbus Cloud (aproximadamente 300 personas) en Buenos Aires y LATAM. El equipo de Soporte IT está compuesto por 9 técnicos, 2 líderes de turno y 1 gerente, y trabaja sobre la plataforma **Nimbus Helpdesk** (basada en Jira Service Management).

## 1. Cómo abrir un ticket

### 1.1 Por el portal Nimbus Helpdesk (canal recomendado)

Dirección: `https://helpdesk.nimbuscloud.example` (acceso por SSO de Okta, sin VPN).

1. Ingresá con tu usuario de Okta.
2. Hacé clic en *Crear solicitud*.
3. Elegí la categoría: *Accesos y cuentas*, *Equipamiento*, *Software y licencias*, *Red y conectividad*, *Seguridad* u *Otros*.
4. Completá el resumen (una línea clara), la descripción, el impacto (cuántas personas afecta) y adjuntá capturas o logs.
5. Enviá. Recibís un número con formato `HD-00000` (por ejemplo, `HD-48213`) y un correo de confirmación.
6. Podés seguir el estado en *Mis solicitudes* y agregar comentarios.

El portal calcula la prioridad inicial según las respuestas, y un técnico la confirma dentro de los plazos de respuesta.

### 1.2 Por correo electrónico

Escribí a **it-help@nimbuscloud.example**. El sistema crea un ticket automáticamente con el asunto como resumen. Para que el ticket se clasifique mejor, usá estas etiquetas al inicio del asunto: `[ACCESO]`, `[EQUIPO]`, `[SOFTWARE]`, `[RED]` o `[URGENTE]`. El correo con la etiqueta `[URGENTE]` genera una alerta al técnico de turno, pero solo debe usarse para P1 y P2. Los correos enviados a técnicos individuales no se tratan como tickets y no cuentan para el SLA.

### 1.3 Otros canales

- **Slack**: el comando `/helpdesk` abre un formulario que genera un ticket. El canal `#it-ayuda` es para consultas informales.
- **Teléfono (solo P1 y P2)**: guardia IT +54 11 5555-0199, operativa las 24 horas, todos los días. Para llamadas desde otros países, usar el mismo número con el prefijo internacional.
- **Presencial**: Mesa de Ayuda en el piso 14, sector Soporte, de lunes a viernes de 9:00 a 18:00. Se atiende sin turno, pero se registra un ticket igualmente.

Cuándo no usar la mesa de ayuda: pedidos de compras generales, problemas con la plataforma de producto que ven los clientes (eso va a Soporte al Cliente) y consultas de RR.HH.

## 2. Prioridades P1 a P4

La prioridad se determina por el **impacto** (a cuántas personas o servicios afecta) y la **urgencia** (si hay una alternativa o un plazo crítico).

| Prioridad | Definición | Ejemplos |
|---|---|---|
| **P1 - Crítica** | Caída total de un servicio esencial o riesgo de seguridad grave; afecta a toda la empresa o a una sede | Caída del SSO de Okta, Google Workspace o la VPN para todos; ransomware; red de oficina caída; cuenta de administrador comprometida |
| **P2 - Alta** | Un servicio importante degradado, o una persona/equipo totalmente bloqueado sin alternativa | Laptop que no enciende; MFA perdido con trabajo urgente; equipo de 10 personas sin acceso a GitHub |
| **P3 - Media** | Problema que afecta el trabajo pero hay alternativa; una persona con funcionalidad parcial | Impresora sin tóner, VPN inestable, lentitud, error en una aplicación |
| **P4 - Baja** | Consulta, pedido estándar o mejora sin impacto en el trabajo | Alta de licencia, periférico nuevo, consulta de procedimiento |

Si considerás que la prioridad asignada no refleja la realidad, comentalo en el ticket con el impacto concreto. No subas prioridades sin justificación: la mala clasificación afecta a quienes sí tienen una urgencia real. Los pedidos de la dirección (C-level) no se priorizan automáticamente; se evalúan por impacto como los demás.

## 3. SLA en horas

Los SLA se miden en **horas hábiles** de servicio, salvo P1 (y P2 con guardia) que se miden en horas corridas. El horario de servicio estándar es de lunes a viernes, de 9:00 a 18:00 (hora de Buenos Aires), excluyendo feriados argentinos. Las zonas horarias de LATAM se cubren con el turno extendido de 8:00 a 20:00.

| Prioridad | Primera respuesta | Resolución objetivo | Actualizaciones al solicitante | Cobertura |
|---|---|---|---|---|
| P1 | 15 minutos | 4 horas | Cada 30 minutos | 24x7 (guardia) |
| P2 | 1 hora | 8 horas | Cada 2 horas | 24x7 (guardia) para ticket abierto por teléfono |
| P3 | 4 horas | 24 horas (3 días hábiles máximo) | Diaria | Horario de servicio |
| P4 | 8 horas | 5 días hábiles | A pedido y al cierre | Horario de servicio |

Reglas importantes:

1. El reloj del SLA se **pausa** cuando el ticket pasa a *Esperando al solicitante* (por ejemplo, si el técnico te pidió información). Si no respondés en 3 días hábiles, el técnico envía un recordatorio; a los 5 días hábiles sin respuesta, el ticket se cierra automáticamente con la posibilidad de reabrirse dentro de 7 días.
2. El reloj también se pausa en *Esperando a un proveedor* (por ejemplo, un caso de garantía en Apple), aunque se informa un tiempo estimado.
3. Los SLA se miden mensualmente. La meta es cumplir el 95 % en P1 y P2 y el 90 % en P3 y P4. En septiembre de 2026 el cumplimiento fue de 97 % y 92 % respectivamente.
4. Los reportes de cumplimiento se publican el primer día hábil de cada mes en Confluence, espacio `IT-Metrics`.
5. Los solicitantes reciben una encuesta de satisfacción de 3 preguntas al cerrar el ticket; la meta de CSAT es 4,5 sobre 5.

## 4. Horarios de guardia

La guardia garantiza respuesta ante P1 y P2 fuera del horario de servicio. Se gestiona con PagerDuty y rota semanalmente.

- **Guardia primaria**: un técnico de Soporte IT, de lunes a lunes, desde las 18:00 de un lunes hasta las 9:00 del lunes siguiente en el horario nocturno, y las 24 horas los fines de semana y feriados. Responde la alerta en 10 minutos.
- **Guardia secundaria**: un líder de turno; entra si la primaria no confirma en 15 minutos.
- **Guardia de SecOps**: especialista de seguridad para incidentes SEC-1 y SEC-2, con tiempo de respuesta de 15 minutos.
- **Guardia de SRE/Plataforma**: para incidentes en producción de la plataforma de producto (fuera del alcance de IT corporativa).

La guardia se compensa con un adicional por disponibilidad y con horas libres por cada intervención nocturna. Los técnicos no deben realizar cambios riesgosos en guardia salvo con aprobación del líder de turno. El calendario vigente figura en PagerDuty y en el canal `#it-guardia`.

Cómo invocar la guardia: llamá al +54 11 5555-0199 y, si no atiende nadie, el sistema reintenta con la secundaria. También podés escribir `@it-oncall` en el canal `#it-urgente`. No uses la guardia para P3 y P4: serán atendidos en el horario de servicio.

## 5. Escalamiento

Hay dos tipos de escalamiento:

**Escalamiento funcional (entre niveles técnicos):**

1. **Nivel 1 (Mesa de Ayuda)**: registra, clasifica y resuelve el 65 % de los tickets con la base de conocimiento.
2. **Nivel 2 (Soporte especializado)**: sistemas, redes, MDM, Okta; resuelve problemas complejos y cambios de configuración.
3. **Nivel 3 (Ingeniería / Proveedores)**: SRE, SecOps y proveedores externos (Okta, Google, Apple) para fallas de plataforma o defectos.

El pase de nivel se hace dentro de los siguientes plazos: N1 a N2 si no hay solución en 2 horas hábiles (P2) o 1 día (P3); N2 a N3 si no hay solución en 4 horas (P1) o 1 día (P2).

**Escalamiento jerárquico (por incumplimiento de SLA):**

- Al 75 % del tiempo de SLA consumido, el sistema alerta al técnico asignado y al líder de turno.
- Al 100 %, se notifica al Gerente de Soporte IT.
- Al 150 % de un P1 o P2, se informa al CTO y se abre un canal `#inc-AAAAMMDD` con reporte de estado cada 30 minutos.

Si como solicitante creés que tu ticket no avanza, usá el botón *Escalar* del portal, que explica el motivo y notifica al líder de turno. Cada incidente P1 genera un informe post-mortem sin culpas dentro de los 5 días hábiles, que incluye línea de tiempo, causa raíz y acciones correctivas.

## 6. Mantenimiento programado

Los trabajos planificados se ejecutan en ventanas definidas para minimizar el impacto:

- **Ventana semanal de parches**: miércoles de 12:00 a 14:00 hs (hora de Buenos Aires) para actualizaciones de software y MDM. No requiere corte de servicio.
- **Ventana mensual de infraestructura**: el segundo sábado de cada mes, de 22:00 a 02:00 hs del domingo. Se aplican cambios en red, VPN, firewall y directorio. Puede producir cortes breves (hasta 15 minutos).
- **Ventana trimestral mayor**: el último sábado de marzo, junio, septiembre y diciembre, de 20:00 a 04:00 hs. Para migraciones y renovaciones de certificados y de hardware de red.

Procedimiento de comunicación:

1. Los cambios se registran como *Solicitud de cambio* (RFC) en Nimbus Helpdesk y los aprueba el Comité de Cambios (CAB) cada martes a las 11:00.
2. Se anuncia con **7 días de anticipación** en `#it-estado`, por correo a todo el personal y en el calendario "IT - Mantenimiento". Los cambios de emergencia se avisan en cuanto se aprueban.
3. Durante la ventana, el estado se publica en `status.nimbuscloud.example`.
4. Al terminar, se confirma el cierre y se abre una ventana de 24 horas de monitoreo reforzado.

Los cambios que afectan a personas en LATAM se planifican considerando los husos horarios. Las renovaciones de certificados se programan con 30 días de anticipación para evitar vencimientos inesperados (error `CERT-EXP-001`).

## 7. Backups y recuperación

Nimbus Cloud sigue la regla 3-2-1: tres copias, en dos medios distintos, una fuera del sitio principal. Esta sección detalla lo relativo a los datos corporativos (no al producto SaaS, que tiene su propio plan de continuidad).

| Sistema | Frecuencia de backup | Retención | RPO | RTO |
|---|---|---|---|---|
| Google Workspace (Gmail, Drive) | Diario, con Backupify ficticio | 365 días | 24 horas | 8 horas |
| Okta (configuración y grupos) | Exportación diaria | 90 días | 24 horas | 4 horas |
| Jira y Confluence | Diario, con copia semanal completa | 180 días | 24 horas | 8 horas |
| GitHub (repositorios) | Réplica cada 6 horas a almacenamiento propio | 365 días | 6 horas | 12 horas |
| Servidores de archivos de la oficina | Incremental cada hora, completo cada domingo | 60 días | 1 hora | 4 horas |
| Laptops | No se respaldan: el trabajo debe estar en Drive | N/A | N/A | N/A |

Los backups se cifran con AES-256 y se almacenan en una región distinta (São Paulo) a la de operación. Cada trimestre se realiza una **prueba de restauración**; el resultado se documenta en Confluence. La última (septiembre de 2026) restauró 2 TB de Drive en 3 horas y 40 minutos.

Cómo pedir una recuperación:

1. Primero revisá la **papelera de Drive** (30 días) o el historial de versiones del archivo (*Archivo > Historial de versiones*).
2. Si no está allí, abrí un ticket en *Otros > Recuperación de datos*, indicando ruta del archivo, fecha aproximada de pérdida y persona propietaria.
3. Soporte restaura desde el backup: archivos individuales en 4 horas hábiles; carpetas grandes en hasta 24 horas.
4. Se restaura en una carpeta aparte llamada `Restaurado_AAAAMMDD` para que revises antes de reemplazar.

En caso de desastre (pérdida de la oficina, caída prolongada de un proveedor), se activa el Plan de Continuidad del Negocio: el personal trabaja de forma remota, con comunicaciones por Slack y, como alternativa, el canal de Telegram de emergencia del comité de crisis. El Plan se ensaya dos veces por año. Los contactos clave: Gerente de Soporte IT, CTO y Responsable de Seguridad, con directorio impreso en la oficina y en la bóveda de emergencia de 1Password.

Para cualquier consulta sobre este documento, escribí a it-help@nimbuscloud.example.
