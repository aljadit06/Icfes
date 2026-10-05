import random
import requests
import streamlit as st
import streamlit.components.v1 as components

# Configuración de la página
st.set_page_config(
    page_title="Icfes interactivo 2027", page_icon="🎓", layout="wide"
)

# CONFIGURACIÓN WHATSAPP (CallMeBot configurado con tu número)
MI_NUMERO_WHATSAPP = "573007318439"
MI_API_KEY_WHATSAPP = (  # <-- Reemplaza "TU_API_KEY" con la clave que te envió el bot por WhatsApp
    "TU_API_KEY"
)


def enviar_alerta_whatsapp(puntaje, desglose):
    try:
        mensaje = (
            f"🎓 *¡Simulacro ICFES Finalizado!*\n\n"
            f"Ricardo Toro ha completado la prueba.\n"
            f"🎯 *Puntaje Global:* {round(puntaje)} / 500 pts\n\n"
            f"📊 *Desglose por área:*\n"
        )
        for area, datos in desglose.items():
            mensaje += (
                f"- {area}: {datos['correctas']}/20"
                f" ({round(datos['puntaje'])} pts)\n"
            )

        url = f"https://api.callmebot.com/whatsapp.php?phone={MI_NUMERO_WHATSAPP}&text={requests.utils.quote(mensaje)}&apikey={MI_API_KEY_WHATSAPP}"
        requests.get(url)
    except Exception as e:
        print(f"Error al enviar WhatsApp: {e}")


# 1. Saludo de voz automatizado para Ricardo Toro al cargar la página
voz_script = """
<script>
    function speakWelcome() {
        if ('speechSynthesis' in window) {
            let msg = new SpeechSynthesisUtterance("Bienvenido Ricardo Toro a tu simulación icfes");
            msg.lang = 'es-CO';
            msg.rate = 0.9;
            window.speechSynthesis.speak(msg);
        }
    }
    window.onload = speakWelcome;
</script>
"""
components.html(voz_script, height=0)

# Título principal de la plataforma
st.title("🎓 Icfes interactivo 2027 - Simulacro Oficial Grado 11")
st.markdown(
    "### Recorrido Integral: Las 5 Áreas del ICFES (20 preguntas aleatorias"
    " por componente)"
)

# Definir las 5 áreas oficiales del ICFES
AREAS_ICFES = [
    "Lectura Crítica",
    "Matemáticas",
    "Ciencias Naturales",
    "Sociales y Ciudadanas",
    "Inglés",
]


