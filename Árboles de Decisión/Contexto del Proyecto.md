## 🏗️ Contexto del Proyecto

La empresa, ubicada en **San Bernardo**, fabrica **hormigones, bloques y estructuras prefabricadas**.  
La gerencia busca estudiar los factores que influyen en la **venta y despacho** para predecir si un día será de **"alta demanda"** o **"baja demanda"**.

---

### 📋 Variables del Dataset

| Variable                  | Tipo                    | Descripción |
|----------------------------|--------------------------|--------------|
| fecha                     | Temporal                 | Día de registro |
| temperatura               | Numérica                 | Temperatura promedio del día (°C) |
| lluvia_mm                 | Numérica                 | Cantidad de lluvia en milímetros |
| dia_semana                | Categórica               | Día (Lunes, Martes, etc.) |
| feriado                   | Categórica (Sí/No)       | Si fue día feriado o no |
| promocion                 | Categórica (Sí/No)       | Si hubo promoción comercial activa |
| stock_disponible          | Numérica                 | Porcentaje de stock disponible en bodega (0-100) |
| personal turno            | Numérica                 | Cantidad de trabajadores operando ese día |
| atrasos_camiones          | Numérica                 | Número de camiones que llegaron tarde a cargar producto |
| tiempo_promedio_despacho  | Numérica                 | Promedio de tiempo (en minutos) entre pedido y despacho |
| ventas_altas              | Categórica (Sí/No)       | Si las ventas fueron altas o no (**variable objetivo**) |

---

## 🔹 Parte 1: Preparación de los Datos

1. Importar librerías necesarias.  
2. Simular o generar el dataset con al menos **300 registros**.  
3. Asegurar que las tendencias del contexto estén representadas en los datos.  
4. Explorar los datos: mostrar `head()`, tipos de datos e identificar nulos o inconsistencias.

---

## 🔹 Parte 2: Análisis Exploratorio (EDA)

1. Crear gráficos de **distribución** de variables numéricas.  
2. Usar **gráficos de conteo (`countplot`)** para variables categóricas.  
3. Generar un **mapa de calor de correlaciones**.  
4. Crear al menos **dos gráficos de dispersión (`scatterplot`)** que relacionen variables numéricas con `ventas_altas`.  
5. Responder preguntas sobre **tendencias**, **días de mayor venta** e **influencia visual**.

---

## 🔹 Parte 3: Construcción del Modelo

1. Convertir las variables categóricas a numéricas con `pd.get_dummies()`.  
2. Separar variables independientes (`X`) y dependiente (`y`).  
3. Dividir el dataset en entrenamiento y prueba usando `train_test_split`.  
4. Crear y entrenar un **Árbol de Decisión (`DecisionTreeClassifier`)** con profundidad máxima ajustable (`max_depth=...`).  
5. Evaluar el modelo con los datos de prueba mostrando:  
   - **Precisión (`accuracy_score`)**  
   - **Reporte de clasificación (`classification_report`)**

---

## 🔹 Parte 4: Visualización e Interpretación

1. Dibujar el árbol con `plot_tree()` y analizar sus ramas.  
2. Identificar qué variables aparecen más cerca de la raíz (las más importantes).  
3. Discutir:  
   - ¿Qué condiciones generan días de alta demanda?  
   - ¿Qué decisiones podrían tomar los gerentes para mejorar los días con ventas bajas?

---

## 🔹 Parte 5: Predicciones y Escenarios Futuros

1. Crear una **tabla con escenarios futuros** (por ejemplo, 5 días proyectados).  
2. Usar el modelo para **predecir si esos días tendrán ventas altas o bajas**.  
3. Visualizar los resultados con un **gráfico de barras o pastel**.  
4. Redactar una **conclusión técnica** y una **recomendación estratégica** para la gerencia.
