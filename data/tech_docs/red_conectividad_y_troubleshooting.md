# Red, Conectividad y Troubleshooting en Nimbus Cloud

Guía práctica del equipo de Soporte IT para resolver los problemas de conexión más comunes, tanto en la oficina de Buenos Aires como en el trabajo remoto desde LATAM. Está organizada por tipo de problema, con pasos numerados y los códigos de error ficticios que usa Nimbus Cloud en sus herramientas. Antes de abrir un ticket, recorré la sección que corresponda: aproximadamente el 70 % de los casos se resuelve con estos pasos.

## 1. Wi-Fi de la oficina de Buenos Aires

La oficina (piso 14 y piso 15 de Av. Corrientes) cuenta con 24 puntos de acceso Wi-Fi 6E, administrados desde un controlador central. Hay tres redes:

| SSID | Uso | Autenticación |
|---|---|---|
| `Nimbus-Corp` | Equipos corporativos | 802.1X con certificado del MDM, sin contraseña manual |
| `Nimbus-Guest` | Visitas | Portal cautivo con clave del día, válida 24 horas, aislada de la red interna |
| `Nimbus-IoT` | Impresoras, salas de reunión, TVs | Clave compartida, sin acceso a Internet salvo lo necesario |

Para conectarte a `Nimbus-Corp`, el equipo debe tener el perfil de Wi-Fi instalado por el MDM. En la gran mayoría de los casos se conecta solo. Los dispositivos personales (BYOD) deben usar `Nimbus-Guest`.

Capacidad y datos: banda de 5 GHz y 6 GHz preferente, ancho de banda total de 1 Gbps simétrico con dos proveedores de Internet (enlace principal y enlace de respaldo de 500 Mbps con conmutación automática en menos de 30 segundos).

Si el Wi-Fi no conecta o es lento:

1. Desactivá y volvé a activar el Wi-Fi del equipo.
2. Olvidá la red `Nimbus-Corp` y reconectate (en macOS: *Ajustes del Sistema > Wi-Fi > Detalles > Olvidar esta red*).
3. Verificá que la fecha y hora estén correctas; un desfase produce errores de certificado.
4. Reiniciá el equipo.
5. Si seguís sin conectar, pedí a Soporte que reinstale el perfil con `sudo jamf policy -event installWifiProfile` (lo hace el técnico, no el usuario) o desde Intune con *Sincronizar*.

Códigos de error frecuentes:

- **NET-WIFI-801**: certificado de dispositivo vencido. Se renueva en Self Service > *Renovar certificado*.
- **NET-WIFI-812**: no se obtuvo dirección IP del DHCP. Reconectar; si se repite, avisar a Soporte porque el pool de la VLAN puede estar agotado (el pool tiene 500 direcciones).
- **NET-WIFI-830**: la autenticación 802.1X fue rechazada; suele indicar cuenta bloqueada o dispositivo fuera de cumplimiento.

Para saber si el problema es de tu equipo o de la oficina, consultá el canal `#it-estado` y el tablero de estado `status.nimbuscloud.example`.

## 2. Internet desde casa (equipo remoto)

Para quienes trabajan desde sus casas, los requisitos mínimos son 30 Mbps de bajada, 10 Mbps de subida y latencia menor a 60 ms hacia Buenos Aires. Probá tu conexión en `speed.nimbuscloud.example` o con el comando `networkQuality` en macOS.

Recomendaciones: usar cable Ethernet con el adaptador USB-C si es posible; si usás Wi-Fi, ubicarte cerca del router y usar la banda de 5 GHz; reiniciar el router una vez por semana. La empresa reintegra hasta ARS 25.000 mensuales (o su equivalente regional) por el servicio de Internet del personal remoto, mediante rendición mensual a Finanzas.

## 3. La VPN no conecta

La VPN corporativa (GlobalProtect, portal `vpn.nimbuscloud.example`) es el origen de muchos tickets. Sigue este árbol de diagnóstico en orden:

1. **Verificá tu Internet**: abrí `https://www.google.com`. Si no abre, el problema es de tu conexión y no de la VPN.
2. **Cerrá y reabrí el cliente** de GlobalProtect. Verificá que el portal escrito sea exactamente `vpn.nimbuscloud.example`.
3. **Probá el MFA**: si la notificación de Okta Verify no llega, abrí la app manualmente y usá el código TOTP.
4. **Cambiá de red**: probá con la red del celular (hotspot). Algunos routers hogareños o redes de hoteles bloquean el puerto UDP 4501.
5. **Pedí que se use el modo SSL**: en el cliente, *Ajustes > Conexión > Forzar SSL (TCP 443)*.
6. **Reiniciá el servicio**: en macOS, `sudo launchctl kickstart -k system/com.paloaltonetworks.gp.pangpsd`; en Windows, reiniciá el servicio *PanGPS* desde `services.msc`.
7. Si todo falla, abrí un ticket P3 (P2 si tenés trabajo bloqueado) y adjuntá los logs: *GlobalProtect > Ajustes > Solución de problemas > Recopilar registros*.

Códigos de error:

- **VPN-1001**: no se puede alcanzar el portal. Falla de DNS o de Internet; probá con `nslookup vpn.nimbuscloud.example`.
- **VPN-2003**: autenticación fallida. Revisá contraseña y MFA; puede haber bloqueo de cuenta (15 minutos).
- **VPN-2017**: el dispositivo no cumple la política (sin cifrado o con SO desactualizado). Revisar Self Service.
- **VPN-3100**: se alcanzó el máximo de sesiones simultáneas (se permite 1 por usuario). Cerrá la sesión en otro dispositivo.
- **VPN-4020**: el túnel se cae cada pocos minutos. Suele ser inestabilidad de Wi-Fi o MTU; se ajusta MTU a 1380.

Si estás conectado a la VPN pero no accedés a un recurso interno, probá `ping 10.20.0.10` (DNS interno). Si responde pero el nombre no resuelve, desconectá y reconectá para refrescar la configuración DNS.

## 4. Impresoras

La oficina cuenta con 4 impresoras multifunción HP LaserJet Enterprise (modelo ficticio M635): dos en el piso 14 (sectores Norte y Sur) y dos en el piso 15. Funcionan con impresión segura: se envía el trabajo y se libera en el equipo acercando la credencial (badge) o ingresando el PIN de 6 dígitos.

Cómo agregar una impresora:

1. Abrí Self Service y elegí *Impresoras > Nimbus-Print-P14N* (u otra según el sector).
2. Esperá a que se instale el controlador (1 o 2 minutos).
3. Imprimí con la cola `Nimbus-Seguro` y liberá el trabajo en el equipo.

Los trabajos no liberados se eliminan a las 24 horas. El límite es de 500 páginas mensuales por persona; para un volumen mayor, pedí autorización.

Problemas típicos:

- **PRN-101 (trabajo atascado en cola)**: cancelar el trabajo (`cancel -a` en macOS desde Terminal, o limpiar la cola desde *Dispositivos e impresoras* en Windows) y reintentar.
- **PRN-204 (impresora fuera de línea)**: verificar que estés en `Nimbus-Corp` o con VPN; si hay un cartel en el panel de la impresora, avisar a Soporte.
- **PRN-310 (atasco de papel)**: seguir las indicaciones del panel, abrir la bandeja 2 y retirar el papel con cuidado.
- **PRN-412 (tóner bajo)**: avisa Soporte; el reemplazo se hace en el día. No pidas tóner por ticket, solo informá la impresora.
- **PRN-505 (PIN rechazado)**: reiniciá tu PIN en Self Service > *Impresión > Resetear PIN*.

El personal remoto no necesita imprimir en general; para trámites que lo requieran, se reintegra el costo de impresión en copisterías con comprobante.

## 5. Videollamadas (Zoom, Meet, Slack Huddles)

Las videollamadas son sensibles a la calidad de red. Una llamada fluida necesita unos 3 Mbps de subida y bajada, con latencia menor a 150 ms y pérdida de paquetes menor al 2 %.

Pasos si la videollamada va entrecortada:

1. Cerrá aplicaciones que consuman ancho de banda (sincronizaciones de Drive, descargas, otras pestañas con video).
2. Apagá tu video y dejá solo el audio; si mejora, el problema es el ancho de banda.
3. Cambiate a Ethernet o acercate al router.
4. Si estás en la VPN, desconectate durante la llamada: el tráfico de Zoom y Meet no necesita el túnel.
5. En Zoom, abrí *Ajustes > Estadísticas* y revisá la pérdida de paquetes y la latencia.

Si no se escucha o no se ve:

1. Verificá que la aplicación tenga permisos: en macOS, *Ajustes del Sistema > Privacidad y seguridad > Micrófono/Cámara*.
2. Seleccioná el dispositivo correcto en la configuración de audio (por ejemplo, Jabra Evolve2 65 y no el micrófono interno).
3. Cerrá cualquier otra aplicación que use la cámara.
4. Reiniciá la aplicación y, si hace falta, el equipo.

