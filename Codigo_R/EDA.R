#cargar paquetes
library("readxl")
library("dplyr")
library("tidyr")
library("stringr")
library("ggplot2")


df <- read.csv("C:/Users/rmont/Downloads/Proyecto final Exploracion/archive/datos_limpios.csv")

# Ver los primeros registros del dataset
head(df)

# Resumen general de los datos (tipo de variables, estadísticas básicas)
summary(df)

# Verificar los tipos de datos de cada columna
str(df)

#Iniciar Análisis EDA

# Cantidad de títulos por tipo de contenido
tipo_count <- table(df$Tipo)
tipo_count
ggplot(data = as.data.frame(tipo_count), aes(x = Var1, y = Freq)) +
  geom_bar(stat = "identity", fill = "mediumseagreen") +
  labs(title = "Distribución de Títulos por Tipo de Contenido", x = "Tipo de Contenido", y = "Número de Títulos") +
  theme_minimal()

# Cantidad de títulos por clasificación
clasificacion_count <- table(df$Clasificacion)
clasificacion_count_df <- data.frame(Clasificacion = names(clasificacion_count), TituloCount = as.vector(clasificacion_count))
ggplot(clasificacion_count_df, aes(x = reorder(Clasificacion, TituloCount), y = TituloCount)) +
  geom_bar(stat = "identity", fill = "steelblue") +
  labs(title = "Distribución de Títulos por Clasificación", x = "Clasificación", y = "Número de Peliculas") +
  theme_minimal()

# Cantidad de contenidos se lanzaron por año
anio_cuenta<- table(df$Anio_lanzamiento)
ggplot(as.data.frame(anio_cuenta), aes(x = Var1, y = Freq)) + 
  geom_bar(stat = "identity", fill = "steelblue") +
  labs(title = "Número de Títulos por Año de Lanzamiento", 
       x = "Año de Lanzamiento", 
       y = "Número de Títulos") +
  theme_minimal()

# Top 10 directores más frecuentes

top_10_directores <- sort(table(df$Director), decreasing = TRUE)[1:10]
top_10_directores_df <- data.frame(Director = names(top_10_directores), Frecuencia = as.vector(top_10_directores))
ggplot(top_10_directores_df, aes(x = reorder(Director, Frecuencia), y = Frecuencia)) +
  geom_bar(stat = "identity", fill = "steelblue") +
  coord_flip() +
  labs(title = "Top 10 Directores Más Frecuentes", x = "Director", y = "Frecuencia") +
  theme_minimal()

# País con más títulos
pais_mas_titulos <- sort(table(df$Pais), decreasing = TRUE)
pais_mas_titulos_df <- as.data.frame(pais_mas_titulos)
ggplot(pais_mas_titulos_df, aes(x = reorder(Var1, Freq), y = Freq)) +
  geom_bar(stat = "identity", fill = "darkgreen") +
  coord_flip() +
  labs(title = "País con Más Títulos", x = "País", y = "Número de Títulos") +
  theme_minimal()

# Movimiento lineal de Titulos a traves del Tiempo
df %>%
  count(Anio_lanzamiento) %>%
  ggplot(aes(x = Anio_lanzamiento, y = n)) +
  geom_line(group = 1, color = "steelblue", size = 1.2) +
  geom_point(color = "red") +
  labs(title = "Número de Lanzamientos por Año",
       x = "Año de Lanzamiento",
       y = "Cantidad de Títulos") +
  theme_minimal()

# Tipo de contenido es más común por país
pais_tipo <-table(df$Pais, df$Tipo)
pais_tipo_df <- as.data.frame(pais_tipo)
colnames(pais_tipo_df) <- c("Pais", "Tipo", "Frecuencia")
ggplot(pais_tipo_df, aes(x = reorder(Pais, -Frecuencia), y = Frecuencia, fill = Tipo)) +
  geom_bar(stat = "identity") +
  coord_flip() +
  labs(title = "Distribución de Tipos de Contenido por País",
       x = "País", y = "Cantidad de Títulos", fill = "Tipo") +
  theme_minimal()

# Bloxpot de Duración por tipo de contenido
bloxplot <- df %>%
  mutate(Duracion_num = case_when(
    str_detect(Duracion, "min") ~ as.numeric(str_extract(Duracion, "\\d+")),
    str_detect(Duracion, "Season") ~ as.numeric(str_extract(Duracion, "\\d+")) * 45,
    TRUE ~ NA_real_
  ))
ggplot(bloxplot, aes(x = Tipo, y = Duracion_num)) +
  geom_boxplot(fill = "skyblue") +
  labs(title = "Duración por Tipo de Contenido",
       x = "Tipo",
       y = "Duración (min)") +
  theme_minimal()

# Distribución de Géneros por Tipo de Contenido
ggplot(df, aes(x = Listado_en, fill = Tipo)) +
  geom_bar() +
  coord_flip() +
  labs(title = "Distribución de Géneros por Tipo de Contenido", x = "Género", y = "Conteo")





