#Instalar paquetes necesarios
install.packages("readxl","dlpyr")
#cargar paquetes
library("readxl")
library("dplyr")
library("tidyr")
library("stringr")


#Cargar el dataset
df <- read.csv("C:/Users/rmont/Downloads/Proyecto final Exploracion/archive/netflix_titles.csv")

#Conocer el dataset
View(df)

#Para observar el tipo de dato en cada columna y asi sus totales
summary(df)           
str(df)
#Se observan valores faltantes o en blanco en algunas columnas, se procede a verificar y tratarlos

#Valores nulos por columas
colSums(is.na(df)) 

#Doble verificacion
any(is.na(df))   

#Revisar duplicados
sum(duplicated(df))

#No se encuentran valores NA en las columnas

#Revisar rango de años
sort(unique(df$release_year))

#Filtrar dataset para rango de fechas de 2016 al 2021
df_filtrado <- df %>%
  filter(release_year %in% c(2020,2021))

View(df_filtrado)
sort(unique(df_filtrado$release_year))

# Se revisa si existen valores en blanco
sapply(df_filtrado, function(x) sum(x == "" | x == " ", na.rm = TRUE))

#Cambiamos valores en blanco por NA 
df_filtrado <- df_filtrado[trimws(df_filtrado$director) != "" & 
                             trimws(df_filtrado$cast) != "" &
                             trimws(df_filtrado$country) != "", ]
#Verificamos
sapply(df_filtrado, function(x) sum(x == "" | x == " ", na.rm = TRUE))

#Eliminar columnas 
df_nuevo <- df_filtrado %>%
  select(-show_id, -description)
View(df_nuevo)

#Renombrar columnas
df_nuevo <- df_nuevo %>%
  rename(
    Tipo = type,
    Titulo = title,
    Director = director,
    Reparto = cast,
    Pais = country,
    Fecha_agregado = date_added,
    Anio_lanzamiento = release_year,
    Clasificacion = rating,
    Duracion = duration,
    Listado_en = listed_in
  )

View(df_nuevo)

#Se observa que las columnas Director, Reparto, Pais, Fecha, contienen mas de 1 dato por fila, 

#Separar datos en Reparto
df <- df_nuevo %>%
  separate(Reparto, into = c("Reparto", "Reparto_2"), sep = ", ", fill = "right") %>%
  mutate(Reparto = replace_na(Reparto, "Desconocido")) %>%
  select(-Reparto_2)

# Separar y quedarte solo con Director
df <- df %>%
  separate(Director, into = c("Director", "Director_2"), sep = ", ", fill = "right") %>%
  mutate(Director = replace_na(Director, "Desconocido")) %>%
  select(-Director_2)

#Separar datos en Pais
df <- df %>%
  separate(Pais, into = c("Pais", "Pais_2"), sep = ", ", fill = "right") %>%
  mutate(Pais = replace_na(Pais, "No Aplica")) %>%
  select(-Pais_2)

#Separar y reemplazar NA en Pais
df <- df %>%
  separate(Listado_en, into = c("Listado_en", "Listado_2"), sep = ", ", fill = "right") %>%
  mutate(Listado_en = replace_na(Listado_en, "No Aplica")) %>%
  select(-Listado_2)



#Transformacion de la columna Fecha
#Aqui la transformacion que se hara es eliminar el año de la pelicula ya que es un dato redundante
#Ya que existe una columna especifica para el año 
df <- df %>%
  mutate(Fecha_agregado = str_replace(Fecha_agregado, ",.*", ""))


#Guardar dataset limpio
write.csv(as.data.frame(df), "C:/Users/rmont/Downloads/Proyecto final Exploracion/archive/datos_limpios.csv", row.names = FALSE)

#Tablas de Contingencia

#Tabla Tipo/Pais
tabla_tipo_pais <- table(df$Pais,df$Tipo)
write.csv(as.data.frame(tabla_tipo_pais), "C:/Users/rmont/Downloads/Proyecto final Exploracion/archive/tabla_tipo_pais.csv", row.names = FALSE)

#Tabla Tipo/Clasificacion
tabla_tipo_clasificacion<-table(df$Tipo, df$Clasificacion)
write.csv(as.data.frame(tabla_tipo_clasificacion), "C:/Users/rmont/Downloads/Proyecto final Exploracion/archive/tabla_tipo_clasificacion.csv", row.names = FALSE)

#Tabla Listado/Tipo
tabla_listado_tipo<-table(df$Listado_en, df$Tipo)
write.csv(as.data.frame(tabla_listado_tipo), "C:/Users/rmont/Downloads/Proyecto final Exploracion/archive/tabla_listado_tipo.csv", row.names = FALSE)