# Función para generar banco robusto y variado por componente
def generar_banco_verdadero(comp):
    banco = []
    for i in range(1, 101):
        if comp == "Lectura Crítica":
            temas_lc = [
                (
                    "Insectos a la carta",
                    (
                        "Estos pequeños animales, por lo general repulsivos para"
                        " nuestra cultura occidental, adquieren cada vez más"
                        " importancia en la alimentación mundial gracias al alto"
                        " contenido vitamínico que poseen. Una vaca requiere 8"
                        " kg de alimento para producir 1 kg de carne de res,"
                        " mientras que los insectos utilizan solo 2 kg para"
                        " producir 1 kg de carne. Además, los insectos no"
                        " necesitan refrigeración porque generan sustancias"
                        " antibióticas mientras están vivos."
                    ),
                    (
                        "De acuerdo con el texto anterior, ¿qué ventaja"
                        " principal representa la producción de insectos"
                        " frente a la ganadería tradicional?"
                    ),
                    [
                        (
                            "A. Los insectos requieren mayor cantidad de espacio"
                            " y recursos hídricos."
                        ),
                        (
                            "B. La producción de carne de insectos es más"
                            " eficiente en el uso de recursos de alimento y"
                            " no requiere refrigeración constante."
                        ),
                        (
                            "C. La cultura occidental acepta totalmente el"
                            " consumo masivo de insectos desde hace siglos."
                        ),
                        (
                            "D. Las vacas generan sustancias antibióticas"
                            " naturales que evitan su descomposición."
                        ),
                    ],
                    1,
                    (
                        "El texto señala explícitamente que los insectos usan"
                        " solo 2 kg de alimento frente a los 8 kg de la vaca,"
                        " además de poseer propiedades antibióticas que evitan"
                        " la refrigeración."
                    ),
                ),
                (
                    "El Grafeno",
                    (
                        "Una lámina de carbono, de un átomo de grosor, está"
                        " detrás del Nobel de Física. El grafeno es un nuevo"
                        " material extremadamente delgado y resistente que,"
                        " como conductor de la electricidad, se comporta como el"
                        " cobre, y como conductor de calor, supera a cualquier"
                        " otro material conocido."
                    ),
                    (
                        "Según el texto, ¿por qué se destaca el grafeno en"
                        " comparación con otros materiales?"
                    ),
                    [
                        (
                            "A. Por ser un material grueso y aislante total de"
                            " la electricidad."
                        ),
                        (
                            "B. Por ser extremadamente delgado, resistente y un"
                            " excelente conductor térmico y eléctrico."
                        ),
                        (
                            "C. Por ser un derivado directo de la madera y el"
                            " plástico industrial."
                        ),
                        (
                            "D. Por impedir por completo el paso de cualquier"
                            " tipo de energía."
                        ),
                    ],
                    1,
                    (
                        "El texto afirma que es extremadamente delgado,"
                        " resistente, conduce electricidad como el cobre y"
                        " supera a cualquier otro conductor de calor conocido."
                    ),
                ),
            ]
            t = temas_lc[(i - 1) % len(temas_lc)]
            lectura = (
                f"**TEXTO OFICIAL - {t[0].upper()} (Item #{i})**\n\n{t[1]}"
            )
            pregunta = t[2]
            opciones = t[3]
            correcta = t[4]
            explicacion = t[5]

        elif comp == "Matemáticas":
            temas_mat = [
                (
                    (
                        "Un docente ha preseleccionado algunos estudiantes para"
                        " una actividad deportiva. Al cumplir los requisitos,"
                        " escoge al azar un grupo de 3 estudiantes y encuentra"
                        " que puede hacer 10 posibles selecciones de grupos"
                        f" diferentes (Problema #{i})."
                    ),
                    (
                        "¿Cuántos estudiantes conforman el grupo"
                        " preseleccionado en total?"
                    ),
                    ["A. 13", "B. 10", "C. 6", "D. 5"],
                    3,
                    (
                        "Aplicando combinatoria C(n, 3) = 10, probando con n = 5"
                        " se tiene 5! / (3! * 2!) = 10. El grupo consta de 5"
                        " estudiantes."
                    ),
                ),
                (
                    (
                        "En una bolsa hay 3 bolas rojas, 3 negras y 12 blancas"
                        f" (Caso #{i}). Una persona afirma que al sacar una bola"
                        " al azar, los tres colores tienen la misma probabilidad"
                        " de salir."
                    ),
                    "¿Es verdadera esta afirmación?",
                    [
                        ("A. Sí, porque la cantidad de colores no importa."),
                        ("B. No, porque no se conoce el total de bolas."),
                        (
                            "C. No, pues hay más bolas de un color (blancas)"
                            " que de los otros dos."
                        ),
                        ("D. Sí, las bolas están repartidas equitativamente."),
                    ],
                    2,
                    (
                        "La afirmación es falsa porque las probabilidades"
                        " dependen del número de elementos de cada clase; al"
                        " haber 12 blancas, su probabilidad es mayor."
                    ),
                ),
            ]
            t = temas_mat[(i - 1) % len(temas_mat)]
            lectura = f"**CONTEXTO MATEMÁTICO - SITUACIÓN #{i}**\n\n{t[0]}"
            pregunta = t[1]
            opciones = t[2]
            correcta = t[3]
            explicacion = t[4]

        elif comp == "Ciencias Naturales":
            temas_cn = [
                (
                    (
                        "Investigaciones recientes han reportado que el hongo"
                        " *Pestalotiopsis microspora* es capaz de usar el"
                        " poliuretano como única fuente de alimento, gracias a"
                        " la secreción de enzimas que rompen enlaces"
                        f" específicos del polímero (Ensayo #{i})."
                    ),
                    (
                        "¿Qué ventaja ambiental ofrece el uso directo de este"
                        " hongo frente a la incineración de plásticos a más de"
                        " 500 °C?"
                    ),
                    [
                        (
                            "A. Su crecimiento no requiere infraestructura"
                            " compleja y reduce la emisión directa de"
                            " dióxido de carbono ($CO_2$)."
                        ),
                        (
                            "B. El hongo destruye el plástico convirtiéndolo en"
                            " material radioactivo."
                        ),
                        (
                            "C. La incineración contamina menos que cualquier"
                            " hongo."
                        ),
                        (
                            "D. El hongo elimina la necesidad de reciclar"
                            " cualquier tipo de materia orgánica."
                        ),
                    ],
                    0,
                    (
                        "La incineración emite grandes cantidades de $CO_2$. El"
                        " uso del hongo actúa como alternativa biológica"
                        " directa sin requerir hornos de quema."
                    ),
                )
            ]
            t = temas_cn[(i - 1) % len(temas_cn)]
            lectura = f"**CONTEXTO CIENTÍFICO - EXPERIMENTO #{i}**\n\n{t[0]}"
            pregunta = t[1]
            opciones = t[2]
            correcta = t[3]
            explicacion = t[4]

        elif comp == "Sociales y Ciudadanas":
            temas_soc = [
                (
                    (
                        "En una empresa, un miembro de la junta directiva"
                        " advierte al gerente que hay un grupo de empleados"
                        " movilizándose para conformar un sindicato. El gerente"
                        " responde: 'Propondré hablar con ellos para"
                        " comunicarles que aquí están prohibidas las protestas"
                        f" y se atenderá de forma individual' (Caso #{i})."
                    ),
                    (
                        "¿Qué derecho constitucional fundamental se pone en"
                        " riesgo con la propuesta del gerente?"
                    ),
                    [
                        ("A. El derecho al libre acceso a la información."),
                        ("B. El derecho a la participación política."),
                        ("C. El derecho a la libertad de creencias."),
                        ("D. El derecho a la libre asociación."),
                    ],
                    3,
                    (
                        "La constitución protege el derecho de los"
                        " trabajadores a asociarse libremente y crear"
                        " sindicatos; prohibir esta iniciativa vulnera la libre"
                        " asociación."
                    ),
                )
            ]
            t = temas_soc[(i - 1) % len(temas_soc)]
            lectura = f"**CONTEXTO SOCIO-POLÍTICO - SITUACIÓN #{i}**\n\n{t[0]}"
            pregunta = t[1]
            opciones = t[2]
            correcta = t[3]
            explicacion = t[4]

        else:  # Inglés
            temas_ing = [
                (
                    (
                        "Read the following sentence based on cultural body"
                        " language: 'In Nigeria, you mustn't use your left hand"
                        " to give or receive things because this hand is"
                        f" considered dirty' (Item #{i})."
                    ),
                    (
                        "According to the text, what is implied about the left"
                        " hand in Nigeria?"
                    ),
                    [
                        (
                            "A. It is used for all polite social"
                            " interactions."
                        ),
                        (
                            "B. It is culturally viewed as unacceptable for"
                            " sharing items."
                        ),
                        ("C. It must be washed before every meal."),
                        ("D. It represents good luck and fortune."),
                    ],
                    1,
                    (
                        "El texto indica explícitamente que no se debe usar la"
                        " mano izquierda para dar o recibir cosas porque se"
                        " considera sucia culturalmente."
                    ),
                )
            ]
            t = temas_ing[(i - 1) % len(temas_ing)]
            lectura = f"**READING COMPREHENSION - ITEM #{i}**\n\n{t[0]}"
            pregunta = t[1]
            opciones = t[2]
            correcta = t[3]
            explicacion = t[4]

        banco.append({
            "id": f"{comp}_{i}",
            "lectura": lectura,
            "pregunta": pregunta,
            "opciones": opciones,
            "correcta": correcta,
            "explicacion": explicacion,
        })
    return banco


