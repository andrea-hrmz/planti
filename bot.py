import discord
from discord.ext import commands
import random
import requests
from openai import OpenAI


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Ha iniciado sesión como {bot.user}')

#IA
ai = OpenAI(api_key="La api va aquí")

@bot.command()
async def ia(ctx, *, mensaje):
    respuesta = ai.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "Eres divertida y amigable."},
            {"role": "user", "content": mensaje}
        ]
    )
    
    await ctx.send(respuesta.choices[0].message.content)

datos = ["Hay muchas formas de apoyar las causas ambientales. Una de ellas es hacer donaciones a organizaciones que cuidan y protegen al planeta de quienes quieren opacar su belleza",
        "El consumo responsable es una buena opción, no compres cosas que no necesitas y regala las cosas que ya no usas a las personas que lo necesitan.",
        "A veces dejamos luces o cargadores conectados sin pensar, pero eso sigue consumiendo energía. No es solo por ahorrar luz, sino porque esa energía se produce contaminando en muchos casos. Es como gastar sin darte cuenta, pero con el planeta.",
        "Cuando te cepillas los dientes o lavas algo y dejas la llave abierta, se desperdicia muchísima agua. Cerrar la llave en esos momentos es un cambio chiquito que, repetido diario, ahorra litros y litros.",
        "Las bolsas de plástico se usan unos minutos… pero tardan años en degradarse. Llevar una bolsa reutilizable es algo súper simple que evita un montón de basura innecesaria.",
        "Popotes, vasos, cubiertos de plástico… se usan una vez y terminan contaminando. Si puedes evitarlos o usar versiones reutilizables, ya estás reduciendo muchísimo tu impacto.",
        "Cada vez que tiras comida, no solo es la comida: es el agua, la energía y el trabajo que se usó para producirla. Servirte solo lo que vas a comer o guardar sobras hace más diferencia de lo que parece.",
        "Camina cuando se pueda, no siempre es posible, pero si un lugar está cerca, caminar en vez de usar carro ayuda a reducir contaminación. Además, bonus: despejas la mente un rato.",
        "Tener plantas no solo se ve bonito, también ayuda al ambiente y te conecta más con cuidarlo. Es como un recordatorio vivo de “oye, hay que cuidar esto”.",
        "Frascos, cajas, ropa… muchas cosas pueden tener una segunda vida. Antes de tirarlo, piensa “¿puedo usar esto para otra cosa?”. A veces sí, y ahorras basura.",
        "No todo lo que quieres necesitas. Pensarlo dos veces antes de comprar evita acumulación y reduce producción innecesaria. Menos cosas, menos impacto.",
        "A veces imprimimos cosas que podríamos ver en el celular o compu. Usar menos papel ayuda a reducir la tala de árboles. Y si ya usas hojas, intenta aprovecharlas por ambos lados.",
        "A veces imprimimos cosas que podríamos ver en el celular o compu. Usar menos papel ayuda a reducir la tala de árboles. Y si ya usas hojas, intenta aprovecharlas por ambos lados.",
        "Cuida tu ropa para que dure más, no es solo moda: mientras más dura tu ropa, menos necesitas comprar. Lavar con cuidado, no usar la secadora tanto y arreglar prendas evita que terminen en la basura rápido.",
        "Shampoo, jabón, limpieza… hay opciones donde puedes rellenar el envase. Eso reduce muchísimo plástico sin que cambies tanto tu rutina.",
        "No necesitas hacerlo perfecto. Con separar orgánico y reciclable ya haces diferencia, porque facilitas que lo reciclable no termine mezclado y se pueda aprovechar.",
        "Lava frutas y verduras en un recipiente. En vez de dejar el agua corriendo, usa un bowl. Luego esa misma agua la puedes usar para plantas o limpieza ligera. Es como “exprimirle valor” al agua.",
        "A veces compras algo pequeño y viene con mil capas de plástico 😭. Elegir productos con menos empaque reduce basura desde el inicio.",
    ]

def dato_del_dia():
    dato = random.choice(datos)
    return dato

@bot.command('dato')
async def dato(ctx):
    await ctx.send(dato_del_dia())

bot.run("tu token aquí")