Códigos de error de Zoom:

- **1001 / 1002**: la cuenta no puede iniciar sesión; usar *Iniciar sesión con SSO* con el dominio `nimbuscloud`.
- **3000**: falla de conexión con el servicio de Zoom; verificar firewall o VPN.
- **5003**: no se pudo conectar con el servidor; probar otra red.
- **10002**: la reunión es solo para usuarios autenticados de Nimbus.

Salas de reunión de la oficina: las 8 salas (Palermo, Recoleta, Belgrano, Núñez, Retiro, Caballito, Barracas y Almagro) tienen pantalla, barra de video Logitech Rally Bar y control Zoom Rooms. Para proyectar de forma inalámbrica, usá el botón *Compartir pantalla* con el código que aparece en pantalla. Si la sala no inicia, reiniciá el control tocando el ícono de ajustes y *Reiniciar*, o avisá en `#it-urgente` con el nombre de la sala.

## 6. Guía de problemas frecuentes (resolución paso a paso)

### 6.1 El equipo va lento

1. Abrí el Monitor de Actividad (macOS) o el Administrador de tareas (Windows) y mirá qué proceso consume más CPU o memoria.
2. Cerrá pestañas de Chrome innecesarias; cada una puede usar 200 a 500 MB.
3. Verificá que haya al menos 15 % de disco libre.
4. Reiniciá: los equipos con más de 7 días encendidos tienen una notificación de reinicio.
5. Si el proceso `falcond` o `kernel_task` supera el 80 % de CPU de forma sostenida, abrí un ticket P3.

### 6.2 No llega o no se envía el correo

1. Verificá tu conexión y entrá a `mail.google.com` desde el navegador.
2. Si el error es **GWS-MAIL-550**, el destinatario o su servidor rechazaron el mensaje: revisá la dirección.
3. Si aparece **GWS-MAIL-552**, el adjunto supera 25 MB: usá un enlace de Drive.
4. Si el correo no llega, revisá la carpeta Spam y las reglas de filtrado.

### 6.3 No me deja entrar a una aplicación (SSO)

1. Cerrá sesión de Okta, borrá las cookies del sitio y volvé a ingresar.
2. Si aparece **OKTA-403-DEV**, ejecutá el chequeo de cumplimiento en Self Service > *Verificar mi equipo*.
3. Si aparece **SAML-512**, activá la hora automática del sistema.
4. Si aparece **SSO-AppNotAssigned**, pedí la asignación por ticket.

### 6.4 Docker, Git o CI no funcionan en la red de oficina o con VPN

1. Si `git clone` falla con `Could not resolve host`, verificá la VPN y el DNS interno.
2. Si `docker pull` falla con `x509: certificate signed by unknown authority`, instalá la CA corporativa desde Self Service > *Certificados de Nimbus*.
3. Si el pipeline falla con `CI-RUNNER-503`, el runner está saturado: reintentá en 10 minutos; si persiste, avisá en `#eq-plataforma`.

### 6.5 Problemas de audio y periféricos

1. Desconectá y reconectá el dock; esperá 10 segundos.
2. Si el monitor externo no tiene señal, probá otro cable USB-C y reiniciá el dock desconectándolo de la corriente por 30 segundos.
3. Si el mouse o el teclado inalámbrico no responden, cambiá las pilas o cargalos y re-emparejalos con el receptor Logi Bolt.

### 6.6 DNS y resolución de nombres

1. Ejecutá `nslookup nimbuscloud.example` y verificá que responda.
2. Limpiá la caché: en macOS, `sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder`; en Windows, `ipconfig /flushdns`.
3. Si el error es **NET-DNS-053**, el servidor DNS interno no responde: avisá a Soporte con el canal `#it-urgente`.

## 7. Cuándo abrir un ticket y qué adjuntar

Abrí un ticket si, tras aplicar la guía, el problema persiste. Para acelerar la resolución, incluí:

- El código de error exacto y una captura de pantalla.
- Desde cuándo ocurre y si pasó antes.
- Tu ubicación (oficina o remoto, ciudad y país) y tipo de conexión.
- Los pasos que ya probaste.
- Si usás VPN, el número de versión del cliente (*GlobalProtect > Ajustes > Acerca de*).

Un ticket completo se resuelve en promedio un 40 % más rápido. Los tiempos de respuesta según prioridad se encuentran en el archivo de mesa de ayuda y SLA.
