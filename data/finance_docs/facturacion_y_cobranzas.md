# Facturación y Cobranzas de Nimbus Cloud

Versión 3.5 – Responsable: Gerencia de Finanzas, equipo de Revenue Operations – Consultas: finanzas@nimbuscloud.example

## 1. Introducción

Nimbus Cloud vende suscripciones B2B a su plataforma de gestión de infraestructura en la nube. Este documento describe cómo se factura, cómo se cobra y cómo se resuelven los desvíos con clientes. Aplica a los equipos de Ventas, Customer Success, Soporte y Finanzas. La facturación se gestiona con el sistema "Nimbus Billing", integrado con el CRM y con el sistema contable.

## 2. Planes y precios de suscripción

Los precios están expresados en USD por mes, por organización, y se facturan en la moneda que figure en el contrato (USD, ARS, CLP, COP, MXN o BRL).

| Plan | Precio mensual | Precio anual (pago único) | Usuarios incluidos | Almacenamiento | Soporte |
|---|---|---|---|---|---|
| Starter | USD 49 | USD 490 (2 meses gratis) | 5 | 100 GB | Correo, 48 h |
| Growth | USD 199 | USD 1.990 | 25 | 1 TB | Correo y chat, 12 h |
| Business | USD 649 | USD 6.490 | 100 | 5 TB | Prioritario, 4 h |
| Enterprise | Desde USD 2.400 | Contrato a medida | Ilimitados | A convenir | Gerente de cuenta, 1 h |

Cargos adicionales:

- Usuario adicional: USD 6 por mes en Starter, USD 5 en Growth y USD 4 en Business.
- Almacenamiento adicional: USD 12 por cada 100 GB mensuales.
- Módulo "Nimbus Security Plus": USD 150 por mes.
- Implementación y onboarding: USD 1.200 pago único para Business; incluido en Enterprise.

Los descuentos máximos que puede ofrecer Ventas sin aprobación son 10% por pago anual y 5% por volumen. Los descuentos de hasta 20% requieren aprobación del Director Comercial, y los mayores, del CFO.

## 3. Ciclo de facturación

### 3.1. Facturación mensual

1. El día 1 de cada mes, Nimbus Billing genera las facturas por el período corriente anticipado más el consumo variable del mes anterior (usuarios y almacenamiento adicionales).
2. Las facturas se envían por correo electrónico a la persona de contacto de facturación antes de las 10:00 (hora de Buenos Aires).
3. El vencimiento es a los 15 días corridos de la emisión para planes Starter, Growth y Business, y a los 30 días para Enterprise (salvo pacto distinto).

### 3.2. Facturación anual

La factura anual se emite 30 días antes del inicio de cada período de renovación. Vence a los 15 días de emitida. Si el cliente no paga, el servicio sigue activo hasta la fecha de renovación, con un período de gracia de 10 días.

### 3.3. Prorrateo

Cuando un cliente hace upgrade a mitad de mes, se factura la diferencia proporcional por los días restantes. Por ejemplo, un cliente que pasa de Growth a Business el día 11 de un mes de 30 días paga USD (649 - 199) x 20/30 = USD 300 adicionales. Los downgrades se aplican en el próximo ciclo, sin crédito retroactivo.

## 4. Facturas electrónicas

Nimbus Cloud emite facturas electrónicas conforme a la normativa de cada país:

- **Argentina:** factura electrónica A (clientes responsables inscriptos) o B/C, emitida con CAE vía ARCA. Se envía en PDF y XML. El punto de venta es el 0004 (servicios online).
- **Chile:** factura electrónica del SII.
- **Colombia:** factura electrónica DIAN con CUFE.
- **México:** CFDI 4.0 con timbrado.
- **Brasil:** NFS-e municipal.
- **Resto del mundo:** invoice en PDF con numeración correlativa.