# Inicializar base de datos general en session_state
if "banco_global" not in st.session_state:
    st.session_state.banco_global = {
        area: generar_banco_verdadero(area) for area in AREAS_ICFES
    }

if "respuestas_globales" not in st.session_state:
    st.session_state.respuestas_globales = {}

if "area_actual_idx" not in st.session_state:
    st.session_state.area_actual_idx = 0

if "examen_finalizado" not in st.session_state:
    st.session_state.examen_finalizado = False

if "whatsapp_enviado" not in st.session_state:
    st.session_state.whatsapp_enviado = False

if "preguntas_simulacro" not in st.session_state:
    st.session_state.preguntas_simulacro = {
        area: random.sample(st.session_state.banco_global[area], 20)
        for area in AREAS_ICFES
    }

# Botón global para reiniciar simulacro en la barra lateral
if st.sidebar.button("🔄 Reiniciar Simulacro Completo"):
    st.session_state.respuestas_globales = {}
    st.session_state.area_actual_idx = 0
    st.session_state.examen_finalizado = False
    st.session_state.whatsapp_enviado = False
    st.session_state.preguntas_simulacro = {
        area: random.sample(st.session_state.banco_global[area], 20)
        for area in AREAS_ICFES
    }
    st.rerun()

# FLUJO PRINCIPAL
if not st.session_state.examen_finalizado:
    area_actual = AREAS_ICFES[st.session_state.area_actual_idx]

    st.sidebar.title("Progreso del Simulacro")
    st.sidebar.write(
        f"Área actual: **{area_actual}** ({st.session_state.area_actual_idx + 1}"
        f" de {len(AREAS_ICFES)})"
    )
    st.sidebar.progress(
        (st.session_state.area_actual_idx + 1) / len(AREAS_ICFES)
    )

    st.header(f"Evaluación Oficial - Componente: {area_actual}")
    st.write(
        "Responde cada una de las 20 preguntas aleatorias de este componente."
        " Al enviar, avanzarás a la siguiente área hasta completar las 5"
        " pruebas."
    )

    preguntas_actuales = st.session_state.preguntas_simulacro[area_actual]

    with st.form(key=f"form_{area_actual}"):
        for i, pregunta in enumerate(preguntas_actuales):
            st.markdown(f"### Pregunta {i+1}")
            st.info(pregunta["lectura"])
            st.write(f"**Enunciado:** {pregunta['pregunta']}")

            resp = st.radio(
                "Selecciona tu respuesta:",
                pregunta["opciones"],
                index=None,
                key=f"q_{pregunta['id']}",
            )
            st.session_state.respuestas_globales[pregunta["id"]] = resp
            st.divider()

        siguiente_btn = (
            "Finalizar y Calcular Puntaje ICFES"
            if st.session_state.area_actual_idx == len(AREAS_ICFES) - 1
            else f"Guardar y Pasar a Siguiente Área"
        )
        submitted = st.form_submit_button(siguiente_btn)

        if submitted:
            if st.session_state.area_actual_idx < len(AREAS_ICFES) - 1:
                st.session_state.area_actual_idx += 1
                st.success(
                    f"¡Componente {area_actual} guardado con éxito! Cargando"
                    " siguiente área..."
                )
                st.rerun()
            else:
                st.session_state.examen_finalizado = True
                st.rerun()

