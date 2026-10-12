# Presupuesto y Cierre Contable en Nimbus Cloud

Versión 3.1 – Responsable: Controller y FP&A – Consultas: finanzas@nimbuscloud.example

## 1. Resumen

Este documento describe cómo Nimbus Cloud planifica su presupuesto anual, lo revisa con forecasts trimestrales, cierra los libros cada mes y reporta resultados a la Dirección. El ejercicio fiscal coincide con el año calendario (1 de enero al 31 de diciembre). La moneda funcional de reporte es el dólar estadounidense; la contabilidad local de Argentina se lleva en pesos y se convierte para consolidar. Los sistemas involucrados son el ERP "Nimbus Ledger", la herramienta de planificación "Nimbus Plan" y el tablero "Nimbus Insights".

## 2. Ciclo presupuestario anual

El presupuesto del año siguiente se prepara entre julio y diciembre, con este cronograma:

| Fecha | Hito | Responsable |
|---|---|---|
| 15 de julio | Lineamientos estratégicos y supuestos macro | CEO y CFO |
| 1 de agosto | Apertura de Nimbus Plan a los líderes de área | FP&A |
| 31 de agosto | Primera versión de presupuestos de área | Directores/as |
| Septiembre (semanas 2 y 3) | Sesiones de revisión uno a uno | FP&A y Business Partners |
| 30 de septiembre | Consolidado preliminar | FP&A |
| 15 de octubre | Presentación al Comité Ejecutivo | CFO |
| 15 de noviembre | Ajustes finales y escenarios | FP&A |
| 5 de diciembre | Aprobación del Directorio | CEO y Directorio |
| 20 de diciembre | Carga final del presupuesto aprobado en Nimbus Ledger | Controller |

### 2.1. Supuestos principales

Los supuestos se documentan en el "Libro de supuestos" y se actualizan cada año. Para el presupuesto 2027 (en preparación a esta fecha), los supuestos de planificación incluyen:

- Crecimiento de ingresos recurrentes (ARR) del 28% interanual.
- Churn mensual de clientes del 1,1% en planes Starter/Growth y del 0,4% en Business/Enterprise.
- Aumento salarial promedio del 14% en pesos (ajustado por paritarias e inflación) y 4% en USD para los equipos remotos.
- Incorporación neta de 45 personas, concentrada en Ingeniería (22), Ventas (12) y Customer Success (8).
- Tipo de cambio presupuestario: se fija como el valor del dólar mayorista proyectado, con un rango de sensibilidad de más o menos 10%.
- Costos de infraestructura en la nube equivalentes al 17% de los ingresos.

### 2.2. Escenarios

FP&A elabora tres escenarios: base, optimista (+10% de ingresos) y conservador (-12% de ingresos). En el escenario conservador se definen medidas de contingencia, como congelar contrataciones no críticas y reducir gastos discrecionales (viajes, eventos) en un 30%.

## 3. Centros de costo

Cada gasto se imputa a un centro de costo (CC) con un dueño responsable. La estructura vigente es:

| Código | Centro de costo | Responsable |
|---|---|---|
| CC-1100 | Ingeniería de Plataforma | VP Ingeniería |
| CC-1200 | Producto y Diseño | VP Producto |
| CC-1300 | Infraestructura y Seguridad | Director de Infraestructura |
| CC-2100 | Ventas Argentina | Director Comercial |
| CC-2210 | Ventas LATAM | Director Comercial |
| CC-2300 | Customer Success y Soporte | Director de Customer Success |
| CC-3100 | Marketing | Director de Marketing |
| CC-4100 | Finanzas y Administración | CFO |
| CC-4200 | Personas y Cultura | Directora de Personas |
| CC-4300 | Legal y Compliance | Gerente Legal |
| CC-9000 | Corporativo (no asignable) | CFO |

Los costos compartidos (alquiler de oficina, servicios de TI generales, licencias corporativas) se asignan a los centros de costo según criterios: el alquiler se distribuye por cantidad de personas en la sede; las licencias corporativas, por usuarios activos. La nueva asignación se revisa cada semestre.

La creación de un nuevo centro de costo requiere una solicitud del Director/a, justificación del negocio y aprobación del Controller. El plazo es de 5 días hábiles.

## 4. Forecast trimestral

Además del presupuesto anual, FP&A realiza un forecast actualizado cada trimestre, que reemplaza los meses restantes del año con proyecciones basadas en el desempeño real.