Datos requeridos del cliente: razón social, CUIT/RUT/NIT o equivalente, condición frente al IVA, domicilio fiscal y correo de facturación. Sin estos datos, Nimbus Billing no libera la factura. Las correcciones de datos fiscales se hacen exclusivamente mediante nota de crédito y nueva factura, nunca editando el comprobante.

## 5. Notas de crédito y débito

Una nota de crédito se emite para:

- Anular una factura emitida por error o con datos incorrectos.
- Reconocer un reembolso total o parcial.
- Aplicar un descuento posterior acordado.
- Compensar caídas de servicio según el SLA.

Proceso:

1. La persona de Customer Success abre el ticket "Solicitud de nota de crédito" en el portal interno Nimbus Desk, con motivo, factura relacionada e importe.
2. Hasta USD 500, aprueba el líder de Finanzas Operativas; de USD 501 a USD 5.000, el Controller; por encima, el CFO.
3. Finanzas emite la nota dentro de 3 días hábiles y la notifica al cliente.

Las notas de débito se emiten cuando corresponde cobrar intereses de mora o ajustes de consumo omitidos.

### Compensaciones por SLA

La disponibilidad comprometida es 99,9% mensual. Si cae por debajo, el crédito automático es:

| Disponibilidad mensual | Crédito sobre la factura del mes |
|---|---|
| Entre 99,0% y 99,9% | 10% |
| Entre 95,0% y 99,0% | 25% |
| Menos de 95,0% | 50% |

El cliente debe reclamarlo dentro de los 30 días posteriores al cierre del mes afectado.

## 6. Medios de pago

| Medio | Disponible para | Comisión | Acreditación |
|---|---|---|---|
| Tarjeta de crédito (Visa, Mastercard, Amex) | Todos los planes | 3,4% a cargo de Nimbus | Inmediata / 48 h |
| Débito automático (CBU/ACH) | Argentina, Chile, México | Sin cargo | 24 a 72 h |
| Transferencia bancaria | Todos | Gastos a cargo del cliente | 1 a 3 días hábiles |
| Link de pago (Mercado Pago) | Argentina | 2,9% | Inmediata |
| SWIFT/Wire | Enterprise internacional | Gastos compartidos (SHA) | 3 a 5 días hábiles |

No se aceptan pagos en efectivo ni cheques. Los pagos deben informarse a cobranzas@nimbuscloud.example con el comprobante cuando se trate de transferencias, indicando los números de factura que cancelan. La conciliación bancaria se realiza todos los días hábiles a las 11:00.

## 7. Mora y recargos

Se considera vencida una factura no pagada al día siguiente de su fecha de vencimiento. El recargo por mora es del 2,5% mensual proporcional a los días de atraso, sobre el saldo vencido. En Argentina el interés se calcula sobre base diaria con tasa nominal anual del 30%.

### Secuencia de gestión de mora

1. **Día 1:** recordatorio automático por correo, tono amable.
2. **Día 7:** segundo aviso, con copia a la persona de Customer Success.
3. **Día 15:** llamada del equipo de Cobranzas y envío de la nota de débito por intereses.
4. **Día 21:** aviso formal de suspensión; se informa que el servicio pasará a modo solo lectura en 7 días.
5. **Día 30:** suspensión a solo lectura. Los datos se conservan.
6. **Día 60:** suspensión total del acceso y derivación a Legal.
7. **Día 90:** el saldo se considera de dudoso cobro, se previsiona al 50% y se evalúa la gestión con una agencia externa.
8. **Día 180:** previsión al 100% y propuesta de castigo al Controller.

Un cliente con deuda vencida mayor a 30 días no puede contratar módulos nuevos ni renovar con descuento. Las excepciones las aprueba el Director Comercial junto con Finanzas.

## 8. Cobranzas

El equipo de Cobranzas (4 personas) monitorea el reporte de antigüedad de saldos (aging) todas las mañanas. El objetivo trimestral es mantener el DSO por debajo de 38 días y los saldos vencidos a más de 60 días por debajo del 3% de la facturación mensual.

Indicadores de referencia:

