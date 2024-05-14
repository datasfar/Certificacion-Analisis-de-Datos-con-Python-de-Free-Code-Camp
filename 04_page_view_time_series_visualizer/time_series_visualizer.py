import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
from matplotlib.dates import MonthLocator

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')

# Clean data
df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')
df_clean = df[(df['value'] > df['value'].quantile(0.025)) & (df['value'] < df['value'].quantile(0.975))]
df = df_clean

def draw_line_plot():

    # Crea una función draw_line_plot que use Matplotlib para dibujar un gráfico de línea similar a "examples/Figure_1.png". El título debería ser Daily freeCodeCamp 
    # Forum Page Views 5/2016-12/2019. La etiqueta en el eje x debería ser Date y la etiqueta en el eje y debería ser Page Views.

    fig, ax = plt.subplots(figsize=(32, 10), dpi=100)
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    sns.lineplot(data=df_clean, legend=False)


    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():

    # Crea una función draw_bar_plot que dibuje un gráfico de barras similar a "examples/Figure_2.png". Debería mostrar el promedio diario de vistas a la página para cada 
    # mes agrupadas por año. La leyenda debería mostrar etiquetas mensuales y tener un título de Months. En la gráfica, la etiqueta en el eje x debería ser Years y la etiqueta 
    # en el eje y debería ser Average Page Views.
    df_bar = df_clean.copy()
    df_bar["Years"] = df_bar.index.year
    df_bar["Months"] = df_bar.index.month_name()
    df_bar = pd.DataFrame(df_bar.groupby(["Years", "Months"], sort=False)["value"].mean().round().astype(int))
    df_bar = df_bar.rename(columns={"value": "Average Page Views"})
    df_bar = df_bar.reset_index()
    missing_data = {
        "Years": [2016, 2016, 2016, 2016],
        "Months": ['January', 'February', 'March', 'April'],
        "Average Page Views": [0, 0, 0, 0]
        }

    df_bar = pd.concat([pd.DataFrame(missing_data), df_bar])

    fig, ax = plt.subplots(figsize=(18, 10), dpi=100)
    ax.set_title("Daily freeCodeCamp Forum Average Page Views per Month")

    chart = sns.barplot(data=df_bar, x="Years", y="Average Page Views", hue="Months", palette="tab10")
    chart.set_xticklabels(df_bar['Years'].unique(), rotation=90, horizontalalignment='center')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():

    # Crea draw_box_plot una función que use Seaborn para dibujar dos puntos de caja adyacentes similar a "examples/Figure_3.png". Estos diagramas de caja deberían mostrar 
    # como los valores son distribuídos dentro de un año dado o mes y como se compara con el tiempo. El título del primer gráfico debería ser Year-wise Box Plot (Trend) y 
    # el título del segundo gráfico debería ser Month-wise Box Plot (Seasonality). Asegurese que la etiqueta mes mes en la parte inferior empiece en Jan y los ejes x y y 
    # estén etiquetados correctamente. La plantilla incluye comandos para preparar los datos.
    # Prepare data for box plots (this part is done!)
    # Copia el DataFrame y resetea el índice
    
    # Prepare data for box plots (this part is done!)
    # Copia el DataFrame y resetea el índice
    df_box = df_clean.copy().reset_index()

    # Extrae el año y el mes de la fecha
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.strftime('%b')

    # Crea subgráficos para los box plots anuales y mensuales
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    # Boxplot anual
    sns.boxplot(data=df_box, x="year", y="value", ax=axes[0], hue='year', palette='tab10')
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    # Boxplot mensual
    month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    sns.boxplot(data=df_box, x="month", y="value", order=month_order, ax=axes[1], hue='month', palette='tab10')
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