1. **Semana 1 del último mes del trimestre:** FP&A distribuye las plantillas en Nimbus Plan con los datos reales de los dos primeros meses.
2. **Semana 2:** los dueños de centros de costo revisan y actualizan sus proyecciones.
3. **Semana 3:** reuniones de revisión con Business Partners; se verifican contrataciones, proyectos y compromisos.
4. **Semana 4:** consolidación y presentación al CFO.
5. **Primeros 10 días hábiles del trimestre siguiente:** presentación al Comité Ejecutivo.

Convenciones: los forecasts se nombran 3+9, 6+6 y 9+3 (meses reales + meses proyectados). Los umbrales de revisión obligatoria son una variación mayor al 5% en ingresos totales o mayor al 8% en el gasto de un centro de costo respecto del presupuesto.

## 5. Cierre mensual

El cierre contable se realiza durante los primeros 8 días hábiles del mes siguiente. Se busca el objetivo de "cierre en 8 días" y la meta del año próximo es 6.

### 5.1. Calendario de cierre (días hábiles - DH)

| Día | Actividad | Responsable |
|---|---|---|
| DH-1 (último día del mes) | Corte de operaciones; se bloquean nuevas imputaciones de gastos en Nimbus Expenses para el período | Contabilidad |
| DH+1 | Conciliaciones bancarias y de tarjetas; registro de la facturación mensual | Tesorería y Contabilidad |
| DH+2 | Cierre de cuentas a pagar: provisión de facturas no recibidas (accruals) | Cuentas a Pagar |
| DH+3 | Cierre de nómina: asientos de sueldos, cargas sociales y provisiones de SAC y vacaciones | Personas y Contabilidad |
| DH+3 | Reconocimiento de ingresos diferidos y amortización de capex | Contabilidad |
| DH+4 | Diferencias de cambio y revalorización de saldos en moneda extranjera | Tesorería |
| DH+5 | Conciliaciones intercompañía y consolidación | Controller |
| DH+6 | Revisión analítica de variaciones; comentarios de los dueños de CC | FP&A |
| DH+7 | Revisión final y aprobación del Controller | Controller |
| DH+8 | Bloqueo del período y publicación de reportes | CFO |

Cualquier ajuste posterior al DH+8 se registra como ajuste del período siguiente, salvo errores materiales (más de USD 25.000), que se tratan con aprobación del CFO.

### 5.2. Lista de verificación del cierre

Antes de bloquear el período, Contabilidad confirma estos puntos en la lista de verificación de Nimbus Ledger:

- Todas las conciliaciones bancarias con diferencias menores a USD 100.
- Cuentas puente y transitorias en cero o explicadas.
- Ingresos diferidos conciliados contra Nimbus Billing con una diferencia máxima de 0,1%.
- Accruals con documentación respaldatoria superiores a USD 2.000.
- Saldos intercompañía conciliados entre Argentina, Uruguay y Brasil.
- Provisión de deudores incobrables actualizada según el aging.
- Asientos manuales revisados por una persona distinta de quien los registró.

Todo asiento manual mayor a USD 10.000 requiere aprobación del Controller.

## 6. Reconocimiento de ingresos

Los ingresos por suscripción se reconocen de manera lineal durante el período de servicio. Una factura anual de USD 6.490 emitida el 1 de marzo genera un ingreso diferido que se libera USD 540,83 por mes. Los servicios de implementación se reconocen al completarse los hitos de entrega. Las bonificaciones y créditos por SLA reducen el ingreso del período en que se otorgan.

## 7. Control de variaciones

Cada mes, FP&A produce el informe de variaciones comparando el real contra el presupuesto y contra el mes anterior.

- **Umbral de explicación:** toda variación superior al 10% y a USD 5.000 en una línea de un centro de costo requiere un comentario escrito del responsable.
- **Variaciones favorables y desfavorables:** se explican ambas. Una subejecución importante puede ser un problema (proyectos demorados) tanto como una sobrejecución.
- **Clasificación:** cada variación se etiqueta como precio, volumen, calendario (timing) o cambio no planificado.
- **Acciones:** si la desviación acumulada de un centro de costo supera el 10% a mitad de año, se solicita un plan de acción en 10 días hábiles.

Ejemplo: el CC-3100 Marketing presupuestó USD 80.000 en eventos para octubre, pero gastó USD 96.500. La variación es USD 16.500 (20,6%), por encima del umbral. El Director de Marketing debe explicar que el evento "Nimbus Summit" se adelantó y de ahí que sea una variación de calendario, no una desviación del presupuesto anual.