# FLUJO DE RESULTADOS
else:
    puntaje_global_total = 0
    desglose_puntajes = {}

    for area in AREAS_ICFES:
        preguntas_area = st.session_state.preguntas_simulacro[area]
        correctas_area = 0
        total_area = len(preguntas_area)

        for p in preguntas_area:
            resp_dada = st.session_state.respuestas_globales.get(p["id"])
            if resp_dada is not None:
                if resp_dada == p["opciones"][p["correcta"]]:
                    correctas_area += 1

        puntaje_componente = (
            (correctas_area / total_area) * 100
            if total_area > 0
            else 0
        )
        desglose_puntajes[area] = {
            "correctas": correctas_area,
            "total": total_area,
            "puntaje": puntaje_componente,
        }
        puntaje_global_total += puntaje_componente

    # Enviar la alerta de WhatsApp una sola vez al finalizar
    if not st.session_state.whatsapp_enviado:
        enviar_alerta_whatsapp(puntaje_global_total, desglose_puntajes)
        st.session_state.whatsapp_enviado = True

    st.balloons()
    st.header("🎯 ¡Simulacro ICFES Finalizado con Éxito!")
    st.write(
        "A continuación se presenta el consolidado de tu rendimiento y el"
        " **Puntaje Global ICFES** estimado (escala oficial de 0 a 500"
        " puntos):"
    )

    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.metric(
            label="🎓 PUNTAJE GLOBAL ICFES",
            value=f"{round(puntaje_global_total)} / 500 pts",
        )
    with col2:
        if puntaje_global_total >= 350:
            st.success(
                "¡Excelente desempeño! Nivel alto para ingresar a"
                " universidades de alta exigencia."
            )
        elif puntaje_global_total >= 250:
            st.info(
                "¡Buen trabajo! Desempeño promedio superior consolidado."
            )
        else:
            st.warning(
                "¡Sigue practicando! Revisa detalladamente el solucionario"
                " inferior para mejorar."
            )

    st.markdown("---")
    st.subheader("📊 Desglose de Puntajes por Componente (Escala 0 - 100)")
    for area, datos in desglose_puntajes.items():
        st.write(
            f"**{area}:** {datos['correctas']} de {datos['total']} correctas —"
            f" **Puntaje:** {round(datos['puntaje'])} / 100"
        )
        st.progress(datos["puntaje"] / 100)

    # Zona protegida con contraseña para revisar solucionario completo
    st.sidebar.divider()
    st.sidebar.subheader("🔒 Zona de Respuestas y Explicaciones")
    codigo_ingresado = st.sidebar.text_input(
        "Ingresa el código de acceso:", type="password"
    )

    if codigo_ingresado == "@Ricardito8":
        st.sidebar.success("¡Código correcto!")
        st.markdown("---")
        st.header(
            "🔑 Solucionario Oficial y Explicaciones Detalladas (Acceso"
            " Restringido)"
        )
        st.write(
            "Estudia las respuestas correctas y explicaciones pedagógicas de"
            " todas las áreas evaluadas:"
        )

        for area in AREAS_ICFES:
            st.subheader(f"📖 Componente: {area}")
            for idx, p in enumerate(
                st.session_state.preguntas_simulacro[area]
            ):
                correcta_texto = p["opciones"][p["correcta"]]
                resp_usuario = st.session_state.respuestas_globales.get(
                    p["id"]
                )
                st.markdown(f"**Pregunta {idx+1}:** {p['pregunta']}")
                st.markdown(
                    f"👉 **Tu respuesta:** `{resp_usuario if resp_usuario else 'Sin responder'}`"
                )
                st.markdown(
                    f"✅ **Respuesta Correcta:** `{correcta_texto}`"
                )
                st.info(
                    f"💡 **Explicación pedagógica:** {p['explicacion']}"
                )
                st.markdown("---")
    elif codigo_ingresado:
        st.sidebar.error("Código incorrecto. Inténtalo de nuevo.")