- **DSO** (días de ventas pendientes de cobro): 34 días en el último cierre.
- **Tasa de cobranza al vencimiento:** 91%.
- **Morosidad mayor a 60 días:** 2,1%.

Para clientes Enterprise, el gerente de cuenta es responsable de gestionar la cobranza en conjunto con Finanzas a partir del día 10 de atraso. Los planes de pago se ofrecen en un máximo de 3 cuotas mensuales sin intereses adicionales, aprobadas por el Controller y formalizadas por escrito.

## 9. Disputas de facturación

Cuando un cliente cuestiona una factura:

1. El cliente envía el reclamo a facturacion@nimbuscloud.example o abre un ticket en el portal, dentro de los 30 días posteriores a la emisión.
2. Finanzas registra la disputa en Nimbus Billing con el estado "En disputa", lo que pausa los recordatorios automáticos y los intereses sobre el monto disputado.
3. Se confirma la recepción en 1 día hábil.
4. Revenue Operations revisa los consumos y contratos y emite un dictamen en un máximo de 7 días hábiles.
5. Si el reclamo es procedente, se emite una nota de crédito; si no, se envía el detalle de respaldo al cliente.
6. La parte no disputada de la factura debe pagarse en término.

Las disputas mayores a USD 10.000 se escalan al Controller y a Legal. Se registran todas las causas raíz en un tablero trimestral para mejorar los procesos (los motivos más frecuentes son usuarios duplicados, datos fiscales incorrectos y cargos por consumos adicionales no comunicados).

## 10. Reembolsos a clientes

Política general:

- **Garantía de satisfacción:** 30 días desde la primera contratación de un plan mensual o anual; se reembolsa el 100% al pago original.
- **Cancelación anual anticipada:** se reembolsa el período no utilizado menos una penalidad del 15%, solo si el cliente avisa con 30 días de anticipación.
- **Cobro duplicado o erróneo:** reembolso del 100% sin penalidad.
- **Servicios de implementación:** no reembolsables una vez iniciados.

Los reembolsos se pagan por el mismo medio utilizado. Los plazos son: tarjeta, 10 días hábiles; transferencia, 5 días hábiles. Los reembolsos mayores a USD 2.000 requieren dos firmas (Controller y CFO). Nunca se reembolsa a una cuenta distinta de la del pago original; si el banco del cliente cambió, se exige una carta firmada por un apoderado.

## 11. Impuestos

### 11.1. IVA

En Argentina, los servicios de software están alcanzados por el IVA a la alícuota general del 21%. Los precios de lista se muestran sin IVA para clientes B2B. Ejemplo: una suscripción Growth de USD 199 convertida a ARS se factura con IVA discriminado: neto + 21%. La liquidación se presenta mensualmente a través del Libro de IVA Digital antes del día 18 del mes siguiente.

Las exportaciones de servicios a clientes del exterior no pagan IVA, pero deben registrarse como factura E y respetarse las condiciones de liquidación de divisas.

### 11.2. Retenciones

Algunos clientes argentinos actúan como agentes de retención. Las retenciones que pueden aplicar son:

- Ganancias: según el régimen vigente (por ejemplo 2% sobre servicios, tasa ficticia).
- IVA: hasta el 10,5% del importe facturado.
- Ingresos Brutos (CABA y provincias): entre 0,5% y 3%.
- SUSS: en casos específicos.

El cliente debe enviar el certificado de retención dentro de los 10 días hábiles. Hasta recibirlo, Cobranzas deja la diferencia como saldo pendiente. Los certificados se archivan en la carpeta fiscal de cada cliente y sirven como pago a cuenta de impuestos.

En el exterior, las retenciones por impuestos locales (por ejemplo, ISR en México) se gestionan con el apoyo de los asesores fiscales externos de cada país.

## 12. Contactos

- Facturación: facturacion@nimbuscloud.example
- Cobranzas: cobranzas@nimbuscloud.example
- Consultas generales: finanzas@nimbuscloud.example
- Escalamiento: Controller (controller@nimbuscloud.example)