### 7.1. Reasignaciones presupuestarias

Los traspasos entre líneas dentro de un mismo centro de costo hasta el 10% del presupuesto los autoriza el Director/a. Los traspasos entre centros de costo requieren la aprobación del CFO. No se pueden pasar fondos de capex a opex ni de opex a capex sin pasar por el Controller.

## 8. Capex vs. opex

La clasificación define si un gasto impacta de inmediato en resultados o se activa y se amortiza.

| Criterio | Opex (gasto) | Capex (inversión) |
|---|---|---|
| Naturaleza | Consumo dentro del período | Bien o desarrollo con beneficio mayor a 12 meses |
| Umbral mínimo | Cualquier monto | USD 2.500 por ítem o conjunto |
| Ejemplos | Alquiler, suscripciones SaaS, publicidad, mantenimiento, capacitación | Servidores propios, notebooks, mobiliario, desarrollo interno capitalizable |
| Tratamiento contable | Resultado del mes | Activo fijo o intangible, con amortización |

Reglas de amortización (método lineal):

- Equipos informáticos: 3 años.
- Mobiliario: 5 años.
- Mejoras en inmuebles alquilados: durante el plazo del contrato.
- Software desarrollado internamente: 3 años desde que se pone en producción.

El desarrollo interno se capitaliza únicamente durante la fase de desarrollo de nuevas funcionalidades, cuando se cumplen los criterios de factibilidad técnica y comercial. Las tareas de mantenimiento, corrección de errores y soporte son opex. Las horas de ingeniería se registran en la herramienta de seguimiento de tiempos con el código "CAP" para las tareas elegibles; la capitalización del trimestre pasado fue de USD 410.000 sobre un total de USD 2,1 millones de costos de ingeniería.

Ejemplo: se compran 20 notebooks a USD 1.900 cada una (USD 38.000). Cada equipo supera el umbral de USD 2.500 solo en conjunto; se activan como un lote y se amortizan en 36 meses, a USD 1.055,56 por mes.

## 9. Reportes a la Dirección

| Reporte | Frecuencia | Destinatarios | Fecha de entrega |
|---|---|---|---|
| Flash de ingresos y caja | Semanal (lunes) | CEO, CFO | 10:00 |
| Paquete de cierre mensual (P&L, balance, flujo de caja) | Mensual | Comité Ejecutivo | DH+8 |
| Tablero de KPI SaaS (ARR, MRR, churn, NRR, CAC, LTV) | Mensual | Comité Ejecutivo | DH+9 |
| Informe de variaciones por centro de costo | Mensual | Directores/as de área | DH+8 |
| Forecast | Trimestral | Comité Ejecutivo y Directorio | Hasta el día 10 hábil del trimestre |
| Informe al Directorio | Trimestral | Directorio | Hasta el día 20 del mes siguiente |
| Estados financieros auditados | Anual | Directorio y accionistas | 31 de marzo |

Indicadores SaaS de referencia al último cierre: ARR de USD 31,4 millones, NRR de 108%, margen bruto de 74% y runway superior a 30 meses. El "Rule of 40" (crecimiento + margen) se monitorea con una meta de 40 o más.

## 10. Auditoría externa y controles

Una firma de auditoría externa revisa los estados financieros anualmente. Los auditores tienen acceso de solo lectura a Nimbus Ledger y a los repositorios de soporte durante el período de trabajo (enero a marzo). Se mantiene la documentación contable por un mínimo de 10 años. Los controles clave del cierre (conciliaciones, aprobaciones de asientos manuales, accesos) se prueban trimestralmente por el equipo de Control Interno.

## 11. Preguntas frecuentes

**¿Cómo pido una ampliación de presupuesto a mitad de año?** Se envía una solicitud a FP&A con justificación, monto y fuente de financiación; hasta USD 20.000 lo aprueba el CFO, y por encima, el Comité Ejecutivo.

**¿Qué pasa si una factura llega después del cierre?** Si el servicio se prestó en el período, se debería haber provisionado. Si no hubo provisión, se contabiliza en el mes siguiente y se informa al área para que mejore su estimación.

**¿Cuándo deben avisar las áreas sobre gastos importantes?** Todo compromiso superior a USD 10.000 que impacte en el mes debe comunicarse a Contabilidad antes del DH-3 del cierre.
