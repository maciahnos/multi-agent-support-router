# Compras y Proveedores en Nimbus Cloud

Versión 2.8 – Responsable: Compras y Abastecimiento (dependiente de Finanzas) – Consultas: finanzas@nimbuscloud.example

## 1. Objetivo y alcance

Esta política ordena cómo Nimbus Cloud adquiere bienes y servicios, cómo se incorporan proveedores y cómo se les paga. Rige para todas las áreas y países. Su propósito es obtener buen precio y calidad, evitar conflictos de interés y dejar trazabilidad completa. Las compras se gestionan en la herramienta "Nimbus Procure", conectada con el ERP contable.

Quedan fuera de esta política los gastos de viaje y representación (ver política de gastos y reembolsos) y los pagos de sueldos y contractors (ver nómina y pagos).

## 2. Proceso de compras paso a paso

1. **Necesidad:** la persona solicitante, junto con su líder, define qué se necesita, para qué y cuánto cuesta aproximadamente.
2. **Solicitud de compra (SC):** se crea en Nimbus Procure, con descripción, centro de costo, monto estimado, fecha deseada y justificación.
3. **Aprobación presupuestaria:** el Business Partner de Finanzas del área verifica que haya presupuesto disponible.
4. **Cotizaciones:** Compras (o el solicitante, en compras menores) reúne las ofertas requeridas por monto.
5. **Selección:** se elige al proveedor con el mejor balance entre precio, calidad, plazo y riesgo; la selección se documenta en la planilla comparativa.
6. **Aprobación según umbral:** ver sección 3.
7. **Orden de compra (OC):** Compras emite la OC, que se envía al proveedor.
8. **Recepción:** quien solicitó confirma la recepción del bien o servicio en Nimbus Procure (el "goods receipt").
9. **Factura y control de tres vías:** Cuentas a Pagar compara OC, recepción y factura.
10. **Pago:** según los plazos definidos en la sección 8.

Una regla clave: **no se paga ninguna factura que no tenga OC previa**, con la excepción de servicios públicos, impuestos y alquileres con contrato vigente. Las compras hechas "después del hecho" requieren una justificación especial y se informan trimestralmente al Comité de Auditoría.

## 3. Umbrales de aprobación por monto

Los montos son totales de la compra, sin IVA, en USD o equivalente. Para contratos recurrentes se considera el valor anual.

| Monto (USD) | Aprobador/es | Cotizaciones requeridas | Documento |
|---|---|---|---|
| Hasta 500 | Líder directo | No requiere | Tarjeta corporativa o SC simple |
| 501 a 2.500 | Líder directo y Business Partner de Finanzas | 1 (con justificación del precio) | SC + OC |
| 2.501 a 10.000 | Director/a del área | 2 | SC + OC |
| 10.001 a 50.000 | Director/a del área y Controller | 3 | SC + OC + comparativo |
| 50.001 a 150.000 | VP del área y CFO | 3 | SC + OC + contrato |
| Más de 150.000 | CFO y CEO | 3 y proceso de licitación | Contrato revisado por Legal |

No se permite fraccionar compras para eludir los umbrales. Compras monitorea mensualmente compras múltiples al mismo proveedor dentro de un período de 30 días que, en conjunto, superen un umbral; esos casos se tratan como una sola compra.

## 4. La regla de las tres cotizaciones

Para compras de más de USD 10.000 se necesitan al menos tres cotizaciones comparables, con el mismo alcance y las mismas condiciones. Detalles del proceso:

- Las cotizaciones se piden por escrito a través de Nimbus Procure (módulo RFQ) o por correo, con una fecha de cierre de 7 días corridos.
- Deben ser de empresas independientes; no pueden pertenecer al mismo grupo económico.
- La planilla comparativa incluye: precio, plazos de entrega, condiciones de pago, garantía, referencias y evaluación de riesgos.
- Si se elige una opción que no es la más económica, se debe justificar por escrito (por ejemplo, mejor soporte, integración existente o menor riesgo de seguridad).

### Excepciones

Se puede omitir el requisito con aprobación del CFO en estos casos:

1. Proveedor único (patentes, licencias propietarias, servicios de un fabricante).
2. Emergencia operativa que ponga en riesgo el servicio a clientes.
3. Renovación de contratos vigentes con un aumento menor al 5% o al IPC, lo que sea menor.
4. Continuidad de un proyecto en curso ya adjudicado por competencia.

La excepción se registra en el campo "Single source" de Nimbus Procure con el formulario F-07.

## 5. Alta de proveedores

Ningún proveedor puede recibir una OC sin estar dado de alta y aprobado en el maestro de proveedores. El alta lo realiza exclusivamente el equipo de Compras, no el solicitante.

Pasos:

1. El solicitante pide el alta mediante el formulario "Alta de proveedor" en Nimbus Procure.
2. El proveedor completa el portal de autogestión (https://proveedores.nimbuscloud.example) con la siguiente documentación:
   - Constancia de inscripción fiscal (CUIT, RUT, NIT o equivalente).
   - Constancia de CBU o datos bancarios, en papel membretado y firmada, o certificado bancario.
   - Constancia de inscripción en Ingresos Brutos, certificados de exclusión o retención, si aplican.
   - Formulario de conflicto de intereses y aceptación del Código de Conducta para Proveedores.
   - Para servicios críticos, certificado de seguridad (por ejemplo SOC 2 o ISO 27001) y una póliza de seguro vigente.
3. Compras verifica la información contra el registro oficial (ARCA, SII, etc.) y contra listas restrictivas de sanciones.
4. Se realiza una llamada de verificación al número del proveedor registrado en un listado público (no al número informado en el correo) para confirmar los datos bancarios.
5. Aprobación por parte del Controller si la compra anual esperada supera USD 50.000.
6. El alta se completa en un plazo de 5 días hábiles desde que la documentación está completa.

Los cambios en datos bancarios de proveedores existentes siguen el mismo control de verificación telefónica y requieren la aprobación de dos personas de Finanzas. Esto es crítico para prevenir fraudes de suplantación (ver el documento de nómina y pagos).

### Evaluación de proveedores

Cada año Compras evalúa a los proveedores con compras superiores a USD 25.000 anuales usando cuatro criterios con ponderación: calidad (35%), cumplimiento de plazos (25%), precio (25%) y soporte (15%). Los proveedores con puntaje inferior a 60/100 pasan a un plan de mejora o se reemplazan.

## 6. Órdenes de compra

La OC es el documento que obliga a Nimbus Cloud frente al proveedor. Debe incluir:

- Número correlativo (formato OC-2026-00xxx).
- Proveedor, CUIT y contacto.
- Descripción, cantidad, precio unitario y moneda.
- Condición de pago y plazo de entrega.
- Centro de costo y cuenta contable.
- Aprobaciones electrónicas.

Si el valor final de la factura excede el de la OC en más del 5% o USD 500 (lo que sea menor), se debe emitir una modificación de OC antes de pagar. Las OC se cancelan automáticamente si no tienen movimientos en 90 días.

Las OC en moneda extranjera usan la cotización del día de emisión para el presupuesto, y la cotización del día de pago para el registro del gasto. Las diferencias de cambio las absorbe el área de Tesorería.

## 7. Contratos

Se firma un contrato escrito para toda compra superior a USD 25.000 o con duración superior a 12 meses. Las cláusulas mínimas son:

- Alcance, entregables y niveles de servicio (SLA).
- Precio, ajustes y moneda; los aumentos anuales se limitan al 8% o al IPC.
- Plazo y renovación; la renovación automática debe tener un aviso previo de 60 días.
- Confidencialidad y protección de datos personales.
- Cláusula de seguridad de la información y derecho de auditoría.
- Terminación anticipada con aviso de 30 días.
- Ley aplicable: Argentina, con jurisdicción en los tribunales ordinarios de la Ciudad de Buenos Aires.
- Anticorrupción y cumplimiento de la ley de ética.

Legal revisa todos los contratos mayores a USD 50.000 con un plazo de revisión de 5 días hábiles. Los contratos firmados se guardan en el repositorio "Nimbus Contracts" con alerta automática 90 días antes del vencimiento. Sólo firman contratos quienes tienen poder vigente: hasta USD 150.000, el CFO; por encima, el CEO.

## 8. Plazos de pago a proveedores

| Tipo de proveedor | Plazo estándar | Notas |
|---|---|---|
| Proveedores generales | 30 días desde la recepción de la factura | Corridas de pago los martes y viernes |
| Proveedores PyME locales | 15 días | Política de apoyo a pequeñas empresas |
| Proveedores de software SaaS | Según contrato (en general, pago anticipado) | Tarjeta virtual |
| Proveedores críticos de infraestructura (nube) | 45 días | Contrato marco |
| Proveedores del exterior | 30 días + 2 a 4 días de transferencia | Se aplica la normativa cambiaria vigente |

Descuentos por pronto pago: se aprovechan los descuentos del 2% a 10 días (condición "2/10 neto 30") cuando la tasa implícita supere el costo de financiamiento de Nimbus Cloud, evaluado por Tesorería.

Las facturas se reciben por el correo facturas.proveedores@nimbuscloud.example, y para ser válidas deben mencionar el número de OC. Las facturas sin OC se devuelven dentro de 3 días hábiles. Cuentas a Pagar publica el cronograma semanal de pagos todos los lunes, y los proveedores pueden consultar el estado en el portal.

### Retenciones a proveedores

Nimbus Cloud actúa como agente de retención de Ganancias, IVA y Ingresos Brutos conforme a la normativa. Se emiten los certificados dentro de los 10 días hábiles del pago. Ejemplo: una factura de USD 1.000 + IVA a un proveedor inscripto con retención del 2% de Ganancias se paga con USD 20 menos de retención.

## 9. Compras de software

Las compras de software y servicios SaaS tienen requisitos adicionales por los riesgos de seguridad y de datos.

1. **Revisión de seguridad:** todo software que acceda a datos de clientes, empleados o finanzas pasa por el formulario de evaluación de proveedores de TI. El equipo de Seguridad de la Información (seguridad@nimbuscloud.example) responde en 5 días hábiles.
2. **Revisión de privacidad:** si se tratan datos personales, Legal verifica que exista un acuerdo de procesamiento de datos (DPA).
3. **Catálogo de herramientas aprobadas:** antes de pedir una nueva herramienta, revisar el catálogo interno; si existe una alternativa, se debe usar.
4. **Licencias:** se compran por el menor número posible de usuarios y se revisan trimestralmente. Las licencias sin uso durante 60 días se reasignan o se dan de baja.
5. **Pago:** las suscripciones menores a USD 500 por año pueden pagarse con la tarjeta virtual de suscripciones de Finanzas; las de mayor valor siguen el circuito de OC.
6. **Renovaciones:** el dueño de cada herramienta es responsable de decidir la renovación al menos 45 días antes del vencimiento.

Está prohibido contratar software con la tarjeta personal sin autorización o utilizar versiones gratuitas con datos de producción. Las herramientas no autorizadas (shadow IT) detectadas se bloquean y se reportan al líder del área.

Ejemplo: el equipo de Marketing necesita una herramienta de automatización de campañas por USD 4.800 al año. Debe pasar por revisión de seguridad, comparar dos opciones, obtener la aprobación del Director de Marketing (rango USD 2.501 a 10.000) y se emite la OC por un año, con aviso de renovación a 45 días.

## 10. Conflictos de interés y obsequios

Ninguna persona puede participar en una decisión de compra si tiene un vínculo familiar, financiero o personal con el proveedor. Se debe declarar en el formulario F-02. Los obsequios de proveedores se rechazan si superan USD 50 y se informan a Compliance cualquiera sea el valor. Está prohibido recibir comisiones, descuentos personales o invitaciones a eventos durante un proceso de selección abierto.

## 11. Indicadores de gestión

- Porcentaje de compras con OC previa: objetivo 95% (actual 92%).
- Ahorro negociado sobre cotización inicial: objetivo 6%.
- Plazo promedio de alta de proveedor: 5 días hábiles.
- Facturas pagadas en término: objetivo 97%.

Los indicadores se presentan trimestralmente al Comité de Finanzas.
